"""Minimal GitHub REST client: auth, pagination, rate-limit handling.

Kept dependency-free on purpose — this repo should stay runnable with a bare
Python 3 and a token, both locally and inside GitHub Actions.
"""
import json
import os
import subprocess
import time
import urllib.error
import urllib.parse
import urllib.request

API = "https://api.github.com"


def token() -> str:
    """Token from the environment, falling back to the local gh CLI login."""
    env = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if env:
        return env
    out = subprocess.run(
        ["gh", "auth", "token"], capture_output=True, text=True, check=True
    )
    return out.stdout.strip()


class Client:
    def __init__(self) -> None:
        self._headers = {
            "Authorization": f"Bearer {token()}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "awesome-jev-discovery",
        }

    @staticmethod
    def _is_rate_limited(err: urllib.error.HTTPError) -> bool:
        return (
            err.headers.get("Retry-After") is not None
            or err.headers.get("X-RateLimit-Remaining") == "0"
        )

    def get(self, path: str, **params) -> dict:
        url = f"{API}{path}"
        if params:
            url += "?" + urllib.parse.urlencode(params)
        req = urllib.request.Request(url, headers=self._headers)
        for attempt in range(5):
            try:
                with urllib.request.urlopen(req, timeout=30) as resp:
                    return json.load(resp)
            except urllib.error.HTTPError as err:
                # 403 means two different things. A secondary rate limit is
                # worth waiting out; a token without the right scope never
                # succeeds, and retrying it just buries the real reason.
                if err.code == 403 and not self._is_rate_limited(err):
                    raise PermissionError(
                        f"403 from {path}: {err.read().decode('utf-8', 'replace')[:300]}\n"
                        "The code search endpoint needs a personal access token with "
                        "`public_repo` scope. GitHub Actions' built-in GITHUB_TOKEN "
                        "cannot use it — set GH_PAT instead."
                    ) from err
                if err.code in (403, 429):
                    wait = int(err.headers.get("Retry-After") or 2 ** (attempt + 3))
                    time.sleep(min(wait, 120))
                    continue
                raise
        raise RuntimeError(f"gave up after 5 attempts: {url}")

    def search_repos(self, query: str) -> tuple[list[dict], int]:
        """Return (items, total_count). The API refuses to page past 1000 items,
        so callers must slice a query that reports more than that."""
        items, page = [], 1
        total = 0
        while True:
            data = self.get(
                "/search/repositories", q=query, per_page=100, page=page,
                sort="updated", order="desc",
            )
            total = data.get("total_count", 0)
            batch = data.get("items", [])
            items.extend(batch)
            if len(batch) < 100 or page >= 10:
                return items, total
            page += 1
            time.sleep(1)

    def get_repo(self, full_name: str) -> dict | None:
        """Repo metadata, or None if it no longer exists publicly."""
        try:
            return self.get(f"/repos/{full_name}")
        except urllib.error.HTTPError as err:
            if err.code in (404, 451):
                return None
            raise

    def search_code(self, query: str, max_pages: int = 10) -> set[str]:
        """Repos whose code matches. Returns full_names only — search/code hands
        back a stripped repository object without stars or dates.

        Code search is limited to 10 requests/minute and 1000 results, so this
        paces itself and accepts partial coverage of very common matches.
        """
        repos: set[str] = set()
        for page in range(1, max_pages + 1):
            data = self.get("/search/code", q=query, per_page=100, page=page)
            items = data.get("items", [])
            repos.update(i["repository"]["full_name"] for i in items)
            if len(items) < 100:
                break
            time.sleep(6)
        return repos

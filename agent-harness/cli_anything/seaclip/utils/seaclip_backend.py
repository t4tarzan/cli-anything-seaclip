"""HTTP client for SeaClip-Lite FastAPI backend."""

import os
import requests
from typing import Any

DEFAULT_BASE_URL = "http://127.0.0.1:5200"


class SeaClipBackend:
    """Thin HTTP client wrapping the SeaClip-Lite FastAPI endpoints."""

    def __init__(self, base_url: str | None = None, timeout: int = 30):
        self.base_url = (
            base_url
            or os.environ.get("SEACLIP_URL")
            or DEFAULT_BASE_URL
        ).rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()

    # ── helpers ───────────────────────────────────────────────────────

    def _url(self, path: str) -> str:
        return f"{self.base_url}{path}"

    def _get(self, path: str, params: dict | None = None) -> Any:
        r = self.session.get(self._url(path), params=params, timeout=self.timeout)
        r.raise_for_status()
        return r.json()

    def _post(self, path: str, json: dict | None = None) -> Any:
        r = self.session.post(self._url(path), json=json, timeout=self.timeout)
        r.raise_for_status()
        return r.json()

    def _delete(self, path: str) -> Any:
        r = self.session.delete(self._url(path), timeout=self.timeout)
        r.raise_for_status()
        return r.json()

    # ── health ────────────────────────────────────────────────────────

    def health(self) -> dict:
        return self._get("/health")

    # ── issues ────────────────────────────────────────────────────────

    def list_issues(
        self,
        status: str | None = None,
        priority: str | None = None,
        search: str | None = None,
        limit: int | None = None,
    ) -> list[dict]:
        params: dict[str, Any] = {}
        if status:
            params["status"] = status
        if priority:
            params["priority"] = priority
        if search:
            params["search"] = search
        if limit:
            params["limit"] = limit
        return self._get("/api/issues", params=params)

    def create_issue(
        self, title: str, description: str = "", priority: str = "medium"
    ) -> dict:
        return self._post(
            "/api/issues",
            json={"title": title, "description": description, "priority": priority},
        )

    def move_issue(self, issue_id: str, column: str) -> dict:
        return self._post(f"/api/issues/{issue_id}/move", json={"column": column})

    def update_issue_status(self, issue_id: str, status: str) -> dict:
        return self._post(f"/api/issues/{issue_id}/status", json={"status": status})

    def delete_issue(self, issue_id: str) -> dict:
        return self._delete(f"/api/issues/{issue_id}")

    # ── agents ────────────────────────────────────────────────────────

    def list_agents(self) -> list[dict]:
        return self._get("/api/agents")

    # ── pipeline ──────────────────────────────────────────────────────

    def start_pipeline(self, issue_id: str, mode: str = "auto") -> dict:
        return self._post(f"/api/pipeline/{issue_id}/start", json={"mode": mode})

    def pipeline_status(self, issue_id: str) -> dict:
        return self._get(f"/api/pipeline/{issue_id}/status")

    def resume_pipeline(self, issue_id: str) -> dict:
        return self._post(f"/api/pipeline/{issue_id}/resume")

    def stop_pipeline(self, issue_id: str) -> dict:
        return self._post(f"/api/pipeline/{issue_id}/stop")

    # ── scheduler ─────────────────────────────────────────────────────

    def list_schedules(self) -> list[dict]:
        return self._get("/api/scheduler")

    def add_schedule(self, config: dict) -> dict:
        return self._post("/api/scheduler/add", json=config)

    def sync_schedule(self, schedule_id: str) -> dict:
        return self._post(f"/api/scheduler/{schedule_id}/sync")

    # ── activity ──────────────────────────────────────────────────────

    def list_activity(self, limit: int | None = None) -> list[dict]:
        params: dict[str, Any] = {}
        if limit:
            params["limit"] = limit
        return self._get("/api/activity", params=params)

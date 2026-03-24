"""Knowledge Organizer Subagent - Stub.

Notion/Obsidian/Zotero operations are handled directly by Claude Code
via MCP tools (notion-search, notion-fetch, notion-create-pages, etc.).
This module exists only for orchestrator registration.
"""

from __future__ import annotations

import logging
from typing import Any

from agents.core.base_agent import AgentStatus, BaseAgent, TaskResult

logger = logging.getLogger("subagent.knowledge_organizer")


class KnowledgeOrganizerSubagent(BaseAgent):
    """Stub — real operations use Notion MCP directly via Claude Code."""

    def __init__(self) -> None:
        super().__init__(
            name="knowledge_organizer",
            description="Notion + Obsidian + Zotero (via MCP direto)",
        )

    async def execute(self, task: dict[str, Any]) -> TaskResult:
        """Delegate to Claude Code MCP tools."""
        self.status = AgentStatus.RUNNING
        try:
            return TaskResult(
                success=False,
                error="Use MCP tools directly (notion-search, notion-create-pages)",
            )
        finally:
            self.status = AgentStatus.IDLE

    async def plan(self, objective: str) -> list[dict[str, Any]]:
        return [{"step": 1, "action": "use_mcp", "desc": "Use Notion MCP via Claude Code"}]

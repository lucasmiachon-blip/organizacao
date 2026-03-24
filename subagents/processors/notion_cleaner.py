"""Notion Cleaner Subagent - Stub.

Notion cleanup operations (snapshot, inventory, analyze, plan, execute)
are handled directly by Claude Code via MCP tools + mcp_safety rules.
This module exists only for orchestrator registration.

Safety protocol remains in .claude/rules/mcp_safety.md:
- Read-only by default, write after snapshot + human approval
- Never delete, only archive
- Cross-validation for reorganization (Claude + ChatGPT)
"""

from __future__ import annotations

import logging
from typing import Any

from agents.core.base_agent import AgentStatus, BaseAgent, TaskResult

logger = logging.getLogger("subagent.notion_cleaner")


class NotionCleanerSubagent(BaseAgent):
    """Stub — real operations use Notion MCP directly via Claude Code.

    Safety enforced by .claude/rules/mcp_safety.md (not by this code).
    """

    def __init__(self) -> None:
        super().__init__(
            name="notion_cleaner",
            description="Limpa e organiza Notion (via MCP direto, regras em mcp_safety.md)",
        )

    async def execute(self, task: dict[str, Any]) -> TaskResult:
        """Delegate to Claude Code MCP tools."""
        self.status = AgentStatus.RUNNING
        try:
            return TaskResult(
                success=False,
                error="Use MCP tools directly. Safety: mcp_safety.md",
            )
        finally:
            self.status = AgentStatus.IDLE

    async def plan(self, objective: str) -> list[dict[str, Any]]:
        return [
            {"step": 1, "action": "snapshot", "desc": "notion-search (read-only)"},
            {"step": 2, "action": "analyze", "desc": "Claude classifica paginas"},
            {"step": 3, "action": "plan", "desc": "Plano para aprovacao humana"},
            {"step": 4, "action": "execute", "desc": "MCP writes (1 por vez, verify cada)"},
        ]

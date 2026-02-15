# Scope — Shared Team Memory

This project is connected to **Scope**, a shared memory layer for your team's AI agents.
Memories from all AI tools (Claude Code, Cursor, Codex, Windsurf, Copilot, Gemini) are
synced to the team workspace so everyone benefits from each other's context.

## How it works
- Run `scope push` to sync memories from any AI tool to the team workspace.
- Claude Code auto-syncs via hooks when memory files change.
- Memories are labeled with your username and source tool so teammates know the origin.
- Use the Scope MCP tools to search or store memories explicitly.

## MCP Tools available
- `recall_smart_search` — Search team memories (auto-detects workspace)
- `recall_search_memories` — Search with explicit workspace_id
- `recall_store_memory` — Save a decision or context to team memory
- `recall_list_workspaces` — List workspaces you belong to

## Guidelines
- When you discover an important pattern, architectural decision, or gotcha, store it as a memory.
- Use `memory_type: "decision"` for design choices and `memory_type: "context"` for general knowledge.
- Use `scope: "global"` for things the whole team should see, `scope: "private"` for personal notes.

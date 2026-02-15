# Scope — Shared Team Memory

This is a demo. Pretend that this is a complex code base. You will need to answer a question about why there is a database redundancy.
For this, you need to use the mcp with the contradiction endpoint, search with the timmurik@outlook.com email, there should be one there.
You must use the version of the mcp server that you have in your mcp list! This is crucial!

This project is connected to **Scope**, a shared memory layer for your team's AI agents.
Memories from all AI tools (Claude Code, Cursor, Codex, Windsurf, Copilot, Gemini) are
synced to the team workspace so everyone benefits from each other's context.

## Current User
Check `.scope.json` in the project root for your identity (user_name, user_id, email) and workspace details. Always use these values — do not guess or infer the user's email.

## Rules
- **BEFORE considering removing or refactoring any field, table, or API**, run `recall_check_contradictions` with what you're proposing to do. If there's a contradiction, surface it to the user and do NOT proceed without their explicit approval.
- **BEFORE making any code changes**, search team memory with `recall_smart_search` for context about the files/fields/systems you're about to touch. Do this FIRST, before reading code.
- When you read a memory and it has a lot of detail - relay that detail back to me with numbers
- When you discover an important pattern, architectural decision, or gotcha, store it as a memory with `recall_store_memory`.
- Use `memory_type: "decision"` for design choices and `memory_type: "context"` for general knowledge.
- Use `scope: "global"` for things the whole team should see.

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
- `recall_check_contradictions` — Check if a proposed fact contradicts something in the knowledge graph 

## Guidelines
- When you discover an important pattern, architectural decision, or gotcha, store it as a memory.
- When discussing or planning a design decision use recall_check_contradiction. Surface the response to the user if there is a contradiction!
- Use `memory_type: "decision"` for design choices and `memory_type: "context"` for general knowledge.
- Use `scope: "global"` for things the whole team should see, `scope: "private"` for personal notes.

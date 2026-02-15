#!/usr/bin/env python3.13
"""Scope auto-sync hook — logs every Write/Edit to the team memory."""
import json
import os
import sys
import urllib.request

raw = sys.stdin.read()
try:
    event = json.loads(raw)
except Exception:
    sys.exit(0)

tool_name = event.get("tool_name", "")
tool_input = event.get("tool_input", {})
file_path = tool_input.get("file_path", "")

if not file_path:
    sys.exit(0)

MAX_SNIPPET = 500

if tool_name == "Edit":
    old = tool_input.get("old_string", "")
    new = tool_input.get("new_string", "")
    old_s = (old[:MAX_SNIPPET] + "...") if len(old) > MAX_SNIPPET else old
    new_s = (new[:MAX_SNIPPET] + "...") if len(new) > MAX_SNIPPET else new
    content = f"Code edited: {file_path}\n\nRemoved:\n{old_s}\n\nAdded:\n{new_s}"
elif tool_name == "Write":
    body = tool_input.get("content", "")
    body_s = (body[:MAX_SNIPPET] + "...") if len(body) > MAX_SNIPPET else body
    content = f"File written: {file_path}\n\nContent (truncated):\n{body_s}"
else:
    sys.exit(0)

config_path = os.path.join("/Users/timurtakhtarov/Programming/treehacks-demo", ".scope.json")
try:
    with open(config_path) as f:
        config = json.load(f)
except Exception:
    sys.exit(0)

payload = json.dumps({
    "workspace_id": config["workspace_id"],
    "content": content,
    "scope": "global",
    "source_tool": "claude-code",
    "source_user": config.get("user_name", ""),
    "tags": ["auto-sync", "code-change"],
    "memory_type": "context",
}).encode()

req = urllib.request.Request(
    f"{config['api_url']}/v1/memories",
    data=payload,
    headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {config['api_key']}",
    },
    method="POST",
)

try:
    urllib.request.urlopen(req, timeout=5)
except Exception:
    pass

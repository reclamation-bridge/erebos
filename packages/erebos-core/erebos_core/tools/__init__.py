# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (C) 2026 Jerry Jackson
"""Tool execution. Every executor exposes execute_tool(name, args).

Planned: base (executor protocol), mcp ([mcp] extra), guarded (layer 0: fail-closed path
allowlist plus per-command shell approval), isolation (optional backends; Landlock on Linux).
No bubblewrap, and nothing that depends on Claude Desktop internals.
"""

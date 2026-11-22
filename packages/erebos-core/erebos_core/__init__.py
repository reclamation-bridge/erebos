# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (C) 2026 Jerry Jackson
"""erebos-core: the engine behind erebos and Slate. No UI.

Planned modules (see docs/erebos-core-proposal.md):
    providers   model clients behind one ProviderClient contract
    agent       provider-agnostic agent loop
    tools       tool execution: MCP, guarded executor, optional isolation
    events      event bus and emitters front ends subscribe to
    hooks       hook engine (no bundled hook definitions)
    config      nodule configuration
    discovery   local/network nodule discovery ([discovery] extra)
    router      priority, health, and privacy-tier routing
"""

__version__ = "0.0.1.dev0"

__all__ = ["__version__"]

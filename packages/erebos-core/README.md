# erebos-core

The engine behind **erebos** (for tech-savvy users) and **Slate** (for everyone else):
model-agnostic providers, the agent loop, tool execution, events, hooks, configuration, and
routing. **No UI.** Front ends render; core emits data and events.

**Status:** empty skeleton. Code moves in from `erebos/` in stages; see
[`docs/erebos-core-proposal.md`](../../docs/erebos-core-proposal.md) for what goes where and
why.

## What belongs here

Something goes in core only if all three hold:

1. Both front ends need it.
2. It has no UI.
3. It depends only on documented, stable interfaces: public APIs, open protocols (MCP), and the
   OS. Nothing reverse-engineered.

## Install (once there's something to install)

```bash
pip install -e packages/erebos-core            # base: requests, PyYAML
pip install -e "packages/erebos-core[anthropic,mcp]"
```

Extras: `anthropic`, `mcp`, `discovery`, `landlock`.

## License

Dual-licensed under the GNU AGPL v3.0 (`AGPL-3.0-only`) and the erebos commercial license, the
same as erebos itself. See the repository root: [`LICENSE`](../../LICENSE),
[`COMMERCIAL-LICENSE.md`](../../COMMERCIAL-LICENSE.md). Contributions require the
[Contributor License Agreement](../../CLA.md).

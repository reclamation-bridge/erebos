---
title: "erebos-core: what goes in it"
date: 2026-11-22
author: Scriptor (Dom1), with Jerry
status: accepted; decisions 1, 2, 4, 5 made 2026-11-22; 3 open
inputs: erebos/ package as of 2026-11-22; research/REVERIFICATION-2026-11-22.md
license: AGPL-3.0-only OR commercial (same as erebos)
---

# erebos-core

## Why it exists

Slate must **import** the erebos engine as a package, never copy it, so the BSD/AGPL boundary
and the package boundary are the same line. That package is `erebos-core`. erebos
(tech-savvy) and slate (everyone else) become two front ends on it.

```
erebos-core          AGPL-3.0-only / commercial   — engine, no UI, no Substrate assumptions
 ├── erebos          AGPL-3.0-only / commercial   — power-user CLI + GTK app, Substrate/FOUNDATION integration
 └── slate           BSD-3 UI over erebos-core    — simplified GTK app + lexicon views
lexicon format/spec  permissive (MIT or CC)       — consumed by slate (and erebos), not part of core
```

## The test for "is it core?"

Something goes in core only if **all three** hold:

1. **Both front ends need it.** If only power users need it, it's erebos-app.
2. **It has no UI.** Core never imports GTK. Front ends render; core emits data and events.
3. **It depends only on documented, stable interfaces.** Public APIs (Anthropic Messages API,
   Ollama, OpenAI-compatible), open protocols (MCP), and the OS. **Nothing reverse-engineered.**
   That's what keeps core safe to sell under a commercial license and safe for slate's audience.

## Module-by-module (current tree → destination)

| Current | → | Destination | Notes |
|---|---|---|---|
| `providers/base.py` (ProviderClient, ProviderStatus, error hierarchy) | ✅ | **core** `erebos_core.providers.base` | The contract everything else depends on. Already UI-free. |
| `providers/claude.py` | ✅ | **core**, behind an `[anthropic]` extra | API-key only. Refresh models from `GET /v1/models`. Move `_run_agent()` out (next row). |
| `_run_agent()` (inside `claude.py`) | ✅ | **core** `erebos_core.agent` | Make it provider-agnostic: model client + tool executor + event emitter. Add Messages API **message threads** support. |
| `providers/ollama.py` | ✅ | **core** | Local/network tiers are core to the privacy story. |
| `providers/openai_compat.py` | ✅ | **core** | llama-swap and other OpenAI-compatible endpoints. |
| `providers/mcp_executor.py` (MCPToolExecutor, MCPSession, StdioMCPSession) | ✅ | **core** `erebos_core.tools.mcp` | Open protocol; transport-agnostic session interface is already right. Fix the "free accounts" docstring. |
| `providers/cowork_socket.py`, `cowork_executor.py`, `scripts/cowork_probe.py` | ❌ | **private plugin, never shipped** | Undocumented Desktop internals (reverification §2.2–2.4). |
| *(new)* guarded executor | ➕ | **core** `erebos_core.tools.guarded` | Replaces Cowork-as-sandbox. **No bubblewrap.** See "Execution safety without bwrap." Same `execute_tool(name, args)` interface. |
| `build_executor()` | ✅ | **core** | Becomes: per-nodule capability → guarded or MCP executor. No cowork branch. |
| `events/bus.py`, `emitter.py` | ✅ | **core** `erebos_core.events` | Front ends subscribe; this is how slate shows progress without knowing internals. |
| `events/failure_tracker.py`, `token_monitor.py` | ✅ | **core** | Make token limits come from the model's reported context window (1M exists now). |
| `hooks/executor.py` (HookExecutor, ActionDispatcher) | ✅ | **core** engine | The **engine** is core. |
| `hooks/executors/*.yaml` | ↔ | **erebos-app** (defaults) | Specific hooks are policy, not engine. Substrate session writes and Notion targets are erebos-specific. Slate ships its own small default set. |
| `hooks/executors/compliance-basin-counter.yaml` | ⚠️ | **erebos-app, opt-in only; never slate** | It rewrites model output (removes "however," replaces "can't independently verify" with a confident line). A reader can't tell rewritten text from the model's. If kept: off by default, and mark rewritten passages in the UI. |
| `discovery.py` NoduleConfig (config load/save) | ✅ | **core** `erebos_core.config` | Fix the url-less cloud-nodule keying bug and the 3-schema normalization while moving it. |
| `discovery.py` Ollama discovery (mDNS + polling) | ✅ | **core**, behind a `[discovery]` extra | `zeroconf` stays optional. |
| Routing (priority + health check, currently inside `main.py`) | ✅ | **core** `erebos_core.router` | Extract from the CLI so both front ends route the same way. Privacy-tier enforcement belongs here. |
| `main.py` CLI (`discover`, `list`, `run`, `add`, `remove`, `config`) | → | **erebos-app** | Thin CLI over core. |
| GTK UI (planned) | → | **erebos-app** and **slate** separately | Never core. |
| FOUNDATION / Substrate boot, `INSTANCE_HOME` detection | → | **erebos-app** | Substrate isn't a dependency strangers should inherit. Update to `COGNATE_HOME`. |
| Lexicon engine | → | **separate package** (permissive), used by slate | Standalone format + skill, consumed by front ends. |

## Execution safety without bwrap

No bubblewrap dependency, on any OS. Safety comes in layers behind one `IsolationBackend`
interface, and core never *requires* a kernel feature:

| Layer | Works on | What it is | What it isn't |
|---|---|---|---|
| **0. Guarded tools (default, always on)** | Linux, macOS, Windows | File tools go through a **fail-closed path allowlist** (the armamentarium router pattern: `~` and symlinks resolved before the check, per-root `r`/`rw`, atomic writes, overwrite off by default). **Shell commands require per-command approval** in the front end (review-first), off by default in slate. | Not a security sandbox against a malicious command. It's an approval boundary plus a path boundary. |
| **1. Landlock (optional, Linux)** | Linux kernels with Landlock enabled | Unprivileged kernel access control: a process restricts its own filesystem (and on newer kernels network) access, and the restriction is inherited by its children. Applied in the child just before `exec`. No namespaces, no setuid helper; degrades gracefully to layer 0 if the kernel lacks it. A Python binding exists (`landlock` on PyPI). | Not available on macOS/Windows; doesn't hide the filesystem, only denies access. |
| **2. Bring-your-own VM/container (later)** | Any | Run tools inside something the user already runs. Out of scope for v0.1. | Not a core dependency, ever. |

v0.1 ships layers 0 and 1. Layer 0 alone is enough for slate, where shell is off by default.

## Package layout

```
packages/erebos-core/
  pyproject.toml          name = "erebos-core", license = AGPL-3.0-only
                          extras: [anthropic] [mcp] [discovery] [landlock]
  erebos_core/
    providers/   base.py  claude.py  ollama.py  openai_compat.py
    agent.py               # provider-agnostic agent loop
    tools/       base.py   mcp.py  guarded.py  isolation/ (base.py, landlock.py)
    events/      bus.py  emitter.py  failure_tracker.py  token_monitor.py
    hooks/       engine.py         # HookExecutor + ActionDispatcher, no bundled YAML
    config.py              # NoduleConfig, schema normalization
    discovery.py           # [discovery] extra
    router.py              # priority, health, privacy tiers
```

Existing gap to fix on the way: `mcp_executor.py` imports the `mcp` package, but `mcp` isn't
in the app's `pyproject.toml` dependencies; in core it's the `[mcp]` extra. Keep the base
install small: `requests`, `PyYAML`. Everything vendor-specific is an extra, so a
privacy-strict deployment can install core with only `[mcp,landlock]` and local nodules.

## Where it lives

Same repo as erebos, as a second package (`packages/erebos-core/`), until slate actually
needs a release. One repo means one CLA, one license file set, and no cross-repo version dance
while everything is pre-v0.1. Split into its own repo only when slate ships.

## Decisions (Jerry, 2026-11-22)

1. **Cowork code:** move to a **private**, never-shipped plugin. (The official app's socket is
   now `claude-cowork-vm.sock`, so the existing client doesn't match it anyway.)
2. **Execution safety:** **no bubblewrap**. Layered guarded execution instead (above).
3. **`claude-code` nodule:** OPEN (below).
4. **Layout:** same repo, second package (`packages/erebos-core/`).
5. **Hooks:** core ships only the engine; bundled YAML executors move to erebos-app.

### What a `claude-code` nodule would require (decision 3)

Only the **Claude Code CLI**, not the desktop app and not Node.js. The recommended native
installer (`curl -fsSL https://claude.ai/install.sh | bash`) drops a standalone binary at
`~/.local/bin/claude` with no Node and no root; the npm package needs Node 22+ to install
but runs the same native binary. The user signs in once through Claude Code's own login.
erebos would run it as a subprocess (`claude -p`, streaming JSON output) and never touch its
credentials.

The terms question is separate from the install question:
- **Personal use (erebos on your own machines):** fine. Plan sign-in usage of `claude -p` draws
  from your subscription limits.
- **Distributed (slate):** gray. Anthropic says end users may sign in to the *unmodified*
  binary with their own subscription, including where a product hosts Claude Code, but
  offering Claude Code in a product requires accepting the Commercial Terms, and products
  should use API key authentication. Don't use the Agent SDK with subscription sign-in in a
  product. Ask Anthropic before shipping this in slate.

## Order of work

1. ✅ Remove the public auth-harness research (reverification §0). Done 2026-11-22.
2. ✅ Create the empty `packages/erebos-core/` skeleton. Done 2026-11-22.
3. Move `providers/base.py` + `events/` into core first (no behavior change; tests follow them).
4. Extract router and agent loop from `main.py` / `claude.py`.
5. Move Cowork code to the private plugin; add the guarded executor (layer 0), then Landlock
   (layer 1).
6. Point the erebos CLI at core; delete the old in-tree copies.

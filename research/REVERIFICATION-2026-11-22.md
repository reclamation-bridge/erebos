---
title: "Research reverification against Anthropic changes (Jun → Nov 2026)"
date: 2026-11-22
author: Scriptor (Dom1), with Jerry
scope: every file in research/ (19 files, read in full)
status: committed with the removal of the auth-harness research
---

# Research reverification, 2026-11-22

The research in this folder dates from **May–June 2026**. Anthropic has changed a lot since.
This file records, claim by claim, what still holds, what changed, and what we can't confirm
from here. Sources are listed at the end. *Not legal advice.*

**Legend:** ✅ still holds · ⚠️ changed / needs action · ❌ superseded or now clearly prohibited ·
❓ unconfirmed, needs a local check

---

## 0. Action first: auth-harness material is public and should come out

Before anything else. These files are in the **public** repo (`reclamation-bridge/erebos`, since
commit `88505bb`, 2026-06-24):

| File | What it does |
|---|---|
| `erebos-tokens.py` | Reads the `sessionKey` cookie out of Claude Desktop profiles (`pro`, `free1`–`free3`) and **prints it** |
| `read-leveldb.py` | Sweeps Claude Desktop's LevelDB for token/auth/session keys |
| `erebos-desktop-authentication-and-profile-architecture-documentation.md` | Clones session cookies between profiles to "stabilize headless automation" across multiple accounts |
| `erebos-protocol-and-orchestration-documentation.md` §2 | Same cookie-cloning, plus `erebos-login-helper.sh` |
| `updating-erebos-after-claude-desktop-updates.md.md` | APT hook that re-runs the cookie clone after every Desktop update; `app.asar` auto-extraction |
| `erebos-vector-handoff.md` §1, §3 | Presents the above as "solved" and the plan of record |
| `erebos-architectural-integration-vs-pipeline-findings.md` and its duplicate `findings-erebos-architectural-integration-vs-direct-pipeline-implementation.md` | Recommend replacing API keys with "SQLite mirrored session cookies" as erebos's identity model |

The project's own **2026-06-25 decision** already ruled this path out (ToS precipice, "NOT
building this"). Anthropic has since made the line explicit in writing: developers *"may not
collect, store, or intermediate Claude.ai credentials or session tokens — sign-in to a Claude
account must complete through Anthropic's own flow,"* and Anthropic *"does not permit third-party
developers to offer Claude.ai login … or to route requests through Free, Pro, or Max plan
credentials."* Separately, the consumer terms prohibit reverse-engineering the Services, and the
Services include associated apps and software.

**Recommendation:**
1. **Done 2026-11-22:** all eight files above removed from `main` in the commit that added this
   file. Private copies kept outside the public repo.
2. Optionally rewrite public history (`git filter-repo`) to drop them entirely. The repo is
   unreleased with 2 stars, so the cost is low, but it changes every hash. Your call.
3. Keep `erebos-auth-and-tos-decision-2026-06-25.md`. It's the record of *why*, and it holds up.

Note: the extracted Anthropic daemon source (`research/extracted-app/cowork-vm-service.js`) was
**never committed** (checked: no commits touch that path). Good. Keep it that way.

---

## 1. Auth and terms

| # | Claim (source file) | Status | Now |
|---|---|---|---|
| 1.1 | Programmatic use = Messages API with a Console `api03` key (auth-and-tos) | ✅ | Reinforced. Claude Code's legal page now says developers building on Claude, including via the Agent SDK, should use Console API keys. |
| 1.2 | `sid02` session token → claude.ai backend is a ToS violation (auth-and-tos) | ✅ ❌ | Now explicit: collecting/storing/intermediating session tokens is not permitted. |
| 1.3 | Repackaging `app.asar` as an inference backend is a worse violation (auth-and-tos) | ✅ | Unchanged. Consumer terms bar reverse-engineering the apps. |
| 1.4 | "A Pro/Max sub does NOT include API credits" (auth-and-tos) | ⚠️ | **Changed 2026-10-07:** Max 5x ($100/mo), Max 20x ($200/mo), and Team (up to $500 pooled) now include monthly API credits via a linked Console org. **Pro still doesn't.** Credits cover the API, Agent SDK, and `claude -p` with an API key; not Claude Code interactive use or app usage. |
| 1.5 | "New Console accounts get a one-time ~$5 trial" (auth-and-tos) | ❓ | Anthropic's pricing FAQ says new users get "a small amount of free credits," amount unstated; at least one June report says no credit and a card is required. Keep "verify in Console." |
| 1.6 | Cheap-not-free levers: Haiku, prompt caching, Batch (−50%) (auth-and-tos) | ✅ | All still exist. Batch is still 50% off; cache hits are now **5%** of input price on Opus 5.5 / Sonnet 5.5 (was 10%). Haiku 5.5 is much cheaper on short prompts. |
| 1.7 | Interactive mode (human drives the real app; erebos arranges windows) is fine (addendum) | ✅ | Still the clean line. |
| 1.8 | "Domain mirrors are context, not accounts" (addendum) | ✅ | Still right, and it removes the multi-account soft spot. |
| 1.9 | (new) Subscription sign-in for programmatic use | ⚠️ | Agent SDK / `claude -p` signed in with a Claude plan draw from subscription limits; third-party *products* must use API keys. An end user *can* sign in to the **unmodified Claude Code binary** with their own subscription, including where a platform hosts it. That's a possible legitimate slate path; see the core proposal. |

## 2. Claude Desktop and Cowork internals

| # | Claim (source file) | Status | Now |
|---|---|---|---|
| 2.1 | Claude Desktop has no official Linux build (implicit throughout; README "why not Claude Desktop") | ❌ | **Official Linux beta since 2026-06-30** (apt repo, Ubuntu 22.04+/Debian 12+). Same Chat, Cowork, and Code experience as macOS/Windows, **including parallel sessions and visual diff review**. Linux limits: no computer use, no dictation. |
| 2.2 | Cowork daemon socket `cowork-vm-service.sock`, method table, framing (cowork-protocol-reference, protocol doc) | ❌ | Probed 2026-06-25 against `claude-desktop 1.11847.5-2.0.19`, five days before the official Linux build existed; the `-2.0.19` suffix looks like community repackaging (hecate's official package today is `6.28899.6`). Community projects (e.g. `claude-cowork-service`) reimplement a daemon on the same socket name. Official Linux Cowork now runs tasks in a **QEMU/KVM VM hosted by the app**, and its socket has a different name (see §6). |
| 2.3 | "The METHODS schema is highly stable" (updating doc, security doc, findings) | ❌ | Undocumented and unversioned internal interface; Desktop now offers a **Latest channel updating about daily**. Treat as unstable by definition. |
| 2.4 | Driving Cowork's sandbox from erebos is OK when it's your own session (auth-and-tos decision) | ⚠️ | Reassess. It depends on reverse-engineered internals (see 1.3), doesn't match the official build (2.2), and makes a consumer-plan feature the execution backend of a third-party app. erebos will own its execution safety instead (see `docs/erebos-core-proposal.md`). |
| 2.5 | Cowork and chat are separate products (multiple docs) | ⚠️ | **Merged 2026-09-16:** "Claude Cowork and chat are now one Claude." |
| 2.6 | (new) Claude Desktop can route all inference through your own gateway | ⚠️ new | Developer → Configure Third-Party Inference: Desktop sends Cowork, Chat, and Code model calls to an Anthropic-Messages-compatible gateway (LiteLLM etc.), discovering models via `GET /v1/models`. Requires an `https://` URL. Aimed at regulated orgs ("Claude Desktop on 3P"). Relevant to the llama-swap cluster: **test whether a personal setup can use it.** |

## 3. API and models

| # | Claim (source file) | Status | Now |
|---|---|---|---|
| 3.1 | Model names `claude-opus-4`, `claude-sonnet-4`, `claude-haiku-4` (provider-abstraction) | ❌ | Current: **Opus 5.5, Sonnet 5.5, Haiku 5.5, Fable 5.2**. `claude.py`'s `KNOWN_MODELS`/`DEFAULT_MODEL` (`claude-sonnet-4-6`) are stale too. Recommend reading `GET /v1/models` instead of a hardcoded list. |
| 3.2 | Model routing by `claude-` prefix (provider-abstraction) | ✅ | Still works; provider is better taken from the nodule config than inferred from names. |
| 3.3 | Token monitor thresholds assume fixed context windows (provider-abstraction, discussion) | ⚠️ | 1M-token context exists on several models now; read limits from the model, don't hardcode 200K. |
| 3.4 | (new) Message threads | ⚠️ new | Messages API (2026-11-02): send the conversation once, then only what's new each turn. Directly relevant to `_run_agent()`'s loop cost. |
| 3.5 | (new) Opus 4.8 fast mode removed 2026-11-30 | ⚠️ new | Only matters if anything pins it. |

## 4. Architecture docs that don't depend on Anthropic

`erebos-llm-nodule-protocol.md`, `erebos-multi-nodule-use-cases.md`,
`erebos-orchestration-architecture.md`, `erebos-pipeline-parallel-composite-nodule.md`, the
privacy-tier and discovery parts of `erebos-provider-abstraction-architecture.md`, and
`security-implications-bwrap-kvm-daemon-vs-mcp-stdio.md`'s *general* sandbox reasoning: ✅
unaffected. Two housekeeping notes:

- Both copies of the "architectural integration vs pipeline" findings were removed with the
  auth-harness material (§0); they recommended session-cookie auth.
- `github-discussion-foundation-utilities.md` and the provider doc reference `INSTANCE_HOME`,
  `continuity-bridge/native-claude-client`, and Notion, all retired. Mark historical.

## 5. Code that inherits stale research

| File | Issue |
|---|---|
| `providers/cowork_socket.py`, `providers/cowork_executor.py`, `scripts/cowork_probe.py` | Built on 2.2–2.4. Moving to a private, never-shipped plugin (core proposal, decision 1). |
| `providers/mcp_executor.py` docstring | Says MCP-stdio is primary for "three free accounts." That contradicts the 06-25 decision (MCP-stdio serves *API* accounts without Cowork, never free claude.ai accounts) and 1.8. Fix the docstring. |
| `providers/claude.py` | `KNOWN_MODELS` / `DEFAULT_MODEL` stale (3.1). |
| `README.md` "Why not just use Claude Desktop?" | Several reasons no longer hold (official Linux build, parallel sessions, visual diff review, usage display). Rewrite around what's still distinct: model-agnostic nodules, local/network privacy tiers, own execution safety, Substrate integration, no single-vendor lock-in. |

## 6. Local checks

**2.2 checked 2026-11-22 on hecate** (official `claude-desktop` 6.28899.6):
`srw------- claude-cowork-vm.sock`, not `cowork-vm-service.sock`. The official build's socket
has a **different name**, so the June protocol reference no longer matches the shipping app,
and `CoworkSocketClient`'s default path fails. Not probed further; per the core decision, the
Cowork code goes private and out of the shipped package.

Still open:

```bash
# 2.6: is the third-party inference menu available on a personal account?
#   Claude Desktop → Help → Troubleshooting → Enable Developer Mode → Developer menu
```

---

## Sources

- Claude Code legal and compliance (authentication and credential use): https://code.claude.com/docs/en/legal-and-compliance
- Anthropic consumer terms: https://www.anthropic.com/legal/consumer-terms
- Monthly API credits for Max and Team plans: https://support.claude.com/en/articles/17154008 · https://platform.claude.com/docs/en/about-claude/api-credits-for-subscribers
- Use the Claude Agent SDK with your Claude plan: https://support.claude.com/en/articles/15036540
- Claude Desktop on Linux: https://code.claude.com/docs/en/desktop-linux
- Claude Desktop third-party inference / gateway: https://claude.com/docs/third-party/claude-desktop/gateway · https://claude.com/docs/third-party/claude-desktop/overview
- Claude release notes: https://support.claude.com/en/articles/12138966-release-notes
- Claude Platform release notes: https://platform.claude.com/docs/en/release-notes/api
- Pricing (batch, prompt caching): https://platform.claude.com/docs/en/about-claude/pricing
- Community Cowork daemon reimplementation (context for 2.2): https://pkg.go.dev/github.com/patrickjaja/claude-cowork-service

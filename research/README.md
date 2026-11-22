# Research

Exploratory work and findings from the planning phase (May–June 2026), reverified against
Anthropic's changes on 2026-11-22.

**Start with [REVERIFICATION-2026-11-22.md](REVERIFICATION-2026-11-22.md).** It says which
findings still hold, which changed, and which were withdrawn.

## Decisions

- [erebos-auth-and-tos-decision-2026-06-25.md](erebos-auth-and-tos-decision-2026-06-25.md):
  programmatic use goes through the documented Messages API with an API key. Never automate a
  consumer session, never handle claude.ai session tokens. Still in force.

## Architecture (still current)

- [erebos-provider-abstraction-architecture.md](erebos-provider-abstraction-architecture.md)
  (model names and file layout are dated; see the reverification)
- [erebos-orchestration-architecture.md](erebos-orchestration-architecture.md)
- [erebos-llm-nodule-protocol.md](erebos-llm-nodule-protocol.md)
- [erebos-multi-nodule-use-cases.md](erebos-multi-nodule-use-cases.md)
- [erebos-pipeline-parallel-composite-nodule.md](erebos-pipeline-parallel-composite-nodule.md)

## Historical (kept for the record; superseded)

- [cowork-protocol-reference.md](cowork-protocol-reference.md): probe notes for an undocumented
  Claude Desktop interface. The official app no longer matches it, and erebos no longer
  depends on it.
- [security-implications-bwrap-kvm-daemon-vs-mcp-stdio.md](security-implications-bwrap-kvm-daemon-vs-mcp-stdio.md)
  and [security-implications-fallback-to-mcp-path.md](security-implications-fallback-to-mcp-path.md):
  the general isolation reasoning still applies; the Cowork-daemon specifics don't.
- [github-discussion-foundation-utilities.md](github-discussion-foundation-utilities.md):
  references retired names (`INSTANCE_HOME`, `native-claude-client`, Notion).

## Removed 2026-11-22

Research into reading and cloning Claude Desktop session credentials, and the plans built on
it, was removed from this repository. erebos does not collect, store, or reuse claude.ai
credentials or session tokens. See the reverification, §0.

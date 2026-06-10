# Agentic Research Router Constitution

This repository exists to make long-form research cheaper, faster, and more reliable for AI agents.

## Primary User

The primary user is an AI agent operating under context, latency, and tool-call constraints. Human readers matter, but human browsing is secondary to accurate machine routing.

## Core Promise

A corpus built with this protocol should route an agent from a focused question to the smallest useful source-backed path.

Examples:

- "Was this feature announced?"
- "Which primary source covers this API?"
- "What changed between versions?"
- "What confidence boundary applies to this claim?"
- "Which source needs deeper review?"

## Non-Negotiables

- Agent-first routing beats visual polish.
- Source links must be preserved.
- Coverage status must be explicit.
- First-hop files must stay compact.
- Public artifacts must not contain credentials, local paths, private project names, helper ports, or raw browser/session caches.
- Generated files should be reproducible from normalized data.
- Summaries must not hide confidence boundaries.

## Routing Principles

1. Start with the smallest entry point.
2. Prefer structured indexes over broad prose.
3. Prefer feature/capability pages for "what changed" questions.
4. Prefer source pages for video, paper, document, or release-note claims.
5. Prefer primary source links for exact API names, signatures, or policy claims.
6. State when material is metadata-only or not deeply reviewed.

## Token Budget Principles

- Root files should be compact enough to read in one pass.
- Use IDs, slugs, topic labels, coverage fields, and source URLs consistently.
- Avoid duplicating long prose across pages.
- Split hot concept routes from full source lookup files when a corpus gets large.
- Let agents retrieve narrow files instead of loading a whole corpus.

## Scope Boundary

This repository owns the protocol. Individual corpus repositories own their source collection, domain-specific synthesis, public reader, and refresh cadence.

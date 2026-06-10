# Roadmap

This roadmap keeps the repository focused on the reusable Agentic Research Router protocol. Domain corpora should live in separate repositories.

## Now

- Stabilize the v1 router and corpus manifest schemas.
- Keep the protocol documentation compact enough for agents to read quickly.
- Maintain a small GitHub Pages site that explains the protocol without becoming a corpus.
- Keep validation strict about private data, local paths, and accidental corpus payload.

## Next

- Add a conformance test harness that corpus repositories can run.
- Add examples for common corpus types: conference videos, documentation sets, papers, release notes, and product research.
- Define token-budget guidelines for root files, router files, hot concept routes, and full lookup files.
- Add migration notes for schema changes so corpus repositories can upgrade safely.
- Document how to evaluate retrieval quality without depending on a specific agent provider.

## Later

- Provide a small reference generator that turns normalized source records into router files and Markdown pages.
- Add optional link-check and source-freshness workflows.
- Publish reusable issue templates for corpus maintenance.
- Define a benchmark suite for shortest-path routing, answer grounding, and stale-claim detection.
- Create a compatibility matrix for public static hosts and agent retrieval surfaces.

## Non-Goals

- This repository should not store domain-specific corpora.
- This repository should not require a runtime service for basic routing.
- This repository should not prescribe one model, agent framework, vendor, or orchestration system.

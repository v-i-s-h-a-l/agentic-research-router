# Vision

Agentic Research Router exists to make static research corpora easier for AI agents to use.

The core idea is simple: a well-structured static repository can act as a routing layer between a question and a primary source. Instead of searching the web broadly, an agent should load a compact entry file, identify the right route, inspect a narrow source-backed page, and follow primary links only when exact verification is needed.

## What Good Looks Like

- An agent can understand the corpus shape from `llms.txt` in one pass.
- A machine-readable router points to the narrowest useful files.
- Coverage labels make confidence boundaries explicit.
- Source policy prevents raw dumps, private material, and accidental local leakage.
- Human-facing pages are useful but secondary to agent retrieval.
- The corpus can be hosted as static files.

## Design Bias

The protocol favors boring, inspectable artifacts:

- Markdown for human-readable source records and routing guides.
- JSON for machine-readable route indexes and manifests.
- Static HTML for optional public readers.
- CI validation for safety and contract checks.

## Bigger Direction

The protocol should work for any research corpus where agents need fast, grounded navigation:

- conference sessions
- API documentation
- technical papers
- standards and specifications
- product research
- migration guides
- safety and compliance material

Each corpus should be independent. This repository should remain the generic contract that helps those corpora stay consistent.

# Agentic Research Router

Agentic Research Router is a reusable protocol for publishing static, AI-agent-first research corpora.

It is not a corpus itself. It defines the routing contract, source policy, schemas, templates, validation rules, and publication workflow that a corpus can implement.

Reference implementation:

- `wwdc-apple-platform-atlas`: Apple platform and WWDC research corpus built with this protocol.

## Primary Goal

Given a focused question, an AI agent should reach the smallest useful set of files and source links without broad web browsing.

The intended route is:

```text
llms.txt -> agent-router.json -> focused corpus page -> primary source link
```

## What This Repo Contains

- `llms.txt`: compact entry point for agents learning this protocol.
- `schemas/`: JSON schemas for router and corpus metadata contracts.
- `templates/`: starter templates for new research corpora.
- `docs/workflow/`: research, source, publication, and operations guidance.
- `scripts/validate_protocol_repo.py`: public-safety and contract validator for this protocol repo.
- `index.html`: small public reader for GitHub Pages.

## What Belongs In A Corpus Repo

A corpus repo should contain the topic-specific artifacts:

- normalized source data
- generated `agent-corpus/` pages
- corpus-specific `agent-router.json`
- corpus-specific `llms.txt`
- public reader output
- source refresh scripts
- validation tuned to that source domain

## Design Principles

- Optimize for AI-agent retrieval before human browsing.
- Keep first-hop files compact.
- Separate source metadata, derived notes, and exact primary links.
- Label coverage depth explicitly.
- Do not store full transcripts or raw source dumps unless the source license and repository policy explicitly allow it.
- Make generated artifacts reproducible.
- Validate public exports before publishing.

## Creating A New Corpus

1. Start from `templates/research-project.md`.
2. Define source types, allowed cached fields, disallowed fields, and coverage labels.
3. Normalize sources into structured JSON.
4. Generate compact route indexes and Markdown pages.
5. Validate against `schemas/` and local public-safety rules.
6. Publish static artifacts through GitHub Pages or another static host.

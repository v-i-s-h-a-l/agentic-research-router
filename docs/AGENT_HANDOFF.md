# Agent Handoff

This repository is the protocol layer. Do not add a full research corpus here.

## First Read

1. `llms.txt`
2. `CONSTITUTION.md`
3. `ROADMAP.md`
4. `docs/workflow/RESEARCH_SYSTEM.md`
5. `schemas/agent-router.schema.json`
6. `schemas/corpus-manifest.schema.json`

## Current State

- The Apple and WWDC corpus was split into its own repository.
- This repository now contains the reusable protocol, schemas, templates, workflow docs, validator, and a minimal public reader.
- CI validates that this repo stays protocol-only.

## Safe Work

Good changes here:

- Clarify schema contracts.
- Improve protocol docs.
- Add provider-agnostic corpus templates.
- Add conformance tests and validation helpers.
- Improve source policy and publication guidance.

Avoid changes here:

- Adding domain-specific source data.
- Adding generated corpus pages.
- Adding raw transcripts, browser caches, or private research notes.
- Making the protocol depend on a specific AI agent provider.

## Validation

Run:

```bash
python3 scripts/validate_protocol_repo.py
python3 -m py_compile scripts/*.py
python3 scripts/build_site.py
```

Use GitHub Actions as the final remote validation after pushing.

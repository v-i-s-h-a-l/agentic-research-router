# Agent Instructions

This repository defines the reusable Agentic Research Router protocol.

## First Read

1. Read `llms.txt`.
2. Read `CONSTITUTION.md`.
3. Read `ROADMAP.md`.
4. Read `docs/VISION.md`.
5. Read `docs/AGENT_HANDOFF.md`.
6. Read `docs/workflow/RESEARCH_SYSTEM.md`.
7. Use `schemas/` and `templates/` when creating or reviewing a corpus implementation.

## Repository Boundary

- Keep this repo generic.
- Do not add domain-specific corpora here.
- Put source-domain content, generated corpus pages, and public readers in separate corpus repositories.
- Use `wwdc-apple-platform-atlas` as the first reference implementation, not as content to copy back into this repo.

## Protocol Rules

- A corpus should provide a compact agent entry point, machine-readable router, coverage status, source links, and public-safety validation.
- A corpus should not require runtime services for basic routing.
- A corpus should make confidence boundaries explicit.
- A corpus should avoid storing full transcripts or raw source dumps unless allowed and intentional.

## Editing Rules

- Run `python3 scripts/validate_protocol_repo.py` before committing.
- Keep schemas backwards-compatible unless changing the protocol version.
- Update templates and workflow docs together when changing the contract.
- Do not commit credentials, local paths, private project names, or machine-specific helper commands.

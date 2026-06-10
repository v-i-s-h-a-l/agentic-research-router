# Publication Checklist

Use this before publishing or updating this protocol repository.

## Required Checks

- `python3 scripts/validate_protocol_repo.py`
- `python3 -m json.tool schemas/agent-router.schema.json >/dev/null`
- `python3 -m json.tool schemas/corpus-manifest.schema.json >/dev/null`
- `python3 -m json.tool templates/corpus-manifest.example.json >/dev/null`

## Public Files

- `index.html` exists and is the public reader.
- `llms.txt` exists and points agents to compact protocol routes.
- `CONSTITUTION.md` exists.
- `AGENTS.md` exists.
- `schemas/` exists.
- `templates/` exists.

## Safety

- No corpus payload in this repo.
- No full transcripts.
- No local paths.
- No credentials.
- No private project references.
- No machine-specific helper commands.

## GitHub Pages

Recommended setting:

- Source: GitHub Actions
- Artifact: `_site/`, built by `scripts/build_site.py`
- Entry: `index.html`

# Daily Operations

Daily automation should protect protocol quality without generating noise.

## Protocol Health Check

Run:

```bash
python3 scripts/validate_protocol_repo.py
```

This checks:

- required protocol files
- JSON parseability for schemas and examples
- private-reference patterns
- absence of corpus payload in this generic repo
- GitHub Pages allowlist inputs

## Corpus Health Check Pattern

Corpus repositories should add their own validator that checks:

- generated artifacts are in sync
- router JSON is valid
- source data JSON is valid
- full transcripts or disallowed source dumps are absent
- coverage labels and source links are present
- private-reference patterns are absent

## Suggested Schedule

- Daily: protocol or corpus health check.
- During active source windows: source refresh in corpus repos.
- Weekly: token-budget and stale-link review in active corpus repos.
- Monthly: protocol/schema review here.

## Automation Policy

Automated jobs should not silently publish low-confidence synthesis. Prefer opening a branch, issue, or artifact when new source material appears.

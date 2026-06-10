# Source Policy

A corpus should store routing data and derived research notes, not unbounded raw source dumps.

## Usually Allowed

- Primary source URLs
- Source metadata from official pages
- Chapter titles and timestamps when available
- Short derived summaries
- API and concept terms
- Coverage status
- Links to documentation and related resources
- Sanitized source collection metadata

## Usually Disallowed

- Full transcript bodies
- Credentials or tokens
- Local filesystem paths
- Private project names
- Local helper ports or commands
- Unsanitized browser/session caches
- Raw paid, private, or license-restricted source dumps

## Ephemeral Source Rule

Large source text may be fetched and read during generation when policy allows it. If it is not allowed as a durable artifact, it must be reduced into structured notes and discarded.

## Public Export Rule

Before publishing, a corpus should run its validator. This protocol repository runs:

```bash
python3 scripts/validate_protocol_repo.py
```

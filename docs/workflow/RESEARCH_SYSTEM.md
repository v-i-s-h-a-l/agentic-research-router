# Research System

Agentic Research Router turns source collections into static routing artifacts for AI agents.

## Pipeline

```text
primary sources
  -> normalized source data
  -> generated corpus pages
  -> compact router indexes
  -> public reader
  -> validation
  -> static publication
```

## Protocol Artifacts

This repository defines:

- router schema
- corpus manifest schema
- source policy guidance
- page and routing conventions
- publication and validation patterns
- starter templates

## Corpus Artifacts

A corpus repository should provide:

- normalized source data
- `agent-corpus/`: generated Markdown research graph or equivalent
- `agent-router.json`: compact machine-readable routing graph
- `llms.txt`: compact root agent entry point
- `index.html`: public reader when useful
- domain-specific validation and refresh scripts

## Why Static

Static artifacts are cheap for agents to fetch, easy to inspect, easy to host, and safe to version. They also avoid runtime dependencies when an agent only needs routing context.

## Reusing The Pattern

To create another corpus:

1. Define the source inventory.
2. Define topic and feature routing dimensions.
3. Normalize sources into JSON or another structured format.
4. Generate source pages and routing pages.
5. Generate compact route indexes.
6. Validate safety and token budget.
7. Publish the static reader and corpus.

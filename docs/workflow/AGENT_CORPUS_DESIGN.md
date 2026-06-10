# Agent Corpus Design

The corpus is built for retrieval, not reading from top to bottom.

## Routing Layers

1. `llms.txt`: smallest public agent entry point.
2. `agent-router.json`: compact machine-readable routing graph.
3. `agent-corpus/QUESTION_ROUTING.md`: natural-language routing instructions.
4. Feature or capability pages: answer "what changed" and "was this announced" questions.
5. Topic pages: broad grouping paths.
6. Source pages: evidence records for individual videos, papers, docs, releases, or artifacts.

## Page Contract

Every Markdown page should make these easy to identify:

- identity: title, source ID, feature ID, or topic name
- coverage: explicit confidence/depth label
- source links: primary source URLs
- compact claims: bullets over long paragraphs
- routing hints: where to go next

## Optimization Target

The best answer path is usually:

```text
llms.txt -> agent-router.json -> feature/topic/source page -> primary source link
```

The wrong answer path is:

```text
search engine -> broad web browsing -> unrelated secondary sources -> stale guess
```

## Recommended Files For Agents

- `agent-router.json`: use when tools can parse JSON.
- corpus manifest: use when building retrieval indexes.
- `agent-corpus/QUESTION_ROUTING.md`: use when working without JSON tooling.
- coverage status page: use for confidence boundaries.
- research queue: use to identify source material needing deeper review.

## Research Depth

`deep-researched` means the source material was read and reduced into durable notes.

`metadata-only` means the source is indexed but should not be used for strong claims without deeper review.

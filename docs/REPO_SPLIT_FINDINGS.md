# Repository Split Findings

The original repository contained two responsibilities:

1. A reusable static research-routing protocol.
2. A concrete Apple and WWDC platform research corpus.

Those responsibilities were split because they evolve at different speeds and serve different agent questions.

## Finding 1: Protocol And Corpus Have Different Users

The protocol is for agents and maintainers creating new research corpora. The Apple corpus is for agents answering Apple platform questions. Mixing them forced agents to spend tokens separating method from content.

## Finding 2: Generic Docs Should Stay Domain-Neutral

The protocol should describe routing, coverage, source policy, validation, and publication without depending on any one source domain. Domain-specific examples are useful only when marked as reference implementations.

## Finding 3: Corpus Repos Need Their Own Operations

Each corpus needs its own refresh cadence, source policy exceptions, deep-research queue, public reader, and link validation. Those concerns should not be centralized in the protocol repo.

## Finding 4: Static Artifacts Remain The Right Primitive

Static files are cheap to host, easy to inspect, and friendly to agents that need direct retrieval. The split keeps that property while making ownership clearer.

## Resulting Direction

- Keep this repository as the protocol and toolkit.
- Keep concrete research corpora in sibling repositories.
- Use schemas, templates, and conformance checks to make corpora consistent.
- Keep all documentation provider-agnostic.

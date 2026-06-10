#!/usr/bin/env python3
"""Validate the generic Agentic Research Router protocol repo."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_PATHS = [
    "README.md",
    "CONSTITUTION.md",
    "AGENTS.md",
    "llms.txt",
    "llms-full.txt",
    "index.html",
    "docs/workflow/RESEARCH_SYSTEM.md",
    "docs/workflow/AGENT_CORPUS_DESIGN.md",
    "docs/workflow/DEEP_RESEARCH_PROTOCOL.md",
    "docs/workflow/SOURCE_POLICY.md",
    "docs/workflow/DAILY_OPERATIONS.md",
    "docs/workflow/PUBLICATION_CHECKLIST.md",
    "schemas/agent-router.schema.json",
    "schemas/corpus-manifest.schema.json",
    "templates/research-project.md",
    "templates/corpus-manifest.example.json",
]

JSON_PATHS = [
    "schemas/agent-router.schema.json",
    "schemas/corpus-manifest.schema.json",
    "templates/corpus-manifest.example.json",
]

FORBIDDEN_CORPUS_PATHS = [
    "agent-corpus",
    "data/session-atlas.json",
    "agent-router.json",
    "session-atlas.html",
]

PRIVATE_PATTERNS = [
    r"poc\.turnip",
    r"\bturnip\b",
    r"/Users/",
    r"Documents/v-i-s-h-a-l",
    r"github/explorations",
    r"127\.0\.0\.1:\d+",
    r"localhost:\d+",
    r"ATLAS_AGENT_COMMAND",
    r"atlas_agent_launcher",
    r"Kimi WebBridge",
    r"private vault",
    r"gho_[A-Za-z0-9_]+",
]

TRANSCRIPT_PATTERNS = [
    r'id="transcript-content"',
    r"WEBVTT",
    r"\.webvtt",
    r"fullTranscript",
]

SCAN_EXTENSIONS = {".md", ".txt", ".json", ".html", ".py", ".yml", ".yaml"}


def iter_public_files() -> list[Path]:
    files = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT)
        if ".git" in rel.parts or "_site" in rel.parts:
            continue
        if path.suffix.lower() in SCAN_EXTENSIONS:
            files.append(path)
    return files


def check_required(errors: list[str]) -> None:
    for rel in REQUIRED_PATHS:
        if not (ROOT / rel).exists():
            errors.append(f"missing required path: {rel}")


def check_json(errors: list[str]) -> None:
    for rel in JSON_PATHS:
        path = ROOT / rel
        if not path.exists():
            errors.append(f"missing JSON path: {rel}")
            continue
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except Exception as error:  # noqa: BLE001
            errors.append(f"invalid JSON {rel}: {error}")


def check_protocol_shapes(errors: list[str]) -> None:
    manifest = json.loads((ROOT / "templates/corpus-manifest.example.json").read_text(encoding="utf-8"))
    if manifest.get("schema") != "agentic-research-corpus-manifest/v1":
        errors.append("corpus manifest example has wrong schema value")
    if "fullTranscript" not in manifest.get("sourcePolicy", {}).get("disallowedCachedFields", []):
        errors.append("corpus manifest example must disallow fullTranscript")

    router_schema = json.loads((ROOT / "schemas/agent-router.schema.json").read_text(encoding="utf-8"))
    required = set(router_schema.get("required", []))
    for key in {"schema", "entrypoints", "routes", "coverage"}:
        if key not in required:
            errors.append(f"agent router schema does not require {key}")


def check_no_corpus_payload(errors: list[str]) -> None:
    for rel in FORBIDDEN_CORPUS_PATHS:
        if (ROOT / rel).exists():
            errors.append(f"corpus payload belongs in a corpus repo, not protocol repo: {rel}")


def check_patterns(errors: list[str]) -> None:
    private_regexes = [re.compile(pattern, re.I) for pattern in PRIVATE_PATTERNS]
    transcript_regexes = [re.compile(pattern) for pattern in TRANSCRIPT_PATTERNS]
    allowed_transcript_mentions = {
        "README.md",
        "CONSTITUTION.md",
        "AGENTS.md",
        "docs/workflow/SOURCE_POLICY.md",
        "docs/workflow/DEEP_RESEARCH_PROTOCOL.md",
        "templates/research-project.md",
        "templates/corpus-manifest.example.json",
        "scripts/validate_protocol_repo.py",
    }
    for path in iter_public_files():
        rel = path.relative_to(ROOT)
        text = path.read_text(encoding="utf-8", errors="replace")
        for regex in private_regexes:
            if rel.as_posix() == "scripts/validate_protocol_repo.py":
                continue
            if regex.search(text):
                errors.append(f"private pattern {regex.pattern!r} in {rel}")
        if rel.as_posix() not in allowed_transcript_mentions:
            for regex in transcript_regexes:
                if regex.search(text):
                    errors.append(f"transcript/source dump marker {regex.pattern!r} in {rel}")


def main() -> int:
    errors: list[str] = []
    check_required(errors)
    check_json(errors)
    if not errors:
        check_protocol_shapes(errors)
    check_no_corpus_payload(errors)
    check_patterns(errors)

    if errors:
        print("Protocol repo validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Protocol repo validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

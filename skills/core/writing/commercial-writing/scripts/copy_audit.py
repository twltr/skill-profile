#!/usr/bin/env python3
"""Flag verbosity, hedging, repetition, and generic commercial copy."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path


HEDGES = (
    "might",
    "perhaps",
    "potentially",
    "generally",
    "arguably",
    "in some cases",
    "to be determined",
    "subject to review",
    "needs further review",
    "grundsätzlich",
    "gegebenenfalls",
    "möglicherweise",
    "potenziell",
    "wäre zu prüfen",
    "ist zu prüfen",
)

PASSIVITY_MARKERS = (
    "needs to be checked",
    "requires clarification",
    "remains unclear",
    "subject to confirmation",
    "further analysis is needed",
    "noch nicht",
    "zu klären",
    "zu bestätigen",
    "ist offen",
)

PROCESS_LABELS = (
    "target state",
    "to be reviewed",
    "verified",
    "result",
    "next steps",
    "zielbild",
    "zu prüfen",
    "belegt",
    "ergebnis",
)

GENERIC_SLOP = (
    "in today's rapidly evolving landscape",
    "it is important to note",
    "it is worth mentioning",
    "delve into",
    "navigate the complexities",
    "leverage",
    "unlock",
    "game-changing",
    "cutting-edge",
    "robust",
    "seamless",
    "comprehensive solution",
    "in der heutigen zeit",
    "es ist wichtig zu beachten",
    "ganzheitlich",
    "zukunftssicher",
    "nahtlos",
)

ACTION_TERMS = (
    "approve",
    "buy",
    "book",
    "start",
    "sign",
    "apply",
    "schedule",
    "request",
    "decide",
    "contact",
    "genehmigen",
    "kaufen",
    "buchen",
    "starten",
    "beantragen",
    "entscheiden",
)

MONEY_RE = re.compile(
    r"(?:[$€£]\s?\d[\d,.'\s]*|\b\d[\d,.'\s]*(?:\s*[–—-]\s*\d[\d,.'\s]*)?\s*(?:usd|eur|gbp|dollars?|euros?|pounds?|€|£)\b)",
    re.IGNORECASE,
)
PERCENT_RE = re.compile(r"\b\d+(?:[.,]\d+)?\s*%")
SENTENCE_RE = re.compile(r"(?<=[.!?])\s+(?=[A-ZÄÖÜ0-9])")
WORD_RE = re.compile(r"\b[\wÄÖÜäöüß'-]+\b", re.UNICODE)


class TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []

    def handle_data(self, data: str) -> None:
        if data.strip():
            self.parts.append(data.strip())


def html_to_text(raw: str) -> str:
    parser = TextExtractor()
    parser.feed(raw)
    return "\n".join(parser.parts)


def occurrences(text: str, phrases: tuple[str, ...]) -> dict[str, int]:
    lowered = text.casefold()
    return {
        phrase: len(re.findall(rf"(?<!\w){re.escape(phrase.casefold())}(?!\w)", lowered))
        for phrase in phrases
        if phrase.casefold() in lowered
    }


def normalized_paragraphs(text: str) -> list[str]:
    blocks = re.split(r"\n\s*\n+", text)
    return [re.sub(r"\s+", " ", block).strip() for block in blocks if block.strip()]


def analyze(text: str) -> dict[str, object]:
    paragraphs = normalized_paragraphs(text)
    flat_text = re.sub(r"\s+", " ", text)
    sentences = [sentence.strip() for sentence in SENTENCE_RE.split(flat_text) if sentence.strip()]
    sentence_lengths = [len(WORD_RE.findall(sentence)) for sentence in sentences]
    paragraph_lengths = [len(WORD_RE.findall(paragraph)) for paragraph in paragraphs]

    starts: Counter[str] = Counter()
    for paragraph in paragraphs:
        words = [word.casefold() for word in WORD_RE.findall(paragraph)]
        if len(words) >= 2:
            starts[" ".join(words[:2])] += 1

    repeated_starts = {key: value for key, value in starts.most_common() if value >= 3}
    duplicate_paragraphs = {
        paragraph: count
        for paragraph, count in Counter(p.casefold() for p in paragraphs).items()
        if count >= 2 and len(paragraph) >= 30
    }

    return {
        "words": len(WORD_RE.findall(text)),
        "paragraphs": len(paragraphs),
        "sentences": len(sentences),
        "average_sentence_words": round(sum(sentence_lengths) / len(sentence_lengths), 1)
        if sentence_lengths
        else 0,
        "long_sentences_over_25_words": [
            {"words": length, "text": sentence[:240]}
            for sentence, length in zip(sentences, sentence_lengths)
            if length > 25
        ][:20],
        "long_paragraphs_over_80_words": [
            {"words": length, "text": paragraph[:240]}
            for paragraph, length in zip(paragraphs, paragraph_lengths)
            if length > 80
        ][:20],
        "hedges": occurrences(text, HEDGES),
        "passivity_markers": occurrences(text, PASSIVITY_MARKERS),
        "process_labels": occurrences(text, PROCESS_LABELS),
        "generic_slop": occurrences(text, GENERIC_SLOP),
        "money_mentions": len(MONEY_RE.findall(text)),
        "percentage_mentions": len(PERCENT_RE.findall(text)),
        "action_terms": occurrences(text, ACTION_TERMS),
        "repeated_paragraph_starts": repeated_starts,
        "duplicate_paragraphs": duplicate_paragraphs,
    }


def render_text(report: dict[str, object]) -> str:
    lines = [
        f"Words: {report['words']}",
        f"Paragraphs: {report['paragraphs']}",
        f"Sentences: {report['sentences']}",
        f"Average sentence length: {report['average_sentence_words']} words",
        f"Money mentions: {report['money_mentions']}",
        f"Percentage mentions: {report['percentage_mentions']}",
    ]
    for key, label in (
        ("hedges", "Hedges"),
        ("passivity_markers", "Passivity markers"),
        ("process_labels", "Process labels"),
        ("generic_slop", "Generic slop"),
        ("action_terms", "Action terms"),
        ("repeated_paragraph_starts", "Repeated paragraph starts"),
    ):
        values = report[key]
        lines.append(f"\n{label}:")
        if values:
            lines.extend(f"  {name}: {count}" for name, count in values.items())
        else:
            lines.append("  none")

    long_sentences = report["long_sentences_over_25_words"]
    lines.append("\nLong sentences (>25 words):")
    if long_sentences:
        lines.extend(f"  [{item['words']} words] {item['text']}" for item in long_sentences)
    else:
        lines.append("  none")
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", help="Text, Markdown, or HTML file; omit for stdin")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.path:
        path = Path(args.path)
        raw = path.read_text(encoding="utf-8")
        text = html_to_text(raw) if path.suffix.lower() in {".html", ".htm"} else raw
    else:
        text = sys.stdin.read()

    report = analyze(text)
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(render_text(report))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Search the OPC 200-case product library.

This is a lightweight lexical retriever. It is meant to shortlist candidate
cases for an agent, not to replace semantic judgment.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path


DEFAULT_SOURCE = Path(
    "11_能力与Agent/03_项目级skill/maker-forge/references/product-cases-200.md"
)


@dataclass
class Case:
    index: int
    code: str
    name: str
    type: str
    background: str
    result: str
    insight: str
    source: str


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def field(body: str, label: str) -> str:
    match = re.search(rf"(?m)^- \*\*{re.escape(label)}\*\*：(?P<v>.*)$", body)
    return match.group("v").strip() if match else ""


def parse_cases(text: str) -> list[Case]:
    pattern = re.compile(
        r"(?ms)^###\s+(?P<idx>\d{3})\.\s+(?P<code>\S+)\s+(?P<name>.*?)\r?\n\r?\n"
        r"(?P<body>.*?)(?=^###\s+\d{3}\.\s+|\Z)"
    )
    cases: list[Case] = []
    for match in pattern.finditer(text):
        body = match.group("body")
        cases.append(
            Case(
                index=int(match.group("idx")),
                code=match.group("code").strip(),
                name=match.group("name").strip(),
                type=field(body, "类型"),
                background=field(body, "需求背景"),
                result=field(body, "结果"),
                insight=field(body, "启发"),
                source=field(body, "来源"),
            )
        )
    return cases


def cjk_ngrams(text: str, n_min: int = 2, n_max: int = 4) -> set[str]:
    runs = re.findall(r"[\u4e00-\u9fff]+", text)
    grams: set[str] = set()
    for run in runs:
        for n in range(n_min, n_max + 1):
            for i in range(0, max(0, len(run) - n + 1)):
                grams.add(run[i : i + n])
    return grams


def query_terms(query: str) -> list[str]:
    lowered = query.lower()
    terms = set(re.findall(r"[a-z0-9][a-z0-9._-]+|[\u4e00-\u9fff]+", lowered))
    terms.update(cjk_ngrams(lowered))
    return [term for term in terms if len(term) >= 2]


def score_case(case: Case, terms: list[str]) -> int:
    haystacks = [
        (case.name.lower(), 10),
        (case.type.lower(), 8),
        (case.insight.lower(), 5),
        (case.background.lower(), 3),
        (case.result.lower(), 1),
    ]
    score = 0
    for term in terms:
        for text, weight in haystacks:
            if term in text:
                score += weight
    return score


def filter_cases(cases: list[Case], contains_type: str | None) -> list[Case]:
    if not contains_type:
        return cases
    needle = contains_type.lower()
    return [case for case in cases if needle in case.type.lower()]


def rank_cases(cases: list[Case], query: str, contains_type: str | None) -> list[tuple[int, Case]]:
    candidates = filter_cases(cases, contains_type)
    if not query:
        return [(0, case) for case in candidates]
    terms = query_terms(query)
    ranked = [(score_case(case, terms), case) for case in candidates]
    ranked = [item for item in ranked if item[0] > 0]
    return sorted(ranked, key=lambda item: (-item[0], item[1].index))


def case_to_brief(case: Case, score: int) -> dict[str, object]:
    return {
        "score": score,
        "index": case.index,
        "code": case.code,
        "name": case.name,
        "type": case.type,
        "result": case.result,
        "insight": case.insight,
        "source": case.source,
        "background": case.background,
    }


def print_markdown(title: str, ranked: list[tuple[int, Case]], limit: int) -> None:
    print(f"## {title}")
    if not ranked:
        print("\nNo matches.\n")
        return
    for score, case in ranked[:limit]:
        print(f"\n### {case.index:03d}. {case.code} {case.name}")
        print(f"- 分数: {score}")
        print(f"- 类型: {case.type}")
        print(f"- 结果: {case.result}")
        print(f"- 启发: {case.insight}")
        print(f"- 来源: {case.source or '未记录'}")
        print(f"- 需求背景: {case.background}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Search OPC product case corpus.")
    parser.add_argument("query", nargs="?", default="", help="Search query, e.g. '培训 课程 SaaS'")
    parser.add_argument("--root", default=".", help="OPC root directory")
    parser.add_argument("--source", default=str(DEFAULT_SOURCE), help="Case library path relative to root")
    parser.add_argument("--type", default=None, help="Filter by text in type, e.g. success, failure, SaaS")
    parser.add_argument("--limit", type=int, default=5, help="Number of success/general matches")
    parser.add_argument("--failure-limit", type=int, default=3, help="Number of failure matches")
    parser.add_argument("--format", choices=["markdown", "json"], default="markdown")
    args = parser.parse_args()

    sys.stdout.reconfigure(encoding="utf-8")
    source = Path(args.root) / args.source
    if not source.exists():
        print(f"Source not found: {source}", file=sys.stderr)
        return 2

    cases = parse_cases(read_text(source))
    if len(cases) != 200:
        print(f"Warning: expected 200 cases, parsed {len(cases)}", file=sys.stderr)

    ranked = rank_cases(cases, args.query, args.type)
    failures = rank_cases(cases, args.query, "failure")

    if args.format == "json":
        payload = {
            "query": args.query,
            "source": str(source),
            "total_cases": len(cases),
            "matches": [case_to_brief(case, score) for score, case in ranked[: args.limit]],
            "failure_counterexamples": [
                case_to_brief(case, score) for score, case in failures[: args.failure_limit]
            ],
        }
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 0

    print_markdown("匹配案例", ranked, args.limit)
    print()
    print_markdown("失败反例", failures, args.failure_limit)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

---
name: maker-forge
description: "Use OPC's 200-case product library to evaluate product ideas, identify real demand, find analogous success and failure cases, rewrite vague ideas into demand statements, and design a 3-hour Codex MVP. Use when users ask about product ideas, MVP planning, 真需求/伪需求判断, 案例类比, workshop training exercises, 客户方案机会判断, or comparing a business/workflow idea against product cases."
---

# 造物工坊 Maker Forge

Version: v0.1.0

## Core Rule

Use cases as analogy evidence, not proof. Always separate:

- what the case actually shows
- what is similar in the user's idea
- what remains unverified
- what can be tested in a 3-hour MVP

Do not claim a product idea is validated only because a similar case exists. A case can inspire questions, risks, and MVP scope; the user's real customer still needs direct validation.

## Source Corpus

Primary corpus:

- `references/product-cases-200.md`

Use the map first:

- `references/case-library-map.md`

Use the local script when you need candidate cases quickly:

```bash
python "11_能力与Agent/03_项目级skill/maker-forge/scripts/case_search.py" "培训 课程 SaaS" --root . --limit 5 --failure-limit 3
```

If the script returns weak matches, search the corpus manually with `rg` and use judgment. Chinese product ideas often require semantic bridging, not literal keyword matching.

## Operating Modes

Use the lite mode by default:

1. Rewrite the user's idea into a demand sentence.
2. Retrieve 3-5 similar success cases and 2-3 failure counterexamples.
3. Extract the shared pattern and the broken pattern.
4. Score demand strength and MVP feasibility.
5. Output a 3-hour Codex MVP plan.

Use full mode only when the user asks for a formal report, customer plan, course exercise, product strategy, or saveable artifact. Read `references/full-plan.md` before full mode.

## Lite Workflow

1. Clarify the input.
   Identify industry, user role, workflow, current workaround, pain, cost, buyer, and desired result. If these are missing, infer cautiously and mark assumptions.

2. Write the demand sentence.
   Use this pattern:

   ```text
   谁，在什么场景下，因为现有方案什么问题，付出了什么代价，所以需要什么结果。
   ```

3. Retrieve cases.
   Prefer a mix:

   - 3-5 success cases close to the user's workflow
   - 2-3 failure cases close to the user's risk pattern
   - at least 1 case outside the same industry but sharing the same workflow shape

4. Classify the opportunity.
   Use the corpus's dominant patterns:

   - vertical SaaS / workflow software
   - sales acquisition / growth tools
   - professional tools
   - content products / online courses
   - browser plugins / light tools
   - AI tools / AI services
   - low-code / no-code platforms
   - failure patterns such as competition pressure, bad business model, poor product, platform dependence, trust/governance issues

5. Score the idea.
   Use 1-5 scores and one-line reasoning:

   - Pain frequency: how often the pain appears
   - Cost intensity: money, time, revenue, risk, reputation, or emotional cost
   - Workflow proximity: whether it is embedded in an existing repeated workflow
   - Buyer clarity: whether the paying person is clear
   - Alternative pressure: why users would not just use incumbents
   - MVP feasibility: whether a useful slice can be built in 3 hours

6. Design the 3-hour MVP.
   Include:

   - narrow user
   - must-have workflow
   - input/output
   - first screen or first command
   - data needed
   - non-goals
   - validation question

7. Close with the next action.
   The next action should be a concrete customer interview, landing page test, manual service test, clickable prototype, or Codex build task.

## Output Shape

Use `references/output-template.md` for the default response.

Do not dump every retrieved case. Show only the cases that change the decision.

Every case shown to the user must include its source link. If a case has no source link, write `来源：未记录` rather than omitting the field.

## Upgrade Plan

The current skill is the lightweight version. The complete roadmap and upgrade checklist live in:

- `references/lightweight-plan.md`
- `references/full-plan.md`
- `references/upgrade-checklist.md`

Before upgrading the skill, update the checklist first, then implement one phase at a time.

## Boundaries

- Do not write product strategy artifacts unless the user asks to save,落地,生成文件, or做方案.
- Do not copy the full 200-case corpus into `SKILL.md`.
- Do not treat Starter Story or Failory case metadata as independently verified financial truth. Attribute outputs to the source corpus.
- Do not expose raw source-event names, private collection labels, or original internal file names in user-facing answers. Use the sanitized corpus name `product-cases-200.md`.
- Do not expose internal OPC paths in customer-facing exports unless the artifact is explicitly internal.
- If using this for a client knowledge-base product, hand off to `kb-foundry` after the opportunity and MVP shape are clear.

## References

- `references/case-library-map.md`: read first to understand the corpus distribution and common patterns.
- `references/output-template.md`: use for normal user-facing answers.
- `references/lightweight-plan.md`: use when explaining or modifying the lite version.
- `references/full-plan.md`: use when planning a formal or productized version.
- `references/upgrade-checklist.md`: use before any future upgrade.
- `scripts/case_search.py`: use to parse and search the case corpus.

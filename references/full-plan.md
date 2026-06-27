# Full Plan

The full version turns the case library into a product opportunity operating system.

## Target Use Cases

- Product opportunity screening
- 3-hour Codex MVP workshops
- Workshop training exercises
- Customer solution diagnosis
- Course material generation
- Internal case-based product thinking drills

## Full Capability Set

1. Structured case database
   Convert every case into JSON or Markdown case cards with stable fields:
   `id`, `name`, `status`, `category`, `user`, `scenario`, `workaround`, `pain`, `cost`, `product`, `result`, `lesson`, `source`.

2. Hybrid retrieval
   Combine keyword search, category filters, and semantic search. Retrieval should support:
   industry, role, workflow, pain, monetization model, failure risk, MVP type.

3. Demand strength scoring
   Add a scoring rubric with explicit weights:
   pain frequency, cost intensity, budget owner, workflow repetition, current workaround, urgency, alternative pressure, distribution path, trust/risk, MVP feasibility.

4. Failure pattern radar
   Map every idea against failure patterns:
   competition, bad economics, weak PMF, poor product, platform dependence, trust/governance, cash flow, focus drift, timing.

5. MVP blueprint generator
   Produce build-ready MVP briefs:
   first screen, data model, user flow, output spec, non-goals, validation metric, demo script.

6. Training question generator
   Turn cases into exercises:
   hide result, ask learners to identify demand, risk, wedge, MVP; reveal case outcome and lesson.

7. Customer-plan adapter
   Convert product opportunity analysis into customer-facing diagnosis, proposal, and implementation plan. Hand off to `kb-foundry` when this becomes a client knowledge-base or operating-system delivery.

8. Evidence and feedback loop
   Store tested ideas, interview notes, MVP outcomes, and post-test lessons back into OPC:
   `04_选题决策/`, `06_产品交付/`, `08_数据反馈/`, or `03_知识沉淀/` depending on use.

## Suggested Architecture

```text
case corpus
-> normalized case cards
-> retrieval script / hybrid search
-> scoring rubric
-> MVP blueprint template
-> training exercise template
-> validation records
-> feedback into case library
```

## Productization Path

Lite internal tool:

- one script
- one source corpus
- one output template

Standard project skill:

- structured case cards
- scoring rubric
- training generator
- validation record template

Full product:

- local app or Feishu/Miaoda front end
- filters and search
- saved analyses
- workshop mode
- exportable MVP briefs
- customer-facing proposal mode

## Risks

- Case data may contain source bias or unverified numbers.
- Lexical search may miss semantic similarity.
- Too many examples can create false confidence.
- Full system can become heavy before real usage proves demand.

## Full-Version Acceptance Criteria

- Search returns useful analogies for at least 20 realistic product ideas.
- Failure radar catches obvious bad economics and incumbent pressure.
- Training exercises are usable without manual rewriting.
- MVP briefs are concrete enough for Codex to build from.
- The system stores validation results and improves the case library over time.

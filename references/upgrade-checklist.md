# Upgrade Checklist

Update this checklist before changing the skill. Move one phase at a time.

## v0.1 Lite Baseline

- [x] Create project-level skill folder under `11_能力与Agent/03_项目级skill/maker-forge/`.
- [x] Keep `SKILL.md` lightweight and workflow-oriented.
- [x] Record source corpus location.
- [x] Record lightweight plan.
- [x] Record full plan.
- [x] Record upgrade checklist.
- [x] Add a reusable local case search script.
- [x] Add a default output template.
- [ ] Run at least 3 real product idea tests with the user.
- [ ] Record what retrieval missed or overmatched.

## v0.2 Structured Corpus

- [ ] Parse all 200 cases into stable JSON.
- [ ] Add fields: user, scenario, workaround, pain, cost, product, buyer, result, lesson, source.
- [ ] Add category aliases for Chinese/English search.
- [ ] Add unit tests for parser count, first case, last case, and required fields.
- [ ] Add `--category`, `--success-only`, `--failure-only`, and `--json` usage examples to `SKILL.md`.
- [ ] Create a small gold set of 10 product idea queries with expected case families.

## v0.3 Demand Scoring

- [ ] Create `references/demand-scoring-rubric.md`.
- [ ] Define 1-5 scoring anchors for each dimension.
- [ ] Add failure-risk mapping rules.
- [ ] Add output examples for strong, medium, and weak ideas.
- [ ] Test against at least 10 real or historical ideas.

## v0.4 Training Mode

- [ ] Create `references/training-exercise-template.md`.
- [ ] Generate exercise format: prompt, hidden result, learner questions, reveal, debrief.
- [ ] Add workshop-mode output for product case training sessions.
- [ ] Produce 5 sample exercises from the corpus.

## v0.5 MVP Blueprint Mode

- [ ] Create `references/mvp-blueprint-template.md`.
- [ ] Add fields: first screen, workflow, data model, user actions, non-goals, validation metric.
- [ ] Test by building at least 3 Codex MVPs from generated briefs.
- [ ] Record build blockers and revise template.

## v1.0 Productized System

- [ ] Decide whether to keep as project skill, sync to global skill, or turn into a local app.
- [ ] Add semantic or hybrid retrieval if lexical search remains weak.
- [ ] Add saved analysis records under the appropriate OPC business flow.
- [ ] Register or update the capability in `能力开关表.md` after enough real usage evidence.
- [ ] Create a customer-facing export mode if used in paid delivery.
- [ ] Create retirement criteria if the skill becomes redundant with another product opportunity engine.

## Capability Registration Reminder

Suggested capability ID after validation:

```text
maker_forge
```

Suggested state before validation:

```text
experimental
```

Suggested service nodes:

- `daily_content_flow`: 选题判断 / 产品案例类比
- `product_delivery_flow`: 客户需求诊断 / 方案设计
- `capability_onboarding_flow`: 新产品化能力试跑验证
- `client_kb_product_flow`: 客户知识库产品机会判断

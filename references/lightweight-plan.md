# Lightweight Plan

This is the current v0.1.0 design.

## Goal

Turn a vague product idea into a case-backed demand judgment and a 3-hour Codex MVP plan.

## Inputs

Accept any of these:

- a rough product idea
- an industry or customer role
- a workflow pain
- a customer request
- a course or workshop exercise
- a client opportunity

## Output

Produce:

- standard demand sentence
- similar success cases
- failure counterexamples
- opportunity pattern
- demand score
- MVP scope
- validation questions
- next action

## Workflow

1. Rewrite the idea into the demand sentence:

   ```text
   谁，在什么场景下，因为现有方案什么问题，付出了什么代价，所以需要什么结果。
   ```

2. Retrieve 3-5 success cases and 2-3 failure cases.

3. Extract the shared pattern:

   - user type
   - repeated workflow
   - current workaround
   - cost
   - monetization path
   - first wedge

4. Score the idea:

   - pain frequency
   - cost intensity
   - workflow proximity
   - buyer clarity
   - alternative pressure
   - MVP feasibility

5. Design a 3-hour MVP:

   - one target user
   - one repeated workflow
   - one output
   - one measurable validation signal

## What Lite Version Does Not Do

- It does not create a full structured database.
- It does not run embeddings or semantic vector search.
- It does not verify case financial data beyond the source corpus.
- It does not write strategy files unless the user asks.
- It does not replace direct customer interviews.

## Acceptance Criteria

- The output includes at least 3 relevant success cases and 2 failure counterexamples.
- The demand sentence is concrete enough to interview a customer.
- The MVP can be built or mocked within 3 hours.
- The answer marks assumptions and unverified points.
- The user can decide whether to interview, prototype, discard, or refine the idea.

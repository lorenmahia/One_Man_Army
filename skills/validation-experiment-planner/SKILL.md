---
name: validation-experiment-planner
description: "Plan cheap demand and pricing experiments with thresholds written before running anything, small-sample interval checks and a go, adjust or stop gate. Use when the user wants to validate an idea, test demand or willingness to pay, design an experiment, or decide whether to build or stop."
---

# Validation experiment planner

Turns a business idea into a short, ordered set of experiments with written pass and fail thresholds, so the founder decides on evidence rather than hope. It plans the tests; the founder runs them.

## Why it works this way

Public post-mortems of VC-backed startups often cite running out of capital and poor product-market fit (CB Insights, March 2026, 385 shutdowns: 70% and 43%; a snapshot, VC-backed samples only). Commitments of time or money are stronger evidence than compliments or clicks. Small samples measure rates poorly, so thresholds must be fixed first and results read as intervals.

## Steps

1. Load the playbook: read `playbooks/01-validate/validation-and-experiment-design.md` in the repo if available, otherwise fetch https://raw.githubusercontent.com/lorenmahia/One_Man_Army/main/playbooks/01-validate/validation-and-experiment-design.md
2. Ask ONE round of intake questions:
   - The idea and the target segment.
   - The price or fee they have in mind.
   - Evidence so far (interviews, waitlist, sales).
   - Budget in money and weekly hours, and the date they want a decision by.
   - Business type (B2B, consumer, local service, creator) and country if the sector is regulated.
3. List the riskiest assumptions (who has the problem, will they pay, can you reach them, does the economics work). Rank by how badly a wrong guess would hurt.
4. Rank demand tests for the top assumptions from cheapest and weakest to costlier and strongest:
   - Interviews, landing page or fake door, smoke test with ads.
   - Price ask, concierge or Wizard-of-Oz, pre-sales or deposits, paid pilot.
   - Recommend the cheapest test that could falsify the idea. Playbook cost figures are estimates; say so.
5. For each chosen test write, with a date, BEFORE running it:
   - Hypothesis: "We believe [segment] has [problem]. If we offer [solution] at [price], at least [X of N] will [action] within [time]."
   - A kill statement, plus pass, adjust and fail thresholds.
6. Give small-sample guidance with 95% Wilson intervals.
   - Illustrative, from the playbook and recomputed: 0 of 20 gives 0% to 16.1%; 4 of 40 gives 4.0% to 23.1%; 5 of 100 gives 2.2% to 11.2%.
   - The whole interval, not the point estimate, decides.
   - Recompute for the founder's own counts and label the result illustrative.
7. Produce the experiment log table. Columns: date; hypothesis; segment; test type; pass / adjust / fail thresholds; planned sample; start and end dates; raw counts; 95% interval; decision; what we learned; next action; cost in money and hours.
8. Set the go / adjust / stop gate:
   - A calendar date and example criteria for the founder's business type (illustrative in the playbook).
   - At most two adjust rounds before a forced decision.
   - A clean-kill checklist: log the decision, inform participants, delete unneeded personal data, refund deposits, write a short post-mortem.
9. Hand off:
   - `customer-discovery-interviews` for the interview guide.
   - `unit-economics-model` to tie thresholds to price, cost and acquisition cost.
   - `deadline-calendar-sync` for the gate date, if wanted.
   - Point to playbook sections 3 (tests), 4 (pricing), 5 (experiment design) and 7 (gate) for evidence.

## Rules

- Research and planning support only; not legal, tax, investment or financial advice.
- Never invent figures. Quote the playbook's dated figures (last verified 2026-11-11) and say they are snapshots; mark anything unverified or secondary.
- Treat benchmark numbers (conversion rates, reply rates, failure shares) as ranges, not targets.
- Thresholds are written and dated before any test; move them only through a logged decision.
- Count payments, deposits and signed commitments as strong evidence; likes, free signups and friendly interest as weak.
- Fake-door tests must disclose promptly that the product is not available yet; never take money for something that cannot be delivered.
- Collect no personal data beyond what the user chooses to share; tell participants what the research is for.
- Never contact anyone, send outreach, run ads, post anything or make commitments for the user.
- Regulated sectors (health, finance, children, legal): advise professional advice before collecting data or charging pilots.

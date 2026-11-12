# Validation Experiment Planner

> Rank demand tests by cost and evidence strength, write thresholds before you run anything, and reach a dated go / adjust / stop decision.

## When to use it

- "I have an idea. What is the cheapest way to find out if anyone will pay?"
- "Design an experiment to test my pricing with only a handful of prospects."
- "I got 4 signups from 40 visitors. Is that good?"
- "Help me decide whether to build this or stop."

## What you get

- **A ranked list of the riskiest assumptions** behind your idea
- **A test ladder** from cheapest and weakest to costlier and strongest, with a recommended first test
- **Written hypotheses** with pass, adjust and fail thresholds, fixed before any test starts
- **Small-sample intervals** so you read results as ranges, not single percentages (illustrative figures, recomputed)
- **An experiment log table** you can paste into a spreadsheet
- **A go / adjust / stop gate** with a calendar date and a clean-kill checklist

## How it works

```
Intake questions -> Riskiest assumptions -> Pick cheapest falsifying test
   -> Write hypothesis + thresholds first -> Run (you) -> Read the interval
   -> Log -> Go / adjust / stop on the gate date
```

## Boundaries

- Research and planning support only; not legal, tax, investment or financial advice.
- Figures come from the playbook with their dates and are snapshots, not guarantees.
- It never contacts anyone, runs ads or makes commitments for you.
- Regulated sectors need professional advice before collecting data or charging pilots.

## Works well with

- [`customer-discovery-interviews`](../customer-discovery-interviews/) for the interview guide behind problem validation.
- [`unit-economics-model`](../unit-economics-model/) to tie thresholds to price, cost and acquisition cost.
- [`deadline-calendar-sync`](../deadline-calendar-sync/) to put the gate date in your calendar.
- Evidence and sources: [validation and experiment design playbook](../../playbooks/01-validate/validation-and-experiment-design.md).

## Install

**Claude Code:** /plugin marketplace add lorenmahia/One_Man_Army, then /plugin install one-man-army@one-man-army.

**Claude.ai / Desktop:** zip the validation-experiment-planner folder and upload it under **Settings -> Capabilities -> Skills**.

Full instructions are in [`SKILL.md`](./SKILL.md).

# Security Baseline Audit

> Score your setup against ten baseline security controls and get a prioritised fix list, a minimal policy set and a one-page incident runbook.

A self-reported audit for one-person companies: you answer a short set of questions, Claude scores each control and tells you what to fix first.

## When to use it

- "Am I covered on security basics before I launch?"
- "A customer sent a security questionnaire. Where are my gaps?"
- "Do I need SOC 2 yet, and what should I do first?"
- "Write me an incident runbook for when something goes wrong."

## What you get

| Deliverable | Contents |
|---|---|
| **Score table** | Ten controls rated done / partial / missing, with the evidence you gave |
| **Fix list** | Prioritised by Day 1 / Week 1 / Month 1 / Quarter 1, with the playbook's time estimates |
| **Minimal policy set** | The ten short policies, ordered by what you need first |
| **Incident runbook** | One page: detect, contain, rotate, assess, notify, learn, tailored to your accounts |
| **Verify list** | Plan features and jurisdiction rules to confirm yourself |

## How it works

Loads the playbook, asks one round of questions about what you hold and how each control stands, scores from your answers, then delivers the fix list, policies and runbook. It does not scan your systems unless you agree to a named, read-only check.

## Boundaries

- Research and planning support only; not legal, tax, investment or financial advice. Breach-notification duties need counsel.
- The score is self-reported; it does not prove you are secure.
- Breach-cost and SOC 2 cost figures are dated, vendor-biased ranges, not forecasts.
- It never asks for secrets. If you paste one, `secret-exposure-response` takes over.

## Works well with

[`secret-exposure-response`](../secret-exposure-response/) for leaks, [`ci-cd-bootstrap`](../ci-cd-bootstrap/) for pipeline hardening, [`data-protection-readiness`](../data-protection-readiness/) for privacy duties, and the playbook [`security-and-secrets-baseline`](../../playbooks/03-build/security-and-secrets-baseline.md).

## Install

**Claude Code:** /plugin marketplace add lorenmahia/One_Man_Army, then /plugin install one-man-army@one-man-army.

**Claude.ai / Desktop:** zip the security-baseline-audit folder and upload it under **Settings -> Capabilities -> Skills**.

Full instructions are in [`SKILL.md`](./SKILL.md).

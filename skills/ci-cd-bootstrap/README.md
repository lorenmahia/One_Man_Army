# CI/CD Bootstrap

> Turn your stack into a staged CI/CD and release plan, with safe workflow drafts and a way to track delivery performance.

Takes a solo founder from "I push to main and hope" to protected branches, automated checks, short-lived credentials and a rollback you have rehearsed.

## When to use it

- "Set up CI/CD for my Next.js app on GitHub."
- "How do I deploy safely and roll back when I'm the only developer?"
- "Review my GitHub Actions setup for security."
- "What should I track to know if my releases are healthy?"

## What you get

| Deliverable | Contents |
|---|---|
| **Adoption plan** | Day 1 / Week 1 / Month 1 / Quarter 1 items tailored to your stack, each with a "done when" line |
| **Pipeline design** | Stages, triggers, build-once-promote-many flow, branch protection and rollback path |
| **Workflow drafts (optional)** | Files with `<FULL_40_CHAR_SHA>` placeholders, least-privilege `permissions:` and OIDC instead of stored cloud keys |
| **DORA tracking sheet** | How to record the five delivery metrics monthly with no extra tooling |
| **Verify list** | Plan limits and action versions you must check yourself |

## How it works

Loads the playbook, asks one round of questions about stack, host, repo platform and deploy target, places you on the staged ladder, then delivers the plan and design. Drafts are offered, not forced, and nothing is run or changed without your approval.

## Boundaries

- Research and planning support only; not legal, tax, investment or financial advice.
- It never invents action versions or SHAs; you look up and verify each one.
- Playbook figures (free minutes, DORA clusters) are dated snapshots, not targets.
- It does not run commands or change your repos or cloud accounts without approval, and never needs your secrets.

## Works well with

[`security-baseline-audit`](../security-baseline-audit/) for the wider security controls, [`secret-exposure-response`](../secret-exposure-response/) if a credential leaks, and the playbook [`cicd-and-release-pipeline`](../../playbooks/03-build/cicd-and-release-pipeline.md).

## Install

**Claude Code:** /plugin marketplace add lorenmahia/One_Man_Army, then /plugin install one-man-army@one-man-army.

**Claude.ai / Desktop:** zip the ci-cd-bootstrap folder and upload it under **Settings -> Capabilities -> Skills**.

Full instructions are in [`SKILL.md`](./SKILL.md).

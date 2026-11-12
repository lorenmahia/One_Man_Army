---
name: ci-cd-bootstrap
description: "Design a staged CI/CD and release pipeline for a solo founder: intake, then a Day 1 / Week 1 / Month 1 / Quarter 1 adoption plan, pipeline design, SHA-pinned workflow drafts and DORA tracking. Use when the user asks to set up CI/CD, GitHub Actions, deploys, rollbacks or release process."
---

# CI/CD bootstrap

The purpose is to give a one-person team a safe, boring delivery pipeline: protected main, automated checks, short-lived credentials and a fast rollback. It produces a plan and drafts, not a toolchain shopping list.

## Why it works this way

The playbook argues that enterprise-grade delivery is a set of habits, not a toolchain, and that most of it fits free tiers. Staging the work stops a founder building Quarter 1 items before Day 1 is done. Anything about plan limits or action versions changes often, so it is verified, not assumed.

## Steps

1. **Load the playbook.** Read `playbooks/03-build/cicd-and-release-pipeline.md` in the repo if available; otherwise fetch `https://raw.githubusercontent.com/lorenmahia/One_Man_Army/main/playbooks/03-build/cicd-and-release-pipeline.md`. Note its "Last verified" date.
2. **Ask one round of intake questions** (all at once, short answers are fine):
   - Language and framework, and how it is built (container, bundle, static).
   - Repo platform and plan (public or private, free or paid).
   - Hosting and deploy target (PaaS, VM, serverless, cloud provider).
   - Existing CI, tests, staging, and how a release goes out today.
   - Cloud accounts that currently hold long-lived keys in CI, if any.
   - Hours per week available, and whether AI tools write much of the code.
3. **Place them on the ladder.** Say which stage items already exist, using the playbook's Day 1 / Week 1 / Month 1 / Quarter 1 table as the yardstick.

   Day 1 means repo hygiene, protected main, a basic CI file and a budget alert.
   Week 1 means pinned actions, a staging deploy and a tag-based production deploy.
   Month 1 means scoped environments, OIDC, a first rollback rehearsal and a DORA sheet.
   Quarter 1 means infrastructure as code, drift checks and monthly metric reviews.

4. **Deliver the adoption plan.** A table of the four horizons, each item tailored to the stack, with a "done when" line. Do Day 1 in full; keep later horizons short. Do not schedule Quarter 1 work until Week 1 and Month 1 are boring.
5. **Deliver the pipeline design.** Stages (lint, test, build, dependency scan, secret scan, deploy, rollback), which trigger runs each, the artifact flow (build once, promote the same artifact), and the rollback path. Cover branch protection settings and which ones the founder's plan may not enforce (mark as verify in repo settings).
6. **Offer workflow drafts** only if the user wants them. Drafts must:
   - use `<FULL_40_CHAR_SHA>` for every `uses:` reference, with a version comment, and tell the user to look up and verify each action's current SHA from the original repository;
   - set top-level `permissions:` to least privilege (read-only by default, `id-token: write` only on the deploy job);
   - use OIDC to the cloud provider instead of stored keys, with trust-policy conditions to be written by the user and checked against the provider docs;
   - add `concurrency:` with cancel-in-progress, and a Dependabot config for code and actions.
   Show the draft in chat or write a file only when the user approves.
7. **Set up DORA tracking.** Give a monthly spreadsheet layout for the five metrics and how to read each from tags, deploy runs and incident notes. Quote the playbook's 2024 cluster table only as a dated, secondary-source snapshot and prefer trends over labels.
8. **Hand off.** List open questions the user must verify (plan limits, push protection availability, current action SHAs). Point to the playbook sections used (1 hygiene, 2 pipeline, 3 secrets, 4 releases, 5 DORA, 7 staged plan). If a credential was ever committed or pasted, apply `secret-exposure-response`. Suggest `security-baseline-audit` next.

## Output shape

- Start with a three-line summary: where the founder is, the single next action, and the time it takes (an estimate).
- Then the plan table, the pipeline design, optional drafts, the DORA sheet and the verify list, in that order.
- Mark each claim as playbook fact, playbook inference, or your own suggestion.

## Rules

- This is research and planning support only, not legal, tax, investment or financial advice.
- Never invent versions, SHAs, thresholds or figures. Quote the playbook's dated figures with their date and say they are snapshots. Mark anything unverified.
- Never run commands, install tools or change the user's repos, workflows or cloud accounts without explicit approval.
- Never ask the user to paste secrets, tokens or keys. Ask for names and scopes only.
- Treat benchmark numbers (DORA clusters, free-minute allowances, time targets) as ranges and as estimates.
- Keep the plan sized to one person; skip tools and rituals that need a team.

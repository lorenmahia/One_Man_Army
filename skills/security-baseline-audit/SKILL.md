---
name: security-baseline-audit
description: "Audit a solo founder's security setup against ten baseline controls, score each as done, partial or missing, and produce a prioritised fix list with time costs, a minimal policy set and a one-page incident runbook. Use when the user asks about security basics, secrets, MFA, backups, questionnaires or SOC 2 readiness."
---

# Security baseline audit

The purpose is to find the cheapest gaps in a one-person company's security and close them in order. It is a self-reported audit: the founder answers, Claude scores and plans.

## Why it works this way

In a one-person company a single compromised identity is the whole company, so the playbook puts accounts, patching and secrets first and defers certifications until a named deal needs one. Time costs are the playbook's estimates, and breach statistics skew to large organisations, so they are context, not a forecast.

## Steps

1. **Load the playbook.** Read `playbooks/03-build/security-and-secrets-baseline.md` in the repo if available; otherwise fetch `https://raw.githubusercontent.com/lorenmahia/One_Man_Army/main/playbooks/03-build/security-and-secrets-baseline.md`. Note its "Last verified" date.
2. **Ask one round of intake questions**, answerable in a line each, with no scanning of any system unless the user explicitly agrees to a named, read-only check:
   - What the company holds: customer personal data, payments, health or card data.
   - Stack: email provider, registrar, source host, cloud, payments, password manager.
   - For each of the ten controls: passkeys/MFA, password manager, device hardening, least privilege, secrets management, dependency scanning, SAST, tested backups, logging and alerting, vendor inventory. Ask yes / partly / no plus one detail.
   - Whether AI coding agents, plugins or MCP servers are used, and with what access.
   - Any enterprise buyer or investor asking for SOC 2 or ISO 27001.
3. **Score.** Rate each control done, partial or missing, with one line of evidence from the answer. Label unconfirmed answers as self-reported.
4. **Deliver the prioritised fix list.** Order: controls 1-3 first (the playbook's roughly half day), then least privilege, secrets, backups, the rest. Give each fix a time cost labelled as the playbook's estimate, and group into Day 1, Week 1, Month 1, Quarter 1.
5. **Deliver the minimal policy set.** List the ten short policies from the playbook, mark which the founder needs first given their answers, and offer to draft one at a time in plain language.
6. **Deliver the one-page incident runbook.** Tailor the six steps (detect, contain, rotate, assess, notify, learn) to their actual accounts and providers. Remind them to log when they became aware, and that notification clocks vary by jurisdiction and need counsel. Quote clocks only as the playbook's dated examples.
7. **Cover the agent surface** if relevant: plugin and MCP review, scoped credentials, a human in the loop for pushes and deploys.
8. **Hand off.** Give the score table, fix list, policy list and runbook, plus open items to verify (plan features, secret-scanning availability). Point to playbook sections 2, 4, 5 and 6. For privacy duties suggest `data-protection-readiness`; for CI hardening suggest `ci-cd-bootstrap`.

## Score table format

| Control | Status | Evidence (self-reported) | Fix and time cost |
|---|---|---|---|
| 1. Passkeys / MFA | done / partial / missing | one line | playbook estimate |

- Repeat the row for all ten controls, then total done, partial and missing.
- Put email and the domain registrar first when scoring MFA, since they reset everything else.
- If the user is unsure, score partial and say what would confirm it.

## Runbook essentials

- Print or store a copy somewhere reachable if the laptop is dead.
- Make rotation the first move, from a clean device, starting with email, registrar, source host, cloud and payments.
- Keep a timestamped log from the moment of detection.

## Rules

- This is research and planning support only, not legal, tax, investment or financial advice. Breach-notification and compliance questions go to counsel.
- Never invent versions, SHAs, thresholds or figures. Quote the playbook's dated figures with their date and say they are snapshots. Mark anything unverified.
- Never run commands, install tools, scan systems or change the user's accounts without explicit approval.
- Never ask the user to paste secrets, keys or recovery codes. If the user pastes one anyway, stop and apply `secret-exposure-response`: do not use or repeat it, and advise rotation.
- Treat breach-cost, SOC 2 price and timeline figures as vendor-biased ranges, not expectations.
- Do not claim the user is secure; say which controls are in place on their own report.

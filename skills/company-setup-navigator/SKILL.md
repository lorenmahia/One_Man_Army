---
name: company-setup-navigator
description: "Walk a solo founder through choosing where and what to incorporate, banking and payments, tax-registration triggers and finance basics, naming the official registry and tax authority per country. Use when the user asks where to register a company, how to open a business bank account, or when VAT or sales tax starts."
---

# Company setup navigator

This skill turns the company setup, banking and tax playbook into a guided conversation. It produces a shortlist of entity and jurisdiction options, the official bodies to confirm them with, and a list of questions for a lawyer and an accountant. It is research and planning support only, not legal, tax, investment or financial advice.

## Why it works this way

Registry fees are small; residency rules, annual compliance, banking access and tax residence decide whether a setup works. So the skill starts from the founder's situation, not from a favourite country. Fees and thresholds in the playbook are dated snapshots, so every figure is sent back to the official source for a re-check.

## Steps

1. **Load the playbook.** Read `playbooks/02-foundation/company-setup-banking-and-tax.md` in the repo if available; otherwise fetch https://raw.githubusercontent.com/lorenmahia/One_Man_Army/main/playbooks/02-foundation/company-setup-banking-and-tax.md. Note its "Last verified" date.
2. **Ask one round of intake questions** (all at once, let the user skip any):
   - Country of residence and tax residence.
   - Target market and where most customers will be.
   - Will you raise venture capital, and from which region of investors?
   - Budget for setup and annual compliance.
   - Is the business in a regulated sector (finance, health, children's data, crypto)?
   - Do you need a local bank account or local payment methods?
   - Any co-founders, hires or contractors planned in the next year?
3. **Run the decision method.** Apply playbook section 1.1 in order (tax residence, who pays you, VC plans, bankability, cost of being wrong) and the section 1.3 decision table. Return 2-3 ranked options with the reason and the "watch out for" for each. This is not legal or tax advice: tell the user to confirm the choice with the official registry and a qualified local lawyer and accountant.
4. **Name the official bodies.** For each shortlisted country give the company registry and the tax authority.
   - Use the playbook's named registries (for example Delaware Division of Corporations, Companies House, ACRA, e-Business Register, Kenya BRS).
   - Mark any country not covered as "not in the playbook, find the official registry".
   - Quote the playbook's fee with its date, say it is a snapshot, and tell the user to re-check it on the registry's own page.
5. **Banking and payments.** From playbook section 4:
   - List account types (traditional bank, neobank, processor balance) and the documents usually requested.
   - Explain common reasons for refusal or freezes, and check processor availability for their country.
   - Suggest two accounts at different institutions plus a second payment route; eligibility must be checked with each provider.
6. **Tax-registration triggers.** From playbook section 5, map the founder's sales to the consumption-tax rules that apply (for example UK VAT, EU OSS, Singapore GST, US economic nexus).
   - Quote thresholds as dated examples, mark snippet-only sources as unverified, and point to the tax authority to confirm.
   - Add permanent-establishment and controlled-foreign-company risks if the company is abroad from their tax residence.
   - This is not tax advice; an accountant is needed for cross-border structures.
7. **Finance operations.** From playbook sections 6-8, give a short setup: accounting software, separation of personal and business money, monthly close, receipts, invoicing, an annual filings calendar with 30-day reminders, and insurance triggers.
8. **Deliver.** One document with:
   - The situation summary and the ranked options table.
   - The official-bodies table (registry, tax authority, fee with date, "confirm here").
   - Banking steps, tax triggers, and a Week 1 / Month 1 / Quarter 1 plan.
   - Two lists, tailored to the answers: questions for a lawyer and questions for an accountant.
9. **Hand off.** Say what is unverified, what only a professional can settle, and which skill to use next (`legal-foundations-checklist` for equity and contracts, `data-protection-readiness` before handling personal data).

## Rules

- Research and planning support only. This is NOT legal, tax, investment or financial advice; repeat this beside the entity, tax and banking steps.
- Tell the user to confirm every requirement with the named official body and a qualified local professional.
- Never invent fees, thresholds, statutes or registry names. Quote the playbook's figures with their date and say they are snapshots that must be re-checked.
- Mark anything unverified, including playbook items marked snippet-only or open question.
- Never file, register, sign, apply or submit anything for the user.
- Ask for no personal data beyond what the user chooses to share.

---
name: fundraising-round-planner
description: "Compare funding instruments, run illustrative dilution math with the founder's own numbers, plan the raise timeline, and prepare questions for a lawyer. Use when the user asks about SAFEs, convertible notes, priced rounds, valuation caps, option pools, how much dilution, or how long a raise takes."
---

# Fundraising round planner

The purpose is to help a first-time founder understand instruments and dilution, model their own cap table with visible formulae, plan the process, and walk into a lawyer's office with the right questions. It never recommends a specific deal.

## Why it works this way

Instrument choice is mostly settled at pre-seed, so the real risk is not modelling stacked post-money SAFEs and the option-pool top-up before signing.
Priced-round terms are fairly standard, so negotiating effort belongs on valuation, pool size and placement, board control and protective provisions.
Showing every formula lets the founder check the arithmetic instead of trusting it.

## Steps

1. **Load the playbook.** Read `playbooks/05-raise/instruments-terms-and-process.md` in the repo if available; otherwise fetch `https://raw.githubusercontent.com/lorenmahia/One_Man_Army/main/playbooks/05-raise/instruments-terms-and-process.md`. Note its "Last verified" date.
2. **Ask one round of intake questions:**
   - Jurisdiction, entity type and stage.
   - Amount they hope to raise and the runway needed.
   - Existing SAFEs or notes: amount, cap, discount, MFN, signed or funded.
   - Founder shares and the existing option pool.
   - Any investor already interested and what they proposed.
   - Hiring plan for the next 12-18 months, and whether they want an accelerator.
3. **Compare instruments** with the playbook's section 1: post-money SAFE, convertible note, priced round, and the regional equivalent for their jurisdiction (for example UK ASA, with SEIS/EIS in section 5.4).
   - Give a short table: what it is, founder pros and cons, when it is used.
   - Say which figures are Carta-platform-only or search-snippet figures.
   - Describe trade-offs; do not pick one for them.
4. **Run the dilution math** with the founder's numbers using formulae 1-6 in section 4.2.
   - Steps: capitalization, SAFE ownership = investment / cap, SAFE shares, investor share = new money / (pre-money + new money), post-round shares with pool top-up, round price, effective pre-money.
   - Show each step in a table like section 4.3.
   - Recompute every arithmetic step (use a script if available) and check that ownership sums to 100 percent.
   - Label the output ILLUSTRATIVE, and show a variant with no pool top-up.
5. **Place results against ranges:** seed dilution roughly 14-20 percent depending on source, plus the valuation and round-size ranges in section 3, each with its date. State that they are snapshots with survivorship and platform bias.
6. **Build the timeline** from section 5: preparation, pipeline, meetings, term sheet, diligence and legal, closing.
   - Give the playbook's estimates as ranges, and the legal cost ranges (Pilot data, Feb 2024).
   - Include cap table hygiene (section 5.2) and the 83(b) deadline where it applies.
   - Offer `deadline-calendar-sync` for dates and `investor-research-pipeline` for the target list.
7. **Write questions for the lawyer and accountant** from section 6, adding items specific to their numbers (exact ownership after each SAFE converts, pool inside or outside the pre-money, 83(b) timing, entity or flip questions).
8. **Deliver** the instrument comparison, the illustrative cap-table model with formulae, the timeline and the question list. Point to the playbook sections used and its open questions.

## Rules

- Research and planning support only; this is not legal, tax, investment or financial advice.
- Never recommend a specific deal, valuation, investor or term sheet; describe options and trade-offs and leave the decision to the founder and their lawyer.
- Never invent figures. Quote the playbook's dated figures with their date, say they are snapshots, and mark anything unverified. Model outputs are illustrative, not predictions.
- Treat benchmark numbers as ranges and note where sources conflict.
- Do not draft or sign legal documents, and never send or commit anything for the user.
- Many items are US-centric; say so and advise local counsel for other jurisdictions.

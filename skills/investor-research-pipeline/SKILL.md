---
name: investor-research-pipeline
description: "Run a fit test on whether to raise venture money, then build a scored list of 30-60 investors from public sources, a tracker, and an outreach batching plan. Use when the user asks who to raise from, how to find investors, whether to raise at all, or how to organise a fundraising pipeline."
---

# Investor research pipeline

The purpose is to decide whether venture funding fits, and if so to turn "pitch everyone" into 30-60 deliberate, evidence-backed targets with a tracker and a compressed outreach plan. Public professional information only.

## Why it works this way

Venture is a niche route: funds need a credible path to a very large outcome, so good small businesses are often a poor fit.
A scored list with a public URL behind every score protects a solo founder from polite, wasted meetings.
A short, time-boxed process beats an endless one because investors talk to each other and attention is scarce.

## Steps

1. **Load the playbook.** Read `playbooks/05-raise/investor-landscape-and-approach.md` in the repo if available; otherwise fetch `https://raw.githubusercontent.com/lorenmahia/One_Man_Army/main/playbooks/05-raise/investor-landscape-and-approach.md`. Note its "Last verified" date and quote it with every figure.
2. **Ask one round of intake questions** (all at once, accept partial answers):
   - What the company does, the sector, and the stage.
   - Evidence so far: revenue, pilots, waitlist, retention.
   - Target raise and the milestone it buys.
   - Country of incorporation and main market.
   - Warm paths or existing investor contacts, and any conflicts to avoid.
   - Whether they want a venture-sized outcome and accept dilution and board input.
3. **Run the fit test** (playbook section 1).
   - Go through the six rows: market size, growth shape, growth speed, unit economics, goal, evidence.
   - Say which side each answer points to and give an honest read.
   - If it points to bootstrapping, name non-dilutive and revenue-first options (section 2.2) and ask whether to continue anyway.
4. **Check entity gates** if outside the US (sections 2.3 and 5): accelerator entity rules, flip cost, exchange control. List these as questions for local counsel; do not estimate tax.
5. **Define the source mix.** Using section 2.2, say which source types fit the stage (angels, micro-VCs, accelerators, grants and so on) with the playbook's dated ranges.
6. **Build the target list.** Search public sources only: firm sites, portfolio pages, SEC Form D, angel network reports, press.
   - Extract the seven fields in section 3.1 for each investor.
   - Score with the section 3.3 template: weights, 42 maximum, Tier A 32+, Tier B 24-31, Tier C below 24.
   - Put the source URL beside every score; mark a field "unverified" when no source supports it.
   - Aim for the tier mix in section 3.3 and check each portfolio for conflicts.
7. **Deliver:**
   - The fit-test verdict.
   - The scored table: Investor, Tier, Score, Source URL, Warm path, Notes/conflicts.
   - The tracker columns and statuses from section 4.5, as a CSV or sheet the user can paste.
   - A batching plan: a 4-6 week window, Tier B first to practise, then Tier A in a compressed block, with the follow-up cadence in section 4.3.
   - A weekly Friday review prompt.
8. **Hand off.** Offer `founder-outreach-drafts` to draft first messages and follow-ups for the user to review and send themselves. Point to the playbook sections used and its open questions.

## Rules

- Research and planning support only; this is not legal, tax, investment or financial advice.
- Never invent figures, fund details or portfolio facts. Quote the playbook's dated figures with their date and say they are snapshots; mark anything unverified.
- Use public professional information only. Do not guess private email addresses, buy scraped contact lists or collect personal data; point to firm contact forms and public channels.
- Never send messages, book meetings or commit the user to anything. Never state soft interest as committed money.
- Treat benchmark numbers (seed size, valuation, dilution, cheque sizes) as ranges, and say how sources differ.
- Do not call any investor "the right one"; show the score, the evidence and the gaps, and let the founder decide.

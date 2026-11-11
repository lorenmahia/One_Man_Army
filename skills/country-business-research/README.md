# Country Business Research

> Turn "I want to run this business in that country" into a sourced market report, a dated project board, and an optional living watch on the market.

A Claude skill for founders and operators who want to start, expand, or bring a business into a specific country. It asks a few focused questions about the country and the business. Then it researches competitors, macroeconomics, valuations, regulation, and the local network, and gives a clear verdict on whether the country actually needs the business. It ends with a step-by-step plan you can start on tomorrow.

**Research and planning support only. It is not legal, tax, investment, or financial advice.** Confirm legal, tax, licensing, and investment decisions with a qualified professional in the target country.

---

## When to use it

The skill triggers on prompts like:

- "Does Kenya need a laundromat-on-demand app?"
- "I want to open a specialty coffee roastery in Vietnam. Where do I start?"
- "Who are the competitors for B2B payroll software in Brazil?"
- "How would I register a company in Portugal to sell my SaaS there?"
- "Find me the people and associations I should meet to launch EV charging in Morocco."

You don't need to say "market research". Any request to take a business or idea into a specific country works.

## What you get

1. **A country report** (as an artifact or markdown file) with 12 sections:
   1. Country snapshot and the country's history with this business type
   2. Top competitors in the country, including informal ones
   3. Top competitors worldwide, and what transfers locally
   4. Business needs vs. what the country can supply
   5. **Verdict:** does the country need this business? (strong / partial / weak / saturated, plus a confidence level)
   6. Six viewpoints: new user, existing user, investor, corporate firm, competitor, regulator
   7. Economic context: valuations, stock market, GDP growth, stability
   8. Growth niches and a recommended beachhead
   9. Networks and key people (public professional figures only)
   10. How to set up the company: entity routes, costs, timelines
   11. Risks and open questions
   12. Action plan
   Every number is sourced and dated, and facts, estimates and inference are labelled.
2. **A project board** with phases (Validate → Legal & setup → Network → Build → Pilot → Launch). Every task has an owner, a real due date, a definition of done, and dependencies. The first seven days are concrete, and there is a go / adjust / stop gate after validation.
3. **Optional extras** (off by default):
   - **Meetings:** proposes meeting slots and creates calendar invites only after you approve them.
   - **Alerts:** notifies you about new competitors, regulation changes, currency or index moves, and funding rounds by calendar, email, or push.
   - **Recurring refresh:** reruns the research on a cadence you choose (weekly by default) and updates the same report and board in place, with a changelog.

## How it works

```
Intake (country, business, needs, stage, situation)
   → Research (web, official stats, filings, exchanges)
   → Report (12 sections + sources)
   → Networks & people
   → Project board
   → [optional] Meetings · Alerts · Loop
   → Deliver: verdict, top 3 findings, next single action
```

The full instructions are in [`SKILL.md`](./SKILL.md), with appendices for the report template, research checklist, six-viewpoint method, networking rules, board format, alerts/loop setup, and company-setup guidance.

## Install

**Claude Code**

```bash
# from the root of this repo
cp -r skills/country-business-research ~/.claude/skills/
```

Restart Claude Code. The skill loads automatically when a request matches.

**Claude.ai / Claude Desktop**

Zip the `country-business-research` folder and upload it under **Settings → Capabilities → Skills**.

## Tools it uses (when available)

| Purpose | Tool |
|---|---|
| Current data | Web search / web fetch |
| Report & board | Artifacts (Docs, Tasks, or Sheets type), falling back to markdown files |
| Macro & market data | Alpha Vantage connector (FX, GDP, CPI, US-listed comparables) |
| Meetings & reminders | Google Calendar connector |
| Alerts & loop | Scheduled tasks, email connector, push notifications |

Missing connectors are suggested, never assumed. Every step has a fallback that works without them.

## Boundaries

- Uses only **public professional information** about people. No home addresses, family details, personal phone numbers, or guessed emails.
- **Never sends** outreach, invitations, or messages without your explicit approval.
- Scheduled runs never contact people or spend money. Anything that needs a decision gets flagged on the board.
- High-risk situations (sanctions, conflict, capital controls, regulated sectors) are flagged at the top of the report.

## License

Same as the rest of this repository.

---
name: country-business-research
description: Country-specific business research and market-entry planning. Asks which country and which business, then researches competitors, valuations, stock market and GDP context, economic stability, local networks and key people, and builds a project board with a dated action plan, optional meeting scheduling, optional alerts, and an optional recurring refresh. Use whenever the user wants to start, expand, or bring a business or business concept into a specific country, asks "does [country] need [business]", wants competitor or market research for a country, wants to find contacts or networks for a venture abroad, or wants to know how to register a company there, even if they never say "market research" or "country analysis". Research and planning support only, not legal or financial advice.
---

# Country Business Research

Turns "I want to do this business in that country" into a researched, structured report, a project board with dated steps, and (if the user wants) meetings, alerts, and a recurring refresh.

**Disclaimer.** This skill gives research and planning support. It is not legal, tax, investment, or financial advice. State this at the top of the report, again next to the company-setup section and the valuation/stock section, and in the project board's notes. Tell the user to confirm legal, tax, licensing, and investment decisions with a qualified professional in that country. Say it plainly and once per place; don't pile on caveats beyond that.

## Why this skill works the way it does

Business ideas fail in new countries mostly because of local facts the founder didn't know: a dominant incumbent, a regulation, a payment habit, a missing supply chain. The workflow therefore goes from country context, to competitors, to whether the country actually needs the business, to how six different parties would see it, to growth niches, to people and actions. The user ends with something they can act on this week, not just a pile of facts. Research is only useful if it is current and sourced, so look things up rather than relying on memory, and mark anything you could not verify.

## Workflow

### 1. Intake: ask before researching

Ask the user to describe the business in detail. A bad guess at intake wastes the whole research run, so ask the questions that matter and skip the ones already answered. Use AskUserQuestion for short multiple-choice items if available; otherwise ask in plain text. Ask at most one round of questions unless something is truly unclear.

Must know:
- **Country** (and region/city focus if relevant). If the user names several countries, ask for a priority order and run one at a time.
- **The business**: what it is, who the customers are, how it makes money, and what the user's version does differently.
- **What the business needs**: capital, licenses, suppliers, tech, talent, physical space, partners, regulatory approvals.
- **Stage**: idea, prototype, running elsewhere, or already operating in that country. Include whether the user has a registered company anywhere.
- **User's situation**: where they live, budget range, time available, and any existing ties to the country (language, family, contacts).
- **Reference models**: any company abroad the idea is modelled on.

Also ask, as optional settings (offer defaults, don't interrogate):
- Do they want **meeting scheduling** (calendar connected)?
- Do they want **alerts** about changes affecting the business? Off by default. If yes, ask which channel(s): calendar reminders, email, push notification, or something else (Slack, text). Then check that the channel is actually connected; if not, offer to set it up (see section 7).
- Do they want the research to **run on a loop**, and how often? Off by default.

If the user answers vaguely, restate your understanding in two or three lines and proceed. They can correct it.

### 2. Research

Follow Appendix B below for what to gather and where. Use WebSearch/WebFetch for anything current. Scale effort to the question: a full country report needs many searches (competitors, macro data, market data, regulation, people), run in parallel where independent. Do the research in the main session when findings shape the next search; fan out only for clearly independent pieces such as separate competitor deep-dives.

Rules for research quality:
- Cite sources with `[Title](URL)` and give the date of the data. Prefer official and primary sources (central bank, statistics bureau, stock exchange, company filings, World Bank, IMF) over blogs.
- Separate **facts**, **estimates**, and **your inference**. Label each.
- If data is missing or unreliable (common for private companies and some countries' statistics), say so and give a range or a proxy rather than inventing a number.
- Never quote more than a short phrase from any source; paraphrase.
- For valuations of private companies, use only publicly reported funding rounds, acquisitions, or filings, and attribute them.

### 3. Build the report

Use the exact structure in Appendix A below. In order:

1. Country snapshot and the country's history with this type of business
2. Competitors in the country (top players, share, pricing, weaknesses)
3. Competitors worldwide (global leaders, how they would or wouldn't transfer)
4. Business needs, matched to what the country can supply
5. Does the country actually need this business? (an explicit verdict with reasoning and a confidence level)
6. Six viewpoints on the business: new user, existing user, potential investor, corporate firm (investor or customer), competitor, regulatory body
7. Economic context: valuations, stock market, GDP growth, economic stability
8. Growth niches inside the country
9. Networks and key people
10. How to set up the company (ways to go)
11. Risks and open questions
12. Action plan (feeds the project board)

Build section 6 from Appendix C below. Each viewpoint should rest on the country evidence you gathered, because a generic persona tells the user nothing they couldn't guess. The viewpoints also feed back into the verdict, the niche choice, the meeting order, and the board's validation tests.

Give a clear verdict in section 5 (for example: strong need / partial need / weak need / already saturated) and say what would change it. A report that never commits to a view isn't useful to someone deciding how to spend money.

Put the report in an artifact so the user can keep, edit, and share it. Call the artifact tool's list-types action first and use the Docs type for the report. If no artifact tool exists, write a `.md` file and send it.

### 4. Networks and people

Follow Appendix D below. Find organizations the user can plug into (chambers of commerce, industry associations, investment promotion agencies, accelerators, diaspora networks, regulators' business desks, trade fairs) and **public professional figures** relevant to the business: founders and executives of competitors and adjacent firms, association officials, investors with public track records, and officials of relevant agencies.

Boundaries: use only publicly available professional information (company sites, press, conference listings, official directories). Do not dig up home addresses, family details, personal phone numbers, or anything about private individuals. For each person give name, role, why they matter, how to reach them through a public or professional channel, and a suggested first message. If the user has saved outreach wording preferences, apply them only where they fit this venture, and never carry over names, websites, or projects that belong to a different venture; use a neutral version and say so in one line.

### 5. Project board

Follow Appendix E below. Build the board as an artifact of the Tasks type (list artifact types first; if Tasks is not offered, use a Sheets artifact, otherwise a markdown checklist file). Each task needs an owner (the user or a named helper), a due date, a clear definition of done, and its dependencies. Phase the work (research validation, legal setup, networking, pilot, launch) and make the first seven days concrete enough to start tomorrow. Anchor dates to today's date and the user's timezone.

### 6. Meetings (optional)

Only if the user wants scheduling and a calendar connector is present (check with ListConnectors via ToolSearch; if none, use SearchMcpRegistry then SuggestConnectors). Propose meeting slots that fit the user's real availability and the contact's likely time zone. Create events or invitations only after the user approves the specific list. Never send outreach or invitations on your own. If no calendar is connected, give the proposed schedule in the board and draft the messages so the user can send them.

### 7. Alerts (optional, off by default)

Follow Appendix F below. Alerts mean: when something material changes (a new competitor entering, a regulation change, a currency shock, a funding round, an index move beyond a threshold the user sets), the user hears about it. Ask which triggers and which channel, then make sure the channel's connection exists (load ListConnectors via ToolSearch; if it is missing, run SearchMcpRegistry with keywords for the service, then SuggestConnectors so the user can connect it in one click, and wait for them to finish). Implement through a scheduled task (create_trigger) that re-checks the watch-list and notifies via the chosen channel: calendar reminder, a drafted email, or push notification. Confirm the settings back to the user in one sentence. Turning alerts off must be as easy as turning them on.

### 8. Continuous loop (optional)

If the user wants it, set up a recurring scheduled task that reruns the research on the cadence they choose (weekly is a sensible default; avoid daily unless asked, since most of this data doesn't move that fast) and **updates the existing artifacts in place** rather than creating new ones. Each run should append a short "What changed since last run" entry at the top of the report, mark board tasks that have become stale or newly urgent, and send an alert only if an alert trigger fired. Details are in Appendix F below. Tell the user how to pause or stop the loop.

### 9. Company setup guidance

Follow Appendix G below. If the user has no company, explain the realistic routes: register a local entity in the target country, register a foreign entity or branch, register in the home country and export or partner in, use a local partner/franchise/distributor, or test first with no entity (marketplace, contractor, or agent). For each route give what it is, typical steps, rough time and cost ranges (sourced for the specific country, with the date), pros and cons, and which fits the user's stage and budget. Include foreign-ownership limits, licensing for the specific business type, tax registration, and banking. This is information to help the user ask better questions of a local lawyer, accountant, or the country's business registry. It is not advice, so say that, and name the official registry or investment agency where they can confirm.

### 10. Deliver

Finish with a short message: the verdict, the three most important findings, where the report and board are, and the next single action. Offer the optional pieces (meetings, alerts, loop) that the user hasn't switched on yet, in one line. Do not recap the steps you took.

## Handling edge cases

- **Country has weak or contested data**: use regional proxies, say why, and widen ranges.
- **Sanctions, conflict, or heavy capital controls**: flag at the top of the report; these change what is possible and legal, and the user needs local counsel early.
- **Regulated businesses** (finance, health, telecom, education, food, alcohol, crypto): put licensing first in the plan, because it often decides feasibility.
- **User already operating there**: skip setup basics, spend the effort on competitors, niches, and networks.
- **Very large ask** (many countries): do one country fully, then offer the next, rather than a thin pass over all.

---

## Appendix A: Report structure

Use these headings in this order. Open with a three-line summary box (verdict, biggest opportunity, biggest risk) and the disclaimer line: *Research and planning support only; not legal, tax, investment, or financial advice.*

Each section ends with a one-line "So what for this business".

### 1. Country snapshot and history with this business type
- Population, language(s), urbanisation, income levels, internet/mobile/payment penetration, currency, ease-of-doing-business indicators.
- History: when this kind of business first appeared in the country, who tried it, what succeeded or failed and why, notable exits or shutdowns, policy changes that opened or closed the space.

### 2. Top competitors in the country
Table: company, founded, what they offer, scale (users/revenue/locations, with source), pricing, funding or ownership, strengths, weaknesses, and the gap they leave. Include informal competition (street vendors, family firms, WhatsApp traders), because they often are the real competition. Add a short "how they would react" note.

### 3. Top competitors in the world
Table of 3-6 global leaders: what they do best, why they have or have not entered this country, and what from their model transfers. Say where global playbooks break locally (payments, trust, logistics, regulation, price points).

### 4. Business needs vs the country
Take each need identified at intake (capital, licences, suppliers, talent, tech, space, partners) and rate the country: readily available / available with effort / scarce / unavailable. Name the workaround for each scarce item.

### 5. Does the country actually need this business?
- Evidence of unmet demand (searches, complaints, imports, price gaps, adoption of substitutes).
- Evidence against (saturation, low willingness to pay, regulation, cultural fit).
- **Verdict**: strong need / partial need / weak need / saturated, plus a confidence level (high/medium/low) and what evidence would change it.

### 6. Six viewpoints
Look at the business, in this country, through six pairs of eyes: new user, existing user, potential investor, corporate firm (investor or customer), competitor, regulatory body. Follow Appendix C. Use one short block per viewpoint (what they see, what they want, what would make them say yes, what would make them say no), then a one-table summary of the biggest conflicts and agreements across them. End with the top three changes to the business or plan that the viewpoints imply.

### 7. Economic context
- **Valuations**: public comparables (multiples, market caps) and private deals (rounds, acquisitions) in the sector, locally and regionally. Attribute each number and date it.
- **Stock market**: main index level and trend over 1y/5y, liquidity, sector performance, IPO activity, how it compares to regional peers.
- **GDP growth**: recent and forecast growth, sector contribution; compare with stock market performance (do they move together, is the market ahead of or behind the economy).
- **Stability**: inflation, currency volatility and convertibility, debt and credit ratings, political stability, capital controls, banking health. Give an overall stability rating (stable / moderate / fragile) and the main risk drivers.
- Valuation and market notes are information, not investment advice.

### 8. Growth through niches
List 4-8 niches within the country (customer segments, regions, price tiers, channels, adjacent products). For each: size indicator, competition level, entry difficulty, and why it might suit this business. Recommend a beachhead niche and a sequence of expansion.

### 9. Networks and key people
Organizations first, then people (see Appendix D). Table with name, role, relevance, public contact route, suggested first message, proposed meeting week.

### 10. How to set up the company
Routes, steps, rough costs and timelines for this country, with the official registry and investment agency named. Disclaimer repeated here.

### 11. Risks and open questions
Top risks with likelihood, impact, mitigation. List what you could not verify and how the user could find out.

### 12. Action plan
A summary of the project board: phases, the first seven days, and the key milestone dates. Link to the board.

### Sources
Numbered list of `[Title](URL)` with access date.

### Changelog (loop runs only)
Newest first: date, what changed, what it means.

---

## Appendix B: Research checklist

Start broad, then narrow. Run independent searches in the same turn.

### Country and history
- Search: "[business type] history in [country]", "[business type] market [country] report", "[country] [sector] regulation".
- Sources: national statistics bureau, central bank, ministry of trade/industry, World Bank country page, industry association reports, reputable business press.

### Competitors (local)
- Search the business category plus country, plus app stores/marketplaces, local directories, and local-language terms. Check the local-language name for the category; English-only searches miss incumbents.
- For each: website, press, funding databases (Crunchbase-style summaries on the open web), annual reports for listed firms, regulator registers, app-store download ranges, review sites.
- Look for failures too: "[competitor] shuts down", "exits [country]".

### Competitors (global)
- Identify leaders from analyst coverage and sector press. Check "[company] expansion [region]" and "[company] [country]" for entry attempts and withdrawals.

### Valuation and funding
- Public comparables: listed firms in the sector on the country's exchange and regional peers. Use exchange sites or financial data pages for market cap, P/E, EV/revenue. The Alpha Vantage tools (via ToolSearch) cover US-listed tickers, FX, commodities, GDP, CPI, and treasury yields; use them for global comparables and macro series where the country is covered, and web sources for local exchanges.
- Private: announced rounds, acquisitions, and their reported terms. Mark anything undisclosed as undisclosed.

### Stock market
- Main index level, YTD / 1y / 5y change, top sectors, trading volume, number of listed firms, recent IPOs. Compare with a regional benchmark.

### GDP and stability
- Real GDP growth (last 5 years plus forecast from IMF/World Bank), inflation, policy rate, FX trend vs USD, public debt/GDP, sovereign rating, current-account balance, political risk assessments. Compare market return with GDP growth and say what the gap implies.

### Regulation and setup
- Business registry, investment promotion agency, tax authority, sector regulator, foreign-ownership rules, minimum capital, licence fees, typical timelines, visa/residence for founders.

### Demand evidence
- Import data, price comparisons, search interest, complaints and reviews of existing services, government strategy documents naming the sector, donor or development-bank programmes.

### Quality bar before writing
- Every number has a source and a date.
- Conflicting figures are shown as a range with both sources.
- Anything older than two years on a fast-moving topic is flagged.
- Unverified items go in "Open questions".

---

## Appendix C: Six viewpoints

A business that works for the founder's spreadsheet can still fail because one party never says yes. Seeing it through each party's eyes exposes those gaps before money is spent. Ground every viewpoint in the country's evidence from the research (real behaviours, prices, rules, deals), not generic personas. Where evidence is thin, say so and mark the point as an assumption to test.

For each viewpoint write four short parts: **What they see**, **What they want**, **What gets a yes**, **What gets a no**. Then add one **Test**: a cheap action on the project board that checks the point (an interview, a pilot offer, a pre-meeting with a regulator's help desk).

### 1. New user (first-time customer)
- How they would find out about the business in this country (channels, language, trust signals, word of mouth).
- Barriers to the first purchase: price vs local income, payment methods, data costs, literacy, trust, delivery, onboarding effort.
- What the first five minutes and first week must feel like. What makes them try versus stay with the informal or incumbent option.

### 2. Existing user (current customer, once the business is running; before launch, the users of the closest competitor)
- Why they stay or churn: reliability, price changes, support, switching costs, loyalty to people not brands.
- What they would pay more for, what they would complain about publicly, what they would recommend.
- Signals the business should track (retention, repeat rate, referrals, complaints).

### 3. Potential investor (angel, VC, development-finance, local family office)
- Who actually invests in this sector and stage in the country; typical cheque sizes, terms, and exit routes (local listing, regional acquirer, buyback).
- What they check: market size credibility, team and local presence, unit economics, regulatory risk, currency risk and repatriation of returns.
- Likely objections and the evidence that would answer them. Comparable deals, from the valuation research.
- Information only, not investment advice.

### 4. Corporate firm (invest in it, partner with it, or buy its services)
- Which large local or regional firms would care: banks, telcos, retailers, distributors, manufacturers, and the global firm entering the market.
- Corporate-as-customer: procurement hurdles, vendor registration, payment terms, pilot-to-contract path, compliance requirements.
- Corporate-as-investor or acquirer: strategic fit, build-vs-buy logic, what they would want in a partnership (exclusivity, data, control).
- Who inside such firms makes the decision, in role terms. Use public professional figures only.

### 5. Competitor
- How each main competitor (formal and informal, local and global) sees the newcomer: ignore, copy, undercut, lock up suppliers or distributors, lobby, partner, or acquire.
- Their cost and distribution advantages and how fast they can respond.
- Where the newcomer is hard to copy (data, network, licence, brand, local relationships) and where it is easy.
- Plan for the likely first response.

### 6. Regulatory body
- Which regulators and agencies touch the business (sector regulator, central bank, tax authority, competition authority, data-protection authority, consumer agency, local government), and what each cares about.
- How they would classify the business, which licence or approval applies, how long it usually takes, known enforcement patterns, recent or pending rule changes.
- What makes them comfortable (consumer protection, local ownership, taxes paid, data localisation, reporting) and what triggers scrutiny.
- Confirm with the agency or a local professional. Not legal advice.

### Synthesis
After the six blocks:
1. A matrix: rows are the six viewpoints, columns are "Supports", "Blocks", "Needs from the business".
2. The conflicts that matter most (for example regulators want local ownership while investors want control).
3. The top three changes to the product, pricing, structure, or sequence that the viewpoints imply.
4. Feed the Tests and changes into the project board, with dates.

### Using the viewpoints elsewhere
- Verdict (section 5): lower your confidence if any one viewpoint is a hard block.
- Niches: prefer niches where several viewpoints align.
- Meetings: choose first meetings that speak to the weakest-evidenced viewpoint.
- Loop: on each refresh, recheck what changed for each viewpoint (a new rule, a competitor move, a funding round) and note it in the changelog.

---

## Appendix D: Networks and people

### Organizations to find
- Chambers of commerce (national, bilateral such as home-country-to-target-country, and city level)
- Industry and trade associations for the specific sector
- Investment promotion agency and any special economic zone authority
- Accelerators, incubators, and angel/VC networks active in the sector
- Diaspora and alumni networks from the user's home country or university
- Government business-support desks and relevant regulator liaison offices
- Trade fairs and conferences (dates, location, cost, who attends)
- Supplier, distributor, and logistics bodies the business depends on

For each: what it offers, membership cost or entry route, upcoming events, and how it helps this specific business.

### People to find (public professional figures only)
Categories: founders and senior staff at competitors and adjacent firms, association and chamber leaders, investors with a public track record in the sector, officials of the relevant agency or regulator, academics or analysts who publish on the sector, and potential local partners (distributors, franchisees).

For each person record:
- Name, role, organization
- Why they matter to this business (specific)
- A public source for the information (link)
- Best public or professional channel (company contact page, professional network, conference speaker listing, association directory)
- Suggested first message (short, specific, with one clear ask such as a 20-minute call)
- Proposed meeting window

### Boundaries
- Use information the person or their organization has made public in a professional context.
- Do not collect home addresses, family details, personal phone numbers, or private-life information, and do not profile private individuals.
- Do not guess email addresses. Use published contact routes.
- Do not send messages or invitations without the user's approval.
- If the user has saved outreach wording preferences, use them only where they fit this venture. Never carry over names, websites, or projects that belong to a different venture (a saved opener that introduces another product would mislead the recipient). If a saved opener doesn't fit, use a neutral version and say so in one line.

### Meeting schedule
Spread outreach across weeks, starting with the highest-leverage and easiest introductions (associations, diaspora networks) before cold approaches to competitors' executives. Account for time zones, public holidays in the target country, and local business hours and customs. Show the schedule on the project board; create calendar events only after approval.

---

## Appendix E: Project board

Goal: the user opens the board and knows exactly what to do next and by when.

### Format
Call the artifact tool's list-types action first. Use the Tasks type if offered. Otherwise a Sheets artifact with the columns below, otherwise a markdown checklist file.

### Phases (adapt to the business)
1. **Validate**: confirm demand, interview 5-10 potential customers, verify the key assumptions from the report, and run the "Test" action from each of the six viewpoints (new user, existing user, investor, corporate, competitor, regulator).
2. **Legal and setup**: choose the entity route, licences, tax registration, bank account, trademarks.
3. **Network**: join the organizations, book the meetings from the people list.
4. **Build or adapt**: product/service localisation, suppliers, pricing, payments.
5. **Pilot**: smallest real launch in the beachhead niche, with a success metric.
6. **Launch and grow**: expand through the niche sequence from the report.

### Task fields
- Title (verb first)
- Phase
- Owner (user, or a named role such as local lawyer, accountant)
- Due date (real date)
- Definition of done (observable)
- Depends on
- Est. effort and cost
- Notes / links to report sections and sources

### Rules
- The first seven days must be specific enough to start tomorrow: who to contact, what to prepare, what to decide.
- Put professional-advice tasks (hire a local lawyer, confirm tax treatment with an accountant) explicitly on the board. Do not pretend the board replaces them.
- Include meeting tasks from the people list with proposed dates; mark them "proposed" until the user approves and invitations are created.
- Add milestone dates and a decision gate after Validate: "Go / adjust / stop", with the criteria written down in advance.
- Include a notes line: "Planning support only, not legal or financial advice."
- On loop runs, edit the existing board: mark stale tasks, add newly relevant ones, and note changes at the top. Do not rebuild it.

---

## Appendix F: Alerts, connecting channels, and the loop

Both are off unless the user asks. Ask once, explain what each does in one sentence, and honour a no.

### Tools
- Scheduled tasks: load `create_trigger`, `list_triggers`, `update_trigger`, `delete_trigger` via ToolSearch. Call them "scheduled tasks" when speaking to the user.
- Calendar: Google Calendar tools via ToolSearch for reminders and meetings.
- Email: only if a mail connector is present; otherwise draft the message text.
- Push: PushNotification via ToolSearch where available.
If a needed connector is missing, say so, use SearchMcpRegistry and SuggestConnectors, and fall back to what works (for example, alerts as calendar reminders or a section at the top of the report).

### Connecting a channel
Never assume a channel works. For each channel the user picks: check connected tools first (ListConnectors). If it isn't connected, call SearchMcpRegistry with a few keywords (for example ["gmail","email"], ["google calendar","calendar"], ["slack"]), then SuggestConnectors with the matches so the user can connect in one click. If nothing matches, say so and fall back to calendar reminders (if Calendar is connected) or a "Needs your attention" block at the top of the report. After connecting, send one test notification only if the user agrees, so they know it works.

### Alerts
1. Ask which triggers matter. Offer: new competitor or exit, regulation or tax change, currency move beyond X%, main index move beyond X%, funding round or acquisition in the sector, new incentive or grant, political or security events, a deadline on the board approaching.
2. Ask the channel: calendar reminder, email, or push. Ask how often to check (default weekly).
3. Create a scheduled task whose prompt is fully self-contained: country, business summary, watch-list with thresholds, artifact links, channel, and the instruction to notify only when a trigger fires and to stay quiet otherwise.
4. Confirm settings in one sentence and say how to change or stop them.

### Recurring refresh (loop)
1. Ask cadence (weekly default; monthly for slow-moving topics; avoid daily unless asked).
2. Create a scheduled task whose prompt contains: the intake summary, artifact links, the report structure (Appendix A), and these steps: rerun the research for sections whose data changes (competitors, valuations, stock market, GDP/stability, news on regulation and people), check what changed for each of the six viewpoints, compare with the current report, edit the existing artifacts in place, add a dated entry to the Changelog and the top of the board, mark stale or newly urgent tasks, and send an alert only if an alert trigger fired.
3. Each run must keep sources and dates current and must never create duplicate artifacts.
4. Tell the user how to pause or delete the loop. Offer to list it with list_triggers on request.
5. Scheduled runs are unattended: no questions mid-run. If something needs a human decision, record it at the top of the board as "Needs your decision" instead.

### Restraint
- Alerts should be rare and meaningful; a noisy alert gets ignored.
- Never send external messages, create meetings with other people, or spend money from a scheduled run without prior explicit approval.

---

## Appendix G: Company setup guidance

Information to help the user ask better questions of professionals. It is not legal, tax, or financial advice. Say so in the section and point to the official body to confirm each point.

### Ask first
Does the user already have a company anywhere? Where do they live and pay tax? Will they be physically in the target country? Do they need local investors or a local bank account? What is the budget and timeline? Is the business regulated?

### Routes to explain (for the specific country)
1. **Local entity** (for example a private limited company): steps, minimum capital, residency or local-director requirements, foreign-ownership limits, time, government fees, ongoing compliance.
2. **Branch or subsidiary of a foreign company**: when it fits, differences in liability and tax.
3. **Home-country company that sells into the country**: export, cross-border services, cross-border tax and VAT/GST consequences.
4. **Partnership routes**: local partner, distributor, franchise, joint venture, licensing. Risks around control, IP, and exit.
5. **Test without an entity**: marketplace sales, freelancers or agents, pilot with a local partner's licence. Limits and legal risks of operating unregistered.
6. **Special zones and incentives**: free zones, tech parks, startup visas, tax holidays, grants.

### For each route give
What it is, steps in order, rough cost and timeline (sourced and dated for this country), pros, cons, and which user situations it suits. Recommend a shortlist of two routes with reasoning, framed as "options to discuss with a local professional".

### Always cover
- Business-type licences and permits
- Tax registration and what taxes typically apply
- Banking and moving money in and out, including capital controls
- Intellectual property and trademark registration
- Employment rules for first hires and founder visas
- Data protection and consumer rules that apply to the business
- Who to hire: local lawyer, accountant, registered agent; what to ask them

### Where to confirm
Name the country's business registry, investment promotion agency, revenue authority, and sector regulator, with links.

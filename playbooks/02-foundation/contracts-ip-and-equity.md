# Contracts, IP and Equity: The Legal Paperwork a New Company Needs

> Last verified: 2026-11-11. Research and planning support only; not legal, tax, investment or financial advice.

## Summary

- **Fact:** Founder shares, a signed founder IP assignment and (in the US) a timely 83(b) election are the three cheapest things to do on day one and among the most expensive to fix later. The 83(b) deadline is 30 days from transfer with no extension.
- **Fact:** Missing or defective IP assignment (founder pre-incorporation work, contractors with no written assignment) is repeatedly named by law firms as a leading diligence failure. See section 2.
- **Fact:** As of 2026-11-11 US law requires human authorship for copyright (Supreme Court declined to review `Thaler v. Perlmutter`, 2026-03-02); AI-assisted work is judged case by case. UK and EU positions are less settled.
- **Inference:** A solo founder needs, in priority order: customer terms, a contractor agreement with IP assignment, a privacy policy/DPA, and a trademark check. NDAs matter less than most first-time founders think.
- **Fact:** Free open templates exist (Common Paper under CC BY 4.0, Cooley GO, others) but none replace a lawyer for equity, IP assignment or any contract with real liability exposure.

---

## 1. Founder equity for a solo founder

**Not legal advice. Confirm with a qualified lawyer and tax adviser in your jurisdiction.**

### 1.1 Founder shares and vesting

- **Fact:** On incorporation, the founder is issued founder stock (US) or ordinary shares (UK/EU) in exchange for cash, assets or IP. Issue the shares in writing with a stock purchase agreement, a board consent and a ledger entry; do this at formation, before any outside money.
- **Fact:** The common convention is four-year vesting with a one-year cliff: nothing vests for 12 months, 25% vests at the cliff, then roughly 1/48 monthly ([Y Combinator, "How to Split Equity Among Co-Founders"](https://www.ycombinator.com/blog/splitting-equity-among-founders), seen via search snippet; consistent with [Stripe, "Founder vesting"](https://stripe.com/resources/more/founder-vesting), opened 2026-11-11; Stripe's page is vendor marketing for Stripe Atlas).
- **Fact:** Vesting exists mainly to protect co-founders and investors if someone leaves. Neither source I opened addresses solo founders directly; Stripe's page says vesting is optional without outside investors.
- **Inference:** Why investors still ask a sole founder to vest: they are betting on one person staying. A re-vesting clause (for example 25-50% of shares subject to vesting from the financing date) is a common negotiation outcome. I did not find a primary source quantifying this; treat as practitioner convention and raise it with a lawyer.
- **Inference:** Vesting a sole founder's own shares before any investor appears is a choice. Benefits: shows seriousness, and makes a later hire or co-founder grant look consistent. Cost: some paperwork and, in the US, the need for an 83(b) election.
- Acceleration (single or double trigger) is a negotiated term; ask the lawyer how it interacts with a future acquisition.

### 1.2 83(b) election (US)

- **Fact:** An 83(b) election lets you pay tax on restricted stock at its value at grant (often near zero for founders) instead of as it vests. The Treasury regulation requires the election be filed no later than 30 days after the property is transferred ([26 CFR 1.83-2](https://www.law.cornell.edu/cfr/text/26/1.83-2), found via search snippet, not opened in full).
- **Fact:** The IRS released a standardized [Form 15620, Section 83(b) Election](https://irs.gov/pub/irs-pdf/f15620.pdf) (my fetch showed "Rev. 4-2025" but the PDF body was not machine-readable, so I could not verify its instructions from the primary source). Law-firm alerts say the form is optional and a self-drafted election remains valid ([Cozen, 2024](https://www.cozen.com/news-resources/publications/2024/irs-creates-standardized-section-83b-election-form-15620); search snippet only).
- **Fact:** The 30-day window has no extension even with the new form, per the same alerts (search snippets). Practitioners say the clock starts at the transfer date, often the share issuance date, not the date you signed.
- **Conflict flagged:** One 2026 vendor blog says the form can be submitted online since July 2025; older commentary says mail only. I could not confirm online filing against an IRS page. See Open questions.
- **Fact:** A copy goes to the service recipient (the company) per the commentary I saw. Keep proof of mailing (certified mail with receipt is the usual advice).
- **Fact:** Revocation requires IRS consent (26 CFR 1.83-2(f), via search snippet).
- **Inference:** If you issue unvested shares to yourself, put the 30-day deadline in your calendar the day you sign. Outside the US, equivalent tax elections differ (for example UK Section 431 elections); ask an adviser.

### 1.3 Advisor and early-hire equity ranges

All figures are Carta data. **Bias flag:** Carta sells cap-table software and publishes this data for marketing; sample composition (US, venture-backed, Carta customers) skews toward funded startups, which may not match a bootstrapped solo company.

| Role | Figure | Source and date |
|---|---|---|
| Pre-seed advisor | Median about 0.24% fully diluted; about 64% got under 0.3%; about 1 in 10 reached 1% | [Carta, 2025](https://carta.com/data/linkedin-pre-seed-advisor-equity-0-24-percent/) (search snippet; page returned 403 on fetch) |
| Advisor by stage (H1 2024) | 0.21% pre-seed, 0.12% seed, 0.05% Series A | [Carta advisory shares guide](https://carta.com/sg/en/learn/startups/equity-management/advisory-shares/) (snippet; data over 2 years old by 2026 end of H1 2024 is about 2.4 years: **flag**) |
| Advisor typical range | 0.1% to 1% | [Carta, Oct 2025](https://carta.com/uk/en/learn/startups/founding-team/advisor/) (snippet) |
| First engineer | Median 1.54% (two years to Dec 2025); one secondary summary gives middle-50% about 0.61% to 4.13% | [Carta, Dec 2025](https://carta.com/data/linkedin-founding-engineer-equity-1-54-percent/) (snippet); [Cortance](https://cortance.com/answers/hiring-team/what-is-a-typical-equity-range-for-early-stage-engineers-in-2026-startups) (secondary) |
| First hire, cross-sector | Median about 1.4% to 1.5% | [Carta, July 2025](https://carta.com/data/linkedin-first-hire-equity-benchmarks-by-sector/) (snippet) |
| Later hires | About 0.85% (second), about 0.33% (fifth) | [SaaStr summary of Carta State of Seed](https://www.saastr.com/how-much-equity-to-give-your-first-employees-the-real-data-from-50000-startups) (secondary) |

- **Range note:** advisors cluster at 0.1% to 1%; first-employee grants range about 0.6% to 4%, median near 1.5%.
- **Inference:** For a solo bootstrapped founder, use these as sanity checks, not entitlements. Vest advisor grants (commonly over 1-2 years) and tie them to defined help.

### 1.4 Option pool basics

- **Fact:** An option pool is a block of shares reserved for future employee and advisor grants. Carta reports a median seed-stage pool of 11.8% after the round, from 15,000+ startups over five years ([Carta option pool guide](https://carta.com/blog/how-to-size-employee-option-pool/), search snippet; a secondary site cites 12.1% from Carta's 2026 report, unverified). Carta's rule of thumb is 10-20% including allocated and unallocated options.
- **Fact:** Where the pool sits matters: a pool created pre-money dilutes existing holders (you); post-money dilutes new investors too ([Carta, snippet](https://carta.com/uk/en/learn/startups/equity-management/option-pool/)). Carta also publishes cautionary pieces on the "option pool shuffle" and on 20% requests ([Carta](https://carta.com/data/linkedin-option-pool-founders-push-back-20-percent/); snippet).
- **Inference:** Do not create a large pool before you have a financing or a hire to justify it; size it to a 12-18 month hiring plan.

### 1.5 Cap table hygiene and tools

- Keep one source of truth: share ledger, board consents, signed grants, 83(b) proof, and a fully diluted table including SAFEs and notes.
- Tools (options only; vendor claims unverified): Carta, Clerky, Stripe Atlas, Capbase, Pulley, or a spreadsheet at the earliest stage. Self-serve tools can cover formation and first documents ([Carta law-firm guide](https://carta.com/learn/startups/founding-team/law-firms/), snippet). Cheap formation can create cleanup cost later (law-firm blogs; vendor-biased either way).

**So what for a solo founder:** Issue your shares in writing at formation, decide whether to vest them, and if you do (US), file the 83(b) within 30 days; keep advisor grants small, vested and written.

---

## 2. Intellectual property

**Not legal advice. IP ownership rules differ by country; confirm with a qualified IP lawyer in your jurisdiction.**

### 2.1 Founder-to-company IP assignment

- **Fact:** Goodwin states that founders still owning IP created before incorporation is among the most common IP gaps found in diligence; the fix is a document where the founder "hereby assigns" relevant IP to the company ([Goodwin, Nov 2022](https://www.goodwinlaw.com/publications/2022/11/11_03-top-10-commercial-ip-tips-for-startups), opened). Date is about 4 years old, but the principle is stable.
- **Fact:** A second source (vendor blog, April 2026) says incorporation does not move pre-existing work to the company, and that investors check chain of title, signed invention assignments and contractor assignments ([OneGC, 2026-04-14](https://onegc.com/blog/ip-assignment-for-startups), opened; vendor sells legal services; its dollar figures are illustrative, not data).
- **Inference:** Do it as part of the founder stock purchase, listing code, domains, designs, brand names and social accounts. Check any employer agreement you signed before founding; a prior employer may claim your work.

### 2.2 Contractor and employee invention assignments

- **Fact:** Under English law, employees' work in the course of employment generally belongs to the employer, but contractors generally own what they create unless agreed otherwise (Goodwin, above). US sources say the same for most contractor-written software; "a purchase order is not an assignment" (OneGC, above).
- **Fact:** Some US states limit what employers can claim; OneGC cites California Labor Code section 2870 (secondary, unverified here).
- **Fact:** US trade-secret law requires a whistleblower-immunity notice in agreements with employees and contractors that govern confidential information, or the company can lose certain damages against the individual ([Jones Day](https://www.jonesday.com/en/insights/2016/05/federal-defend-trade-secrets-act-imposes-new-notice-obligations-on-employers), 2016, snippet; see 18 U.S.C. 1833(b) and confirm). Sources differ on whether to amend older agreements; ask counsel.
- **Inference:** Sign the assignment before work starts, in the same document as the contractor agreement; assign "present" rights, list background IP the contractor keeps (with a licence to you), and obtain a signed assignment from anyone who already contributed.

### 2.3 Open-source licence hygiene

- **Fact:** Permissive licences (MIT, BSD, Apache-2.0) carry notice obligations; copyleft (GPL, AGPL, and with conditions LGPL, MPL) can require sharing source depending on use. AGPL covers network use, so the usual "SaaS is not distribution" reasoning does not protect you ([Promise Legal](https://blog.promise.legal/startup-central/open-source-license-compliance-for-startups/); Goodwin above for the GPL/SaaS point). Both sources are law-firm or practitioner blogs, not primary licence texts.
- **What to track:** an inventory or SBOM of dependencies with licence, version, whether modified, and whether distributed or only hosted; a short policy (for example pre-approved permissive, review for LGPL/MPL, block GPL/AGPL without sign-off, per Promise Legal's example tiering); attribution files.
- **Inference:** Add licence scanning to CI early. Acquirers and investors commonly audit it.

### 2.4 Ownership of AI-generated code and content

**Conflicts and uncertainty are material here; the topic is fast-moving, so anything older than two years is flagged.**

- **Fact (US):** The Copyright Office's Part 2 report (published 2025-01-29) concludes that prompts alone generally do not give enough control to be authorship, purely AI-generated material is not protectable, and human contribution is assessed case by case; it recommended no new legislation ([Copyright Office AI page](https://www.copyright.gov/ai/), opened; conclusions via law-firm summaries such as [Copyright Alliance](https://copyrightalliance.org/ai-report-part-2-copyrightability/), snippet).
- **Fact (US):** The D.C. Circuit held that copyright requires a human author; the Supreme Court denied certiorari in `Thaler v. Perlmutter` on 2026-03-02 ([Holland & Knight, March 2026](https://www.hklaw.com/en/insights/publications/2026/03/the-final-word-supreme-court-refuses-to-hear-case-on-ai-authorship), snippet). A denial is not an endorsement of the reasoning, and how much human input suffices was left open. A related case, `Allen v. Perlmutter` (D. Colo.), was reported pending.
- **Fact (UK):** Section 9(3) of the Copyright, Designs and Patents Act 1988 gives computer-generated works a 50-year term. A government report published 2026-03-18 proposed removing it for works without a human author, while keeping protection for AI-assisted works; no bill or commencement date was found ([HSF Kramer, March 2026](https://www.hsfkramer.com/notes/ip/2026-03/uk-government-report-on-copyright-and-ai-concludes-more-evidence-is-needed-although-s9-3-cdpa-could-go), snippet; [RPC, June 2026](https://www.rpclegal.com/snapshots/technology-digital/summer-2026/uk-governments-report-on-copyright-and-ai/), snippet).
- **EU and other jurisdictions:** I did not find a sourced current statement; see Open questions.
- **Inference:** Treat purely AI-generated code and assets as possibly unprotectable and not exclusive; keep human authorship (design, selection, editing) and records of it; check your AI tool's terms on output ownership and indemnity; open-source licence contamination from model output is a separate unresolved risk.

### 2.5 Trade secrets

- **Fact:** Protection depends on taking reasonable measures to keep information secret (access controls, confidentiality clauses, need-to-know) ([Barnes & Thornburg / BIPC on the DTSA](https://www.bipc.com/how-the-defend-trade-secrets-act-of-2016-affects-employers-and-what-you-need-to-do-now), 2016, snippet; old but the statute is unchanged as far as I found).
- **Inference:** Mark confidential material, limit repo and customer-data access, offboard accounts promptly, and keep confidentiality terms in every contractor and customer contract.

**So what for a solo founder:** Sign a founder IP assignment to the company now, get a written assignment from every contractor before they start, track open-source licences from day one, and do not rely on AI-generated output as protectable IP.

---

## 3. Trademarks and domains

**Not legal advice. Clearance judgement calls belong with a trademark attorney.**

- **Common-law rights:** In many jurisdictions (US, UK) unregistered use can create rights in the area of use, and a prior unregistered user can challenge your registration. The USPTO database shows registrations and applications only, so it is not a full clearance search; search state records, domains, app stores, social handles and general web too (search snippet summary: [Waltmire](https://www.waltmire.com/?p=1389) and others; law-firm and vendor pages, treat as practitioner views). Use ™ for unregistered and ® only after registration.
- **Naming checks:** search the exact name, phonetic variants and translations, in your goods/services class and neighbouring classes; check domain, handle availability, and app-store names; avoid names confusingly similar to bigger players.
- **Domains and handles:** register the .com or main national domain plus obvious variants, and the main social handles, using a company-owned account (not personal email) with 2FA and registrar lock. Confirm domains are listed in the founder IP assignment.

### Filing offices (fees are per official pages where noted)

| Office | Fee (one class) | Notes |
|---|---|---|
| UKIPO | GBP 205 online, plus GBP 60 per extra class; Right Start GBP 125 plus GBP 30 per extra class | [GOV.UK, opened 2026-11-11](https://www.gov.uk/how-to-register-a-trade-mark/start-your-application); increase effective 2026-04-01 per [CITMA](https://www.citma.org.uk/resources/the-countdown-to-new-uk-ipo-fees-mb26.html) (opened). Applications are published on GOV.UK as soon as filed. |
| EUIPO | EUR 850 online for one class; second class EUR 50; third and later EUR 150 each | [EUIPO fees page](https://www.euipo.europa.eu/en/trade-marks/before-applying/fees-payments) (search snippet; page not opened). Fee due within one month of filing. |
| USPTO | Base application USD 350 per class; surcharges apply (for example for free-text goods descriptions or incomplete information) | [USPTO summary of 2025 fee changes](https://www.uspto.gov/trademarks/fees-payment-information/summary-2025-trademark-fee-changes) (could not open; snippet and law-firm summaries only). **Conflict:** the USPTO page snippet gives 2025-02-18 as the effective date; most law firms say 2025-01-18. Check the live fee schedule. |
| WIPO Madrid | Basic fee CHF 653 (black and white) or CHF 903 (colour), plus CHF 100 per designated member (or its individual fee) and CHF 100 per class above three | [WIPO fees page](https://www.wipo.int/en/web/madrid-system/how_to/file/fees) (opened). Conceptually: one international application based on a home-country mark, designating several members. Madrid dependency on the basic mark and timelines: not verified here. |

- **Timelines:** GOV.UK page I opened did not state a total time (a secondary source says about 3-4 months if unopposed; unverified). USPTO and EUIPO timelines were not verified. Do not plan around a specific date.
- **Inference:** File first in the market where you sell or fundraise, then consider Madrid when expansion is real; fees are non-refundable if the mark is refused (EUIPO statement via snippet).

**So what for a solo founder:** Do a free knock-out search and a domain/handle check before you commit to a name, register the domain and handles at once, and file a trademark in your home market once the name is stable and you can afford a clearance review.

---

## 4. Contracts a startup actually needs

**Not legal advice. Templates are starting points; confirm with a qualified lawyer in your jurisdiction. Do not paste template text blindly.**

### 4.1 Open template sources and their limits

| Source | Licence / terms | Jurisdiction and limits |
|---|---|---|
| [Common Paper standards](https://commonpaper.com/standards/) | Free to use and modify under CC BY 4.0 (page, opened) | Not a law firm; no legal advice; no jurisdiction stated on page. Catalogue includes mutual NDA, Terms of Service, Cloud Service Agreement, DPA, Professional Services Agreement, SOW, Order Form, Independent Contractor Agreement, AI Addendum. |
| [Cooley GO](https://www.cooleygo.com/should-you-require-a-signed-nda-from-a-potential-investor/) | Page shows "All rights reserved" (opened); no open licence stated | Terms-of-use generator was described as for US companies; a UK version exists (search snippet). Cooley says its general forms probably need customisation. |
| Bonterms | Reported as free to use; at least one document labelled CC BY ND by a third party (unverified; check each document) | Does not give legal advice or guarantee enforceability (secondary snippet). |
| Orrick, Y Combinator, Stripe Atlas guides | Not verified in this research | Check each site's terms and the document's jurisdiction before use. |

### 4.2 Priority order

1. **Customer terms (SaaS terms or master services agreement).**
   - Purpose: define what you sell and cap your risk.
   - Understand: liability cap, indemnity (especially IP indemnity), IP ownership of your product versus customer data, term and termination, payment terms, governing law and venue, SLA promises, data-protection terms.
   - Negotiate vs accept: accept mutual 12-months-fees as the general cap; negotiate any super-cap for data breach and confidentiality, and resist uncapped indemnity ([cloudnuro](https://www.cloudnuro.ai/blog/saas-liability-cap) and [Causo](https://hub.causo.ai/guides/saas-contract-negotiation-clauses-founders-2026); vendor blogs, search snippets). Multiples such as 2x-3x are conventions, not measured market data. Do not accept customer-friendly IP terms that transfer your product IP.
2. **Order form / cover page.** Purpose: deal-specific terms (price, term, auto-renewal, notice period) on top of standard terms. Negotiate price and term; keep legal terms in the standard document.
3. **NDAs.** Useful for sharing sensitive material with a customer, partner or contractor and for narrow, core, unpatented IP. Cooley GO advises against asking VCs to sign NDAs early, since they nearly always refuse and it can look inexperienced; share sensitive detail later and in stages ([Cooley GO, last reviewed June 2023](https://www.cooleygo.com/should-you-require-a-signed-nda-from-a-potential-investor/), opened; over two years old, but the norm is stable). Red flags in an NDA someone sends you: very long term, non-compete or non-solicit, residuals clause missing, one-way obligations only on you, or a definition of confidential information that sweeps in everything.
4. **Contractor agreement.** Purpose: scope, payment, IP assignment, confidentiality, independent status. Key: present-tense IP assignment, background IP schedule, termination, no authority to bind. Accept the contractor's reasonable payment terms; never accept a contractor retaining ownership of core code.
5. **Statement of work (SOW).** Deliverables, acceptance criteria, milestones, fees. Accept a fixed-scope SOW; avoid vague "as needed" work with no acceptance test.
6. **DPA and privacy policy.** If you handle personal data for customers, you are usually a processor, and UK/EU GDPR requires a written contract with required terms (security measures, sub-processor authorisation, audit cooperation, deletion or return at end) ([ICO guidance on contracts](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/accountability-and-governance/guide-to-accountability-and-governance/contracts/), snippet summary; see the primary page for the full Article 28(3) list). Pointer: the repo skill `data-protection-readiness`.
7. **Website terms of service.** Disclaimers, acceptable conduct, IP, limitation of liability, governing law. Make sure the acceptance mechanism (click-through) is real; terms bound by a footer link alone are weaker (general practitioner view; not verified here).
8. **Acceptable-use policy.** Prohibited conduct and your right to suspend. Accept standard prohibitions; tailor for AI features, scraping and abuse.
9. **Refund policy.** Consumer law may override your policy in some countries (for example statutory cooling-off rights); check local rules. Keep it short and consistent with checkout and Stripe/payment-processor terms.

### 4.3 Clauses to understand in everything you sign

- **Liability cap:** how much you can lose; check carve-outs (confidentiality, data breach, indemnities, gross negligence).
- **Indemnity:** who pays if a third party sues, especially IP infringement; know whether it is capped.
- **IP:** who owns work product, customer data, feedback and improvements.
- **Termination:** convenience versus cause, cure periods, post-termination data return.
- **Payment terms:** net days, late fees, taxes, currency, refunds.
- **Governing law and venue:** a distant court can make a dispute unaffordable.

**So what for a solo founder:** Start from one open, well-maintained template set, use customer terms, a contractor agreement and a DPA before anything else, and spend lawyer money on the liability, indemnity and IP clauses rather than on boilerplate.

---

## 5. Hiring the first contractor or employee

**Not legal advice. Rules vary widely by country (and by state or province); this section gives two examples only.**

- **US (IRS):** The common-law test sorts facts into behavioural control, financial control and type of relationship (contracts, benefits, permanence, whether work is central to the business) ([IRS, Independent Contractor (Self-Employed) or Employee?](https://www.irs.gov/businesses/small-businesses-self-employed/independent-contractor-self-employed-or-employee), opened). Labour law uses a different test: the DOL's economic reality test. A 2026 proposal (Federal Register 2026-02-27, comments to 2026-04-28) would rescind the 2024 rule and restore a 2021-style test weighting control and opportunity for profit or loss; DOL stopped applying the 2024 standard in enforcement in May 2025 ([Jackson Lewis, 2026](https://www.jacksonlewis.com/insights/dols-proposed-2026-independent-contractor-rule-what-employers-need-know), search snippet). I did not confirm whether a final rule has issued; see Open questions. State tests (for example ABC tests) can be stricter.
- **UK (HMRC):** Status turns on the whole picture, with control, personal service/substitution, mutuality of obligation and financial risk; contract labels alone do not decide it. HMRC offers the free CEST tool, revised 2025-04-30 with no change to principles ([HMRC Employment Status Manual](https://www.gov.uk/hmrc-internal-manuals/employment-status-manual/esm0558), search snippet). Tax status is distinct from employment-rights status (employee, worker, self-employed).
- **Elsewhere:** many countries add presumptions, social-charge rules or a separate "worker" category; check local guidance.
- **Inference:** Contractor signals: they set their own hours and methods, use their own tools, serve several clients, can send a substitute, and are paid per deliverable. Misclassification risks back taxes and penalties. Use an employer-of-record or payroll provider if hiring across borders (options only; not researched here).
- Pointer, options only: third-party plugin `hr-legal-compliance`.

**So what for a solo founder:** Before the first hire, run the official status test for your country, write the contract to match the real working arrangement, and put IP assignment and confidentiality in the signed agreement.

---

## 6. When a lawyer is non-negotiable

**Always get a qualified lawyer for:** priced financing or SAFE negotiations; founder or co-founder equity and any vesting dispute; IP assignment or licensing of core technology; any customer or partner contract with uncapped liability, exclusivity or data-breach indemnity; cross-border employment; regulated products (health, finance, children's data); trademark conflicts; and anything involving litigation threats.

### Cost ranges (low confidence; mostly vendor sources)

- **Incorporation tools:** Stripe Atlas about USD 500; Clerky USD 427 (incorporation only) or USD 819 (lifetime package) ([Rho, 2026](https://www.rho.co/blog/how-to-incorporate-a-startup), snippet; Rho sells banking to startups). Law-firm incorporation about USD 2,000-5,000 in one guide (same snippet set).
- **Seed financing legal fees:** a TechCrunch-hosted article (2019, over two years old) estimates USD 5,000-20,000 using common forms; an unattributed 2026 cost guide gives USD 25,000-75,000, with no stated method ([founder-intelligence guide](https://founder-intelligence-local.vercel.app/costs/startup-lawyer-fees), snippet, low reliability). **Range: roughly USD 5,000 to USD 75,000; treat the top as unverified.**
- **Trademark attorney fees:** not sourced here; official filing fees are in section 3.
- **Fixed fees and programmes:** many firms offer fixed-price incorporation packages, and sources recommend asking for fixed fees on project work such as a seed round (same snippet set). Programme options include Cooley GO and similar free resource libraries (see 4.1), Stripe Atlas, Clerky and accelerator-provided legal perks (YC and others; terms not verified). Ask each firm about startup or deferred-fee arrangements.

### 15 questions to bring to a startup lawyer

1. Which entity type and jurisdiction fit my plans and why?
2. How should my founder shares be issued, and should they vest? On what schedule?
3. Do I need an 83(b) election (or local equivalent), and who files it by when?
4. Does my founder IP assignment cover everything I built before incorporation, including domains and accounts?
5. Does any former employer, university or client have a claim on my work?
6. Are my current contractors and any past helpers covered by written assignments?
7. What open-source licences are in my product, and which are risky for how I deliver it?
8. What is the current position on owning AI-assisted code and content in my markets?
9. Which name, domain and trademark risks do you see, and where should I file first?
10. Which customer terms should I use, and which clauses should I never concede?
11. What liability cap, indemnity and insurance should I have for my first enterprise deal?
12. Am I a controller or processor, and what privacy and DPA documents do I need?
13. How do I classify my first contractor or hire in my country, and what is the downside if I am wrong?
14. What will this engagement cost, can it be fixed-fee, and what is out of scope?
15. What should I never sign without calling you?

Pointer, options only: third-party plugin `general-counsel-advisor`.

**So what for a solo founder:** Pay for a lawyer on equity, IP assignment, financing and high-liability contracts, use templates for the rest, and ask for fixed fees up front.

---

## 7. Staged plan

### Week 1
- Incorporate and issue founder shares in writing; decide on vesting; if vesting in the US, file the 83(b) within 30 days and keep proof.
- Sign the founder IP assignment, including domains and accounts.
- Secure the domain, social handles and a company-owned email with 2FA; do a name knock-out search.

### Month 1
- Put a customer-terms template and order form in place; set a privacy policy and website terms.
- Use a contractor agreement with IP assignment for every contributor; collect signatures from past contributors.
- Start a dependency and licence inventory; add licence scanning to CI.
- Review `secret-exposure-response` (repo skill) so leaked credentials have a runbook, and `data-protection-readiness` (repo skill) before handling personal data.

### Quarter 1
- Run a full trademark clearance and file in your main market.
- Draft a DPA and acceptable-use policy; review refund terms against consumer law.
- Build a simple cap table and document advisor grants; book a lawyer review of everything above.
- Re-check AI-copyright and contractor-classification developments (both fast-moving).

---

## Checklist

- [ ] Founder shares issued in writing; ledger kept
- [ ] Vesting decision made and documented
- [ ] 83(b) filed within 30 days with proof (US, if applicable)
- [ ] Founder IP assignment signed (including domains and accounts)
- [ ] Prior-employer and third-party claims checked
- [ ] Contractor and employee IP assignments signed before work starts
- [ ] Open-source inventory and policy in place
- [ ] AI tool terms and human-authorship records reviewed
- [ ] Trade-secret hygiene: access control and confidentiality clauses
- [ ] Name knock-out search, domains and handles secured
- [ ] Trademark filed in main market
- [ ] Customer terms, order form, ToS, privacy policy, DPA live
- [ ] Contractor agreement and SOW templates ready
- [ ] Worker status checked for each first hire
- [ ] Lawyer review booked; questions list prepared

## Open questions

- Does Form 15620 now allow online submission, and what do the IRS instructions say about filing location? (PDF not machine-readable; one vendor blog claims online filing since July 2025.)
- Has the DOL independent-contractor rule been finalised since the April 2026 sources?
- Current EUIPO, USPTO and UKIPO examination timelines from official pages.
- USPTO fee effective date (2025-01-18 versus 2025-02-18) and current surcharges from the live fee schedule.
- Bonterms and Orrick licence terms, and Y Combinator document licences.
- EU and other-jurisdiction positions on AI-generated work ownership.
- Whether the UK s9(3) repeal has been legislated after June 2026.
- Madrid system dependency rules and typical timelines from WIPO pages.
- Independent, non-vendor data on startup legal fees.
- Employee-vs-contractor tests for countries beyond the US and UK.

## Sources

Access date for all: 2026-11-11. "Opened" means the page was fetched; "snippet" means only search-result text was seen.

1. [Y Combinator, How to Split Equity Among Co-Founders](https://www.ycombinator.com/blog/splitting-equity-among-founders) (snippet)
2. [Stripe, Founder vesting](https://stripe.com/resources/more/founder-vesting) (opened; vendor)
3. [26 CFR 1.83-2, Cornell LII](https://www.law.cornell.edu/cfr/text/26/1.83-2) (snippet)
4. [IRS Form 15620](https://irs.gov/pub/irs-pdf/f15620.pdf) (opened; unreadable body)
5. [Cozen, IRS creates Form 15620](https://www.cozen.com/news-resources/publications/2024/irs-creates-standardized-section-83b-election-form-15620) (snippet)
6. [Carta, pre-seed advisor equity](https://carta.com/data/linkedin-pre-seed-advisor-equity-0-24-percent/) (snippet; 403 on fetch)
7. [Carta, advisory shares guide](https://carta.com/sg/en/learn/startups/equity-management/advisory-shares/) (snippet)
8. [Carta, advisor guide](https://carta.com/uk/en/learn/startups/founding-team/advisor/) (snippet)
9. [Carta, first engineer equity](https://carta.com/data/linkedin-founding-engineer-equity-1-54-percent/) (snippet)
10. [Carta, first hire equity by sector](https://carta.com/data/linkedin-first-hire-equity-benchmarks-by-sector/) (snippet)
11. [Cortance, early-stage engineer equity](https://cortance.com/answers/hiring-team/what-is-a-typical-equity-range-for-early-stage-engineers-in-2026-startups) (snippet)
12. [SaaStr, equity for first employees](https://www.saastr.com/how-much-equity-to-give-your-first-employees-the-real-data-from-50000-startups) (snippet)
13. [Carta, option pool sizing](https://carta.com/blog/how-to-size-employee-option-pool/) (snippet)
14. [Carta, option pool guide (UK)](https://carta.com/uk/en/learn/startups/equity-management/option-pool/) (snippet)
15. [Carta, push back on 20% pools](https://carta.com/data/linkedin-option-pool-founders-push-back-20-percent/) (snippet)
16. [Carta, startup law firms](https://carta.com/learn/startups/founding-team/law-firms/) (snippet; 403 on fetch)
17. [Goodwin, top 10 commercial IP tips for startups](https://www.goodwinlaw.com/publications/2022/11/11_03-top-10-commercial-ip-tips-for-startups) (opened)
18. [OneGC, IP assignment for startups](https://onegc.com/blog/ip-assignment-for-startups) (opened; vendor)
19. [Promise Legal, open source compliance](https://blog.promise.legal/startup-central/open-source-license-compliance-for-startups/) (snippet)
20. [Jones Day, DTSA notice obligations](https://www.jonesday.com/en/insights/2016/05/federal-defend-trade-secrets-act-imposes-new-notice-obligations-on-employers) (snippet)
21. [Barnes & Thornburg, DTSA](https://www.bipc.com/how-the-defend-trade-secrets-act-of-2016-affects-employers-and-what-you-need-to-do-now) (snippet)
22. [US Copyright Office, AI initiative](https://www.copyright.gov/ai/) (opened)
23. [Copyright Alliance, Part 2 summary](https://copyrightalliance.org/ai-report-part-2-copyrightability/) (snippet)
24. [Holland & Knight, Thaler cert denied](https://www.hklaw.com/en/insights/publications/2026/03/the-final-word-supreme-court-refuses-to-hear-case-on-ai-authorship) (snippet)
25. [HSF Kramer, UK copyright and AI report](https://www.hsfkramer.com/notes/ip/2026-03/uk-government-report-on-copyright-and-ai-concludes-more-evidence-is-needed-although-s9-3-cdpa-could-go) (snippet)
26. [RPC, UK government report on copyright and AI](https://www.rpclegal.com/snapshots/technology-digital/summer-2026/uk-governments-report-on-copyright-and-ai/) (snippet)
27. [Waltmire, trademark clearance](https://www.waltmire.com/?p=1389) (snippet)
28. [GOV.UK, register a trade mark](https://www.gov.uk/how-to-register-a-trade-mark/start-your-application) (opened)
29. [CITMA, new UK IPO fees](https://www.citma.org.uk/resources/the-countdown-to-new-uk-ipo-fees-mb26.html) (opened)
30. [EUIPO, fees and payments](https://www.euipo.europa.eu/en/trade-marks/before-applying/fees-payments) (snippet)
31. [USPTO, 2025 trademark fee changes](https://www.uspto.gov/trademarks/fees-payment-information/summary-2025-trademark-fee-changes) (snippet; fetch blocked)
32. [WIPO, Madrid fees](https://www.wipo.int/en/web/madrid-system/how_to/file/fees) (opened)
33. [Common Paper, standard agreements](https://commonpaper.com/standards/) (opened)
34. [Cooley GO, NDAs with investors](https://www.cooleygo.com/should-you-require-a-signed-nda-from-a-potential-investor/) (opened)
35. [cloudnuro, SaaS liability cap](https://www.cloudnuro.ai/blog/saas-liability-cap) (snippet; vendor)
36. [Causo, SaaS contract negotiation](https://hub.causo.ai/guides/saas-contract-negotiation-clauses-founders-2026) (snippet; vendor)
37. [ICO, contracts under UK GDPR](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/accountability-and-governance/guide-to-accountability-and-governance/contracts/) (snippet)
38. [IRS, Independent Contractor or Employee](https://www.irs.gov/businesses/small-businesses-self-employed/independent-contractor-self-employed-or-employee) (opened)
39. [Jackson Lewis, DOL proposed 2026 rule](https://www.jacksonlewis.com/insights/dols-proposed-2026-independent-contractor-rule-what-employers-need-know) (snippet)
40. [HMRC Employment Status Manual ESM0558](https://www.gov.uk/hmrc-internal-manuals/employment-status-manual/esm0558) (snippet)
41. [Rho, how to incorporate a startup](https://www.rho.co/blog/how-to-incorporate-a-startup) (snippet; vendor)
42. [Founder-intelligence, startup lawyer fees](https://founder-intelligence-local.vercel.app/costs/startup-lawyer-fees) (snippet; low reliability)

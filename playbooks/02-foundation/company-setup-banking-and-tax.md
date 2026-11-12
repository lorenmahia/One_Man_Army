# Company Setup, Banking and Tax: A Country-Agnostic Playbook for Solo Founders

> Last verified: 2026-11-11. Research and planning support only; not legal, tax, investment or financial advice.

## Summary

- **Fact:** There is no single best place to incorporate. The right choice depends on where you live, where customers and investors are, and how likely you are to raise venture money. Use the decision method in section 1, then confirm with the registry and a local professional.
- **Fact:** Government registration fees are small (roughly US$100 to US$400 in the examples below). The expensive parts are annual compliance, accounting, registered agents and mistakes, such as a missed foreign-owned-LLC filing in the US that carries a stated US$25,000 penalty.
- **Inference:** Banking, not incorporation, is often the real bottleneck for foreign or crypto-adjacent founders. Apply for accounts early, keep documents consistent, and have a second payment route.
- **Fact:** Sales-tax and VAT duties can start well before profit: for example the EU 10,000 euro cross-border B2C threshold, UK GBP 90,000 VAT registration, and per-state US economic-nexus tests.
- **Inference:** An accountant is mandatory in practice for cross-border structures, payroll, VAT/nexus, and any equity or option grants. A lawyer is mandatory for investor-facing documents and the incorporation choice.

---

## 1. Decision method: where and what to incorporate

**Not legal or tax advice.** Confirm every point with the official registry of the country you choose and with a local lawyer and accountant before filing.

### 1.1 The method (answer these in order)

1. **Where do you live and pay tax?** Your tax residence usually matters more than where the company is registered. A company registered abroad but managed from your home country is often still taxed there (see section 5, controlled foreign company and place-of-management rules). **Inference.**
2. **Who will pay you?** If most customers are in one country, a local entity may be needed for invoicing, VAT/GST and trust.
3. **Will you raise venture capital?** Many US investors expect a Delaware C-corp; many European and Asian investors accept a local limited company but may ask for a flip later. **Inference** from the vendor material in section 3; verify with your target investors.
4. **Can you open a bank account and payment processor in that jurisdiction?** Check this before paying to incorporate (section 4).
5. **What is the cost of being wrong?** Moving later (a "flip": new holding company, share swap, asset transfer) costs legal fees, possible tax events and delay. **Estimate:** low thousands to tens of thousands of US dollars depending on complexity; get a quote.

### 1.2 Entity types at a conceptual level

| Type | Liability | Typical tax treatment (conceptual) | Fits when |
|---|---|---|---|
| Sole proprietorship / sole trader | Personal, unlimited | Business income taxed as yours | Testing an idea locally with low risk |
| Partnership | Often personal (varies by type) | Pass-through in most systems | Two or more people, services business |
| LLC / private limited company | Limited to the company | Company-level tax, or pass-through depending on country and election | Most single-founder businesses |
| C-corporation (US) | Limited | Company-level tax, then dividend tax | Planning to raise US venture capital or issue options |
| Branch of a foreign company | Parent is liable | Profits usually taxed in the branch country | Existing company entering a new market |

### 1.3 Decision table: where to incorporate

| Route | Fits when | Watch out for |
|---|---|---|
| Home country | You live there, customers are local, no near-term VC | Home-country investor norms; foreign customers may want a different jurisdiction |
| Target-market country | Regulated sector, local licences, public-sector buyers, local hiring | Setup friction, residency or local-director rules, foreign-ownership limits |
| Delaware (US) C-corp | US venture capital, stock options, US customers | US tax filings even with no US income; banking and processor rules; state sales-tax nexus |
| UK limited company | English-law contracts, UK/EU-adjacent customers, light registry process | UK corporation tax residence follows management; VAT thresholds |
| Singapore private company | Asia-Pacific customers and investors | At least one locally resident director is required (see 2.3) |
| Estonia via e-Residency | Remote EU business, fully digital admin | A digital ID alone does not create tax residence, but running the company from elsewhere can; bank access is separate |
| Emerging-market home country (e.g. Kenya) | You and your customers are there | Local banking, FX and tax-compliance burden; check foreign-ownership rules |

**So what for a solo founder:** Pick the jurisdiction where you can lawfully bank, get paid, and file taxes with the least friction today; only pay for a US flip when an investor actually asks.

---

## 2. Worked examples from official sources

All fees below were read on or around 2026-11-11 unless marked. **Fees change; confirm at the named registry before paying. This is not legal or tax advice.**

### 2.1 United States: Delaware

- **Registry:** Delaware Division of Corporations (corp.delaware.gov).
- **Fees (Estimate, mixed evidence):** A Division LLC formation form revised 8/2026 lists a US$110 Certificate of Formation fee; older Division documents list US$90, so treat US$90 as outdated ([Delaware LLC Formation form](https://corpfiles.delaware.gov/LLC_Forms/LLC%20Formation.pdf), snippet only; [Delaware 2018 fee schedule](https://corpfiles.delaware.gov/Augustfee2018.pdf), snippet only, 2018). A Certificate of Incorporation cover letter shows a minimum of US$89 plus US$9 per extra page, but it is undated ([Certificate of Incorporation form](https://corpfiles.delaware.gov/Corp_Forms/Incorporation%20-%20Stock.pdf), snippet only). Expedite is extra. Clerky's page cites US$203 in expedited state fees inside its price ([Clerky](https://clerky.com/), vendor, snippet).
- **Annual cost:** The Division says tax and annual reports are due March 1; corporations pay at least US$175 (authorized-shares method) or at least US$400 (assumed-par-value method), capped at US$200,000 (US$250,000 for Large Corporate Filers); late filing carries a US$200 penalty plus 1.5% monthly interest ([Annual Report and Tax Instructions](https://corp.delaware.gov/paytaxes/), snippet only, 2026). LLCs pay a flat annual tax reported as US$300 due June 1 in secondary guides ([Stripe LLC cost guide](https://stripe.com/resources/more/how-much-does-it-cost-to-form-an-llc-in-delaware-fees-and-other-costs), vendor, undated); I could not open the official page.
- **Time:** Same day to a few days with expedite. **Estimate.**
- **Minimum capital:** None required to form a Delaware corporation in the sources I saw. **Inference; unverified at the statute.**
- **Residency / local director:** I found no official statement requiring US-resident directors. A Delaware registered agent with a Delaware address is required (vendor sources). **Open question** (see below).
- **Foreign-owned tax filings:** A foreign-owned single-member LLC must file a pro forma Form 1120 with Form 5472; the IRS states a US$25,000 penalty for failure to file ([Instructions for Form 5472, Rev. December 2024](https://www.irs.gov/pub/irs-pdf/i5472.pdf); [IRS international information reporting penalties](https://www.irs.gov/payments/international-information-reporting-penalties)).
- **Beneficial ownership:** FinCEN exempted US-formed companies from beneficial-ownership reporting by an interim rule in March 2025, and a later final rule (FinCEN page dated August, likely 2026) made this permanent; foreign companies registered in the US still report ([FinCEN news release](https://www.fincen.gov/news/news-releases/fincen-permanently-ends-beneficial-ownership-reporting-requirements-millions), snippet only).

### 2.2 United Kingdom

- **Registry:** Companies House.
- **Fee (Fact, updated 2026-09-25):** GBP 100 online, GBP 124 paper, GBP 156 same-day via software; confirmation statement GBP 50 online ([Companies House fees](https://www.gov.uk/government/publications/companies-house-fees/companies-house-fees)). The fee rose on 1 February 2026 per the government notice, which shows the earlier figure was lower (GBP 65 for community interest companies) ([GOV.UK fee-change notice](https://www.gov.uk/government/news/update-regarding-companies-house-fee-changes), 2025-11-13). Community interest companies pay GBP 115 online.
- **Steps (Fact):** Appoint at least one director (no company secretary needed), register an official address, identify people with significant control (more than 25% of shares or votes), and file a statement of capital for a company limited by shares ([Set up a limited company](https://www.gov.uk/limited-company-formation)).
- **Time:** Not stated on the page; formation agents report hours to days. **Estimate.**
- **Minimum capital / residency / foreign ownership:** The page I read did not state a minimum capital, a director residency rule or a foreign-ownership limit. I did not verify these. **Open question.**

### 2.3 Singapore

- **Registry:** Accounting and Corporate Regulatory Authority (ACRA), through Bizfile.
- **Fee (Fact):** SGD 300 registration fee ([ACRA: registering a local company via Bizfile](https://www.acra.gov.sg/register/business/registering-different-business-structures/local-company/registering-via-bizfile/)). A name-application fee of SGD 15 is reported by secondary guides but not by the ACRA page I read ([Cost of Incorporating a Company in Singapore](https://leftrightcorp.com/guides/business-incorporation/singapore-company-incorporation-cost/), vendor, 2026).
- **Time (Fact):** Most registrations are approved soon after payment; complex ones can take up to 15 working days; those needing referral approval 14 to 60 days (same ACRA page).
- **Residency (Fact):** At least one director must meet local residency rules. A foreign founder usually needs a resident nominee director from a service provider or must relocate.
- **Capital (Fact):** The minimum number of issued shares is one; the page states no minimum paid-up amount.
- **Foreign ownership:** Shareholders can be individuals or corporate entities; no general foreign-ownership cap was stated on the page. Sector licences may differ. **Inference.**

### 2.4 European Union: Estonia (e-Residency)

- **Registry:** e-Business Register (Centre of Registers and Information Systems, RIK); e-Residency programme.
- **Fees (Estimate, secondary):** Online state fee for an OÜ reported as EUR 265; the e-Residency programme fee reported as EUR 150, though an older official figure was EUR 100 to 130 ([Enty: Estonian e-Residency fees 2026](https://enty.io/blog/estonian-e-residency-fees-2026-every-cost-line-item), vendor, 2026). A claimed change to a flat EUR 165 on 2027-01-01 is unverified. Please confirm on the official pages.
- **Time (Fact):** About 3 to 8 weeks to become an e-resident; 1 to 2 days to start a company online ([e-Residency: start a business](https://e-resident.gov.ee/start-transforming-your-business/)).
- **Capital (Fact, snippet):** Official e-Residency guidance sets the minimum share capital of an OÜ at EUR 0.01 per shareholder (older EUR 2,500 floor dropped) ([e-Residency help article](https://learn.e-resident.gov.ee/hc/en-us/articles/360000633557), snippet only; the page returned 403 on fetch).
- **Local rules:** A contact person or legal address service is commonly required for non-resident boards, at roughly EUR 250 to 400 per year in vendor guides ([Enty](https://enty.io/blog/estonian-e-residency-fees-2026-every-cost-line-item)). **Open question** against the official register.

### 2.5 Emerging market: Kenya

- **Registry:** Business Registration Service (BRS), filed on the eCitizen platform.
- **Fee (Fact):** KES 10,650 for a private limited company; certificate typically in 3 to 5 days ([BRS fee schedule: Companies Registry](https://brs.go.ke/fee-schedule-companies-registry/)). A secondary source reports KES 10,750 from another BRS document, so budget KES 10,650 to 10,750 ([Helloduty guide](https://helloduty.com/blogs/how-to-register-a-company-in-kenya), vendor, snippet).
- **Forms (Fact):** CR 1, CR 2, CR 8 and a statement of nominal capital (same BRS page).
- **Process:** Submit three preferred names online ([BRS home](https://www.brs.go.ke)).
- **Foreign ownership / directors (Estimate, secondary):** Guides say foreigners may be shareholders and directors, and a Kenyan tax PIN and registered office are needed. Not confirmed on a government page. **Open question.**
- **Minimum capital:** Not stated on the page I read.

### 2.6 Comparison snapshot

| Item | Delaware | UK | Singapore | Estonia | Kenya |
|---|---|---|---|---|---|
| Registry fee (date) | USD 90 to 110 LLC (2026) | GBP 100 (2026-09) | SGD 300 (2026) | EUR 265 reported (2026) | KES 10,650 (2026) |
| Local director needed | Not found | Not found | Yes, one | Contact person likely | Not confirmed |
| Minimum capital | None found | None found on page | None stated | EUR 0.01 | Not stated |

**So what for a solo founder:** Registry fees are not the deciding factor; residency rules, annual costs and banking access are, so check those first.

---

## 3. Remote and online incorporation services

**Vendor bias warning:** Prices below come mainly from the vendors themselves or from comparison blogs, some of which earn referral fees. Treat them as starting points.

| Service | What it does | Price (date) | Limits |
|---|---|---|---|
| [Stripe Atlas](https://stripe.com/atlas) | Delaware C-corp or LLC, EIN, equity issuance, 83(b) filing, templates, Stripe credits | USD 500 one-time including state fees and first-year registered agent; USD 100 per year after (2026-11, vendor) | Delaware only; ties you toward Stripe's ecosystem; does not give tax or legal advice |
| Firstbase | Delaware/Wyoming formation, EIN, documents | USD 399 list, USD 99 promotional in some windows; registered agent reported at USD 299 per year (secondary, 2026) ([Rho: Firstbase pricing](https://www.rho.co/blog/firstbase-pricing), competitor blog) | Prices conflict across sources; confirm on its pricing page |
| Clerky | Delaware C-corp, financing documents | USD 427 pay-per-use, USD 819 lifetime package; registered agent about USD 125 per year (2026, snippet) ([Clerky](https://clerky.com/)) | C-corp only; no accounting |
| Local equivalents | Registered-agent and incorporation firms (Singapore, Estonia, Kenya) | Vary by firm | Check licensing and whether they hold your documents |

**Limits common to all:** They file paperwork; they do not decide your tax residency, run your bookkeeping, or guarantee a bank account. **Inference.**

**So what for a solo founder:** Use a service for the mechanical filing if you chose Delaware, but treat its checklist as a minimum, not a plan.

---

## 4. Banking and payments

### 4.1 Account options

| Type | Examples | Good for | Watch out for |
|---|---|---|---|
| Traditional bank | Local high-street banks | Deposits, loans, local trust | Branch visits, slow onboarding, strict local-presence rules |
| Neobank / fintech | Mercury, Wise Business, Revolut Business, Airwallex | Remote opening, multi-currency | Not a bank itself (often partner-bank); product and country limits |
| Payment processor balance | Stripe, PayPal | Collecting customer payments | Reserves, holds, and freezes (section 4.3) |

Mercury's own help page says the company must be formed and registered in the US or a US territory, and that eligibility follows a full review; it holds fiat only ([Mercury eligibility](https://support.mercury.com/hc/en-us/articles/28770467511060-Eligibility), snippet only, fetch returned 403).

### 4.2 Documents they usually ask for

**Estimate** (typical, not universal): certificate of incorporation, articles or bylaws, tax ID (EIN, UTR, etc.), proof of address, government ID for each owner with 25% or more, a description of the business and expected volumes, website.

### 4.3 Why accounts get frozen or refused

- **Fact:** Some fintech banks have closed accounts for founders in particular countries; a 2024 report covers Mercury and Nigerian startups ([TechCabal, 2024-07-23](https://techcabal.com/2024/07/23/us-bank-mercury-to-close-accounts-of-nigerian-startups/), snippet only; older than two years from some readers' view, treat as dated).
- **Inference:** Common triggers are mismatched documents, vague business descriptions, sudden large inflows, high-risk categories (crypto, gambling, adult content), and sanctions screening.
- **Open question:** Whether a given bank accepts crypto-adjacent firms differs by bank and by month; sources I saw conflict (Mercury says it does not hold crypto but does not expressly bar buying it). Ask the bank in writing.

### 4.4 Payment processors and payout coverage

Stripe says it serves businesses in 46 countries and regions, sells to 195+ and sends payouts to 160+; availability varies by product ([Stripe global businesses](https://stripe.com/use-cases/global-businesses), search snippet, undated). Check Stripe's live availability page for your country before choosing an entity. Alternatives (PayPal, local gateways such as Paystack, Razorpay, merchant-of-record services) may cover countries Stripe does not; verify each. **Open question.**

### 4.5 Multi-currency and separation of money

- Hold balances in the currencies you invoice in; convert deliberately, not at checkout by default. **Inference.**
- Never pay personal expenses from the business account. Reimburse or pay yourself by a documented route (salary, dividend, loan). Mixing funds weakens the liability shield and creates tax and audit trouble. **Inference.**

**So what for a solo founder:** Open two accounts in different institutions, keep one clean story about your business across all applications, and do not rely on one processor.

---

## 5. Tax basics (conceptual)

**Not tax advice.** Confirm with the official tax authority in each country and a local accountant. **An accountant is mandatory in practice** for: any entity abroad from your tax residence, payroll, VAT/GST or sales-tax registration across borders, equity grants, and R&D credit claims.

### 5.1 Registration

You normally register with the tax authority after the company exists (corporate income tax, employer, VAT/GST). Some systems bundle this (for example, Estonia and India online filings); others require separate applications. Confirm per country.

### 5.2 Consumption taxes and thresholds

| Rule | Threshold or rule | Source and date |
|---|---|---|
| UK VAT registration | GBP 90,000 taxable turnover (12 months or expected in 30 days); overseas businesses supplying the UK must register regardless of turnover, except those with only zero-rated supplies | [GOV.UK: Register for VAT](https://www.gov.uk/register-for-vat), read 2026-11-11 |
| EU OSS | EUR 10,000 cross-border B2C sales (tax-excluded) lets single-state suppliers stay under home VAT; above that, destination-country VAT via the OSS (union scheme for EU firms, non-union scheme for non-EU); returns are quarterly | [EU One Stop Shop](https://vat-one-stop-shop.ec.europa.eu/one-stop-shop_en), read 2026-11-11 |
| Singapore GST | Compulsory above SGD 1 million (12-month test); overseas B2C digital sellers face a two-part test of global turnover above SGD 1 million and Singapore B2C sales above SGD 100,000 | [IRAS OVR seminar slides](https://www.iras.gov.sg/irashome/uploadedFiles/IRASHome/GST/OVR%20Seminar%20Slides(1).pdf) and [Kintsugi guide](https://trykintsugi.com/sales-tax-guides/apac/singapore), snippets only; IRAS threshold page returned 404 |
| US sales tax | After South Dakota v. Wayfair (2018), states can require remote sellers to collect tax above economic-nexus thresholds, commonly USD 100,000 or 200 transactions, ranging from about USD 10,000 to USD 500,000 and varying by state | [Thomson Reuters](https://tax.thomsonreuters.com/blog/how-states-responded-to-south-dakota-v-wayfair-in-2018/) and [Tax Foundation](https://taxfoundation.org/data/all/state/economic-nexus-by-state-2024/) (2024, snippet; older than two years in places; check each state's revenue department) |

### 5.3 Payroll tax and founder pay

- **Fact:** Hiring creates employer registration and withholding duties in the employee's country. Contractors in another country can still be reclassified as employees in some systems. **Inference.**
- **Founder pay:** Common options are salary, dividends, or a mix; the tax result differs a lot by country and entity. Ask an accountant to model it. **Inference.**

### 5.4 R&D credits (example)

- **United States:** A qualified small business may elect to use up to USD 500,000 of the research credit against payroll tax; the IRS reports this limit for tax years beginning after 2022 ([IRS: research credit against payroll tax](https://www.irs.gov/credits-deductions/research-credit-against-payroll-tax-for-small-businesses); [Form 8974 instructions](https://www.irs.gov/instructions/i8974), 2024).
- **United Kingdom:** Claims now go under a merged scheme or Enhanced R&D Intensive Support (ERIS) for periods starting on or after 1 April 2024; the page I read did not give current rates, so confirm with HMRC ([HMRC R&D relief guidance](https://www.gov.uk/guidance/corporation-tax-research-and-development-tax-relief-for-small-and-medium-sized-enterprises)).

### 5.5 Cross-border risks

- **Permanent establishment (PE):** The OECD's 2025 Model Tax Convention update says a home office can be a fixed place of business; its examples treat about 30% of working time at home as not enough on its own and 50% or more with a commercial reason as pointing to a PE. These are illustrations, not bright lines ([OECD 2025 update](https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/11/the-2025-update-to-the-oecd-model-tax-convention_c7031e1b/5798080f-en.pdf), snippet only; [OECD blog, June 2026](https://www.oecd.org/en/blogs/2026/06/home-and-away-when-does-working-remotely-across-borders-create-a-taxable-presence.html)).
- **Controlled foreign company (CFC):** The UK regime can tax certain profits of a non-UK company controlled by UK residents ([HMRC INTM191100](https://www.gov.uk/hmrc-internal-manuals/international-manual/intm191100)). Other countries have comparable rules, for example US filings for foreign-owned entities in section 2.1.
- **Tax residency by management:** Running a foreign company from your home country can make it taxable there. **Inference.**

**So what for a solo founder:** Register for consumption taxes before thresholds bite, and hire an accountant before you form any entity outside your tax residence.

---

## 6. Bookkeeping and finance operations

- **Accounting software:** Choose one that supports your country's tax rules and multiple currencies (examples: Xero, QuickBooks, Zoho Books, Wave, FreeAgent). Vendor availability varies by country. **Inference.**
- **Chart of accounts (basics):** Assets (bank, receivables), liabilities (payables, tax owed, loans), equity (share capital, retained earnings), revenue (by product line), cost of sales, operating expenses (software, contractors, marketing, professional fees).
- **Monthly close (30 to 60 minutes if kept current):** reconcile each bank and processor to the ledger; categorize transactions; match receipts; review unpaid invoices; record tax liabilities; lock the month; export a simple profit-and-loss and balance sheet.
- **Receipts:** Photograph or forward every receipt the day it occurs to a dedicated inbox or folder. Retention periods differ by country; ask your accountant.
- **Invoicing:** Sequential numbers, your legal name and tax ID, customer details, tax shown separately, payment terms and currency. Some countries require specific e-invoice formats. **Open question.**
- **Expense policy (one page):** What the company pays for, approval limit, no personal spend, how reimbursements work.
- **Runway tracking:** Runway (months) = cash on hand divided by average monthly net burn. Track both a base and a pessimistic case. See in-repo `unit-economics-model` for margin and payback modelling.
- **Annual filings calendar (examples, verify):** Delaware annual report and franchise tax March 1 (LLC tax June 1 in secondary sources); UK confirmation statement yearly plus accounts and corporation tax (deadlines on GOV.UK); Singapore annual return and corporate tax filings; Estonia annual report; Kenya annual return. Put every date in a shared calendar with a 30-day reminder.

**So what for a solo founder:** A weekly 15-minute reconcile beats a quarterly panic; set it up in Week 1.

---

## 7. Insurance basics

- **Types to consider (Inference):** professional indemnity / errors-and-omissions (service and software businesses), cyber liability (if you hold customer data), general liability (if you meet people or hold stock), directors and officers (once you have investors or a board), employer's liability or workers' compensation (once you hire; often legally required).
- **Triggers:** Customer contracts often require minimum cover; investors may ask for D&O; hiring triggers legal requirements.
- **Rule of thumb:** Ask a broker for quotes; premiums depend on revenue, sector and country. I did not find an official source for typical premiums, so no figures are given. **Open question.**
- Pair with in-repo `data-protection-readiness` before buying cyber cover.

**So what for a solo founder:** Buy the cover a contract or law requires first; defer the rest until revenue or investors justify it.

---

## 8. Staged plan

### Week 1
- Decide jurisdiction using section 1; write down why.
- Consult a local accountant (30-minute intro call).
- Reserve company name; check trademark conflicts.
- File incorporation (or engage an online service); get tax ID.
- Start bank and payment-processor applications in parallel.

### Month 1
- Open accounts; separate personal and business money.
- Choose accounting software; connect feeds; set up chart of accounts.
- Issue founder shares; sign a founder IP assignment (lawyer).
- Register for payroll or VAT/GST if thresholds or plans require.
- Draft expense policy and invoicing template.

### Quarter 1
- First quarterly review with accountant: tax estimates, VAT/nexus exposure, founder pay.
- Review insurance needs against contracts.
- Build annual filings calendar; set runway dashboard.
- Re-test whether the entity still fits investor plans (flip decision).

---

## Checklist

- [ ] Home tax residence confirmed and written down
- [ ] Jurisdiction chosen with the decision table
- [ ] Official registry page opened and fees dated
- [ ] Local lawyer and accountant identified
- [ ] Company registered; certificate stored
- [ ] Tax ID and tax registrations done
- [ ] Two business accounts and one payment processor applied for
- [ ] Personal and business money separated
- [ ] Accounting software and monthly close routine running
- [ ] Receipts and invoices process set
- [ ] VAT/GST/sales-tax thresholds mapped to your sales
- [ ] Annual filings calendar created
- [ ] Insurance reviewed

## Questions to ask a lawyer

1. Which entity and jurisdiction fit my investor plans, and what would a flip cost?
2. What founder agreements, IP assignment and vesting do I need?
3. Do I need any local director, registered agent or contact person?
4. Are there foreign-ownership limits or licences for my sector?
5. What happens to my equity and IP if a co-founder or investor joins?

## Questions to ask an accountant

1. Where am I tax-resident, and where would the company be treated as resident?
2. What filings does a foreign-owned entity owe even with no income?
3. When must I register for VAT/GST/sales tax, given my customers?
4. How should I pay myself (salary, dividend, loan) and what is the total tax?
5. Does my work create a permanent establishment or CFC exposure?
6. Do I qualify for R&D or startup incentives, and what evidence is needed?

## Related tools (names only)

- In-repo skills: `country-business-research`, `data-protection-readiness`, `unit-economics-model`.
- Third-party plugins (options only; I make no claims beyond their names and descriptions): `finance-skills`, `hr-legal-compliance`, `general-counsel-advisor`.

## Open questions

- Delaware corporation current filing fee and official LLC annual tax page (corp.delaware.gov pages returned errors to the fetch tool; numbers come from snippets).
- Whether Delaware, UK, Estonia or Kenya impose any director-residency or minimum-capital rules beyond those cited.
- Estonia: current e-Residency fee and the planned 2027 change; contact-person rule.
- Kenya: foreign director/shareholder rules on an official page; KES 10,650 vs 10,750.
- Singapore: SGD 15 name fee and IRAS GST thresholds on official pages.
- India and Brazil were not researched; add if a reader needs them.
- Bank policies on crypto-adjacent and foreign founders change often; verify directly.
- Insurance premium ranges; e-invoicing mandates by country.

## Sources

All accessed 2026-11-11. "Snippet" means only a search snippet was seen.

1. [Companies House fees](https://www.gov.uk/government/publications/companies-house-fees/companies-house-fees)
2. [GOV.UK fee-change notice](https://www.gov.uk/government/news/update-regarding-companies-house-fee-changes)
3. [Set up a limited company](https://www.gov.uk/limited-company-formation)
4. [GOV.UK: Register for VAT](https://www.gov.uk/register-for-vat)
5. [ACRA: registering a local company via Bizfile](https://www.acra.gov.sg/register/business/registering-different-business-structures/local-company/registering-via-bizfile/)
6. [e-Residency: start a business](https://e-resident.gov.ee/start-transforming-your-business/)
7. [e-Residency help article (snippet)](https://learn.e-resident.gov.ee/hc/en-us/articles/360000633557)
8. [BRS Kenya fee schedule](https://brs.go.ke/fee-schedule-companies-registry/)
9. [BRS Kenya home](https://www.brs.go.ke)
10. [Delaware LLC Formation form (snippet)](https://corpfiles.delaware.gov/LLC_Forms/LLC%20Formation.pdf)
11. [Delaware Certificate of Incorporation form (snippet)](https://corpfiles.delaware.gov/Corp_Forms/Incorporation%20-%20Stock.pdf)
12. [Delaware 2018 fee schedule (snippet)](https://corpfiles.delaware.gov/Augustfee2018.pdf)
13. [Delaware annual report and tax instructions (snippet)](https://corp.delaware.gov/paytaxes/)
14. [IRS Form 5472 instructions](https://www.irs.gov/pub/irs-pdf/i5472.pdf)
15. [IRS international information reporting penalties](https://www.irs.gov/payments/international-information-reporting-penalties)
16. [FinCEN beneficial ownership news release (snippet)](https://www.fincen.gov/news/news-releases/fincen-permanently-ends-beneficial-ownership-reporting-requirements-millions)
17. [EU One Stop Shop](https://vat-one-stop-shop.ec.europa.eu/one-stop-shop_en)
18. [IRAS OVR seminar slides (snippet)](https://www.iras.gov.sg/irashome/uploadedFiles/IRASHome/GST/OVR%20Seminar%20Slides(1).pdf)
19. [IRS research credit against payroll tax](https://www.irs.gov/credits-deductions/research-credit-against-payroll-tax-for-small-businesses)
20. [IRS Form 8974 instructions](https://www.irs.gov/instructions/i8974)
21. [HMRC R&D relief guidance](https://www.gov.uk/guidance/corporation-tax-research-and-development-tax-relief-for-small-and-medium-sized-enterprises)
22. [OECD 2025 Model Tax Convention update (snippet)](https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/11/the-2025-update-to-the-oecd-model-tax-convention_c7031e1b/5798080f-en.pdf)
23. [OECD blog on remote work, June 2026](https://www.oecd.org/en/blogs/2026/06/home-and-away-when-does-working-remotely-across-borders-create-a-taxable-presence.html)
24. [HMRC CFC overview INTM191100 (snippet)](https://www.gov.uk/hmrc-internal-manuals/international-manual/intm191100)
25. [Mercury eligibility (snippet)](https://support.mercury.com/hc/en-us/articles/28770467511060-Eligibility)
26. [TechCabal on Mercury and Nigerian startups, 2024 (snippet)](https://techcabal.com/2024/07/23/us-bank-mercury-to-close-accounts-of-nigerian-startups/)
27. [Stripe Atlas](https://stripe.com/atlas) (vendor)
28. [Stripe global businesses (snippet)](https://stripe.com/use-cases/global-businesses) (vendor)
29. [Clerky](https://clerky.com/) (vendor, snippet)
30. [Rho: Firstbase pricing](https://www.rho.co/blog/firstbase-pricing) (competitor blog, snippet)
31. [Stripe: Delaware LLC cost guide](https://stripe.com/resources/more/how-much-does-it-cost-to-form-an-llc-in-delaware-fees-and-other-costs) (vendor, snippet)
32. [Enty: Estonian e-Residency fees 2026](https://enty.io/blog/estonian-e-residency-fees-2026-every-cost-line-item) (vendor, snippet)
33. [Leftright: Singapore incorporation cost](https://leftrightcorp.com/guides/business-incorporation/singapore-company-incorporation-cost/) (vendor, snippet)
34. [Helloduty: Kenya guide](https://helloduty.com/blogs/how-to-register-a-company-in-kenya) (vendor, snippet)
35. [Kintsugi: Singapore GST guide](https://trykintsugi.com/sales-tax-guides/apac/singapore) (vendor, snippet)
36. [Thomson Reuters: Wayfair state responses](https://tax.thomsonreuters.com/blog/how-states-responded-to-south-dakota-v-wayfair-in-2018/) (snippet, 2018)
37. [Tax Foundation: economic nexus by state 2024](https://taxfoundation.org/data/all/state/economic-nexus-by-state-2024/) (snippet, 2024)

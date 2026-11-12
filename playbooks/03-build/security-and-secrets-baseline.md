# Security and Secrets Baseline for a One-Person Startup

> Last verified: 2026-11-11. Research and planning support only; not legal, tax, investment or financial advice.

## Summary

- **Fact:** The two biggest ways in are stolen or reused credentials and unpatched software. In Verizon's 2026 report, vulnerability exploitation overtook credential abuse as the top initial-access vector for the first time ([Help Net Security, May 2026](https://www.helpnetsecurity.com/?p=371418)). Third parties now appear in nearly half of breaches (same source).
- **Fact:** Leaked secrets are an industrial-scale problem. GitGuardian counted about 28.65 million new hardcoded secrets in public GitHub commits in 2025, up 34% ([GitGuardian, Mar 2026](https://blog.gitguardian.com/the-state-of-secrets-sprawl-2026/)).
- **Inference:** Ten inexpensive controls (passkeys/MFA, password manager, device hardening, least privilege, secrets management, dependency scanning, SAST, tested backups, alerting, vendor inventory) cover most of what a questionnaire asks about. Expect roughly 2-3 focused days to put the first version in place (Estimate).
- **Fact:** AI coding agents and third-party plugins/skills/MCP servers are a new attack surface. Anthropic's own docs say it does not security-audit MCP servers ([Claude Code security docs, accessed 2026-11-11](https://code.claude.com/docs/en/security)).
- **Inference:** SOC 2 or ISO 27001 is a sales-driven decision, not a day-one need. Build the controls and a minimal policy set first, then buy an attestation only when a specific deal or investor requires it. Vendor cost and timeline claims are biased and unsourced (see section 4).

---

## 1. Threat model for a solo founder

A one-person company is attractive for the same reasons it is weak: one identity holds email, code, cloud, payments and DNS. A single compromised account is the whole company.

### What actually gets small companies breached

| Threat | Evidence (with date) | Confidence |
|---|---|---|
| Credential theft / reuse | Credential abuse was the top initial vector in the 2025 DBIR (data Nov 2023 to Oct 2024), at about 22% vs 20% for exploitation ([Security Magazine, Apr 2025, search snippet](https://www.securitymagazine.com/articles/101569-verizon-2025-data-breach-investigations-report-shows-rise-in-cyberattacks)). In the 2026 DBIR (data Nov 2024 to Oct 2025) it dropped to second ([Help Net Security, May 2026](https://www.helpnetsecurity.com/?p=371418)). | Fact (secondary reporting; primary DBIR not opened) |
| Unpatched software | 2026 DBIR: exploitation is now first. Secondary reports put it at about 31% of incidents vs about 13% for credential abuse ([SecureWorld, May 2026, search snippet](https://www.secureworld.io/industry-news/verizon-dbir-attackers-moving-faster-than-remediation)); one outlet cited 36%, so treat it as a 31-36% range. Median time to fully patch rose from 32 to 43 days; only 26% of CISA KEV entries were fully remediated ([Help Net Security](https://www.helpnetsecurity.com/?p=371418)). | Fact, range |
| Phishing / social engineering | In EMEA, phishing appeared in 19% of breaches in 2025 data ([Verizon EMEA release, Apr 2025](https://www.verizon.com/about/news/2025-data-breach-investigations-report-emea)). 2026 reporting says phishers do better via voice and text than email ([Help Net Security](https://www.helpnetsecurity.com/?p=371418)). CISA calls phishing consistently the most cost-effective way to compromise systems ([CISA small business, accessed 2026-11-11](https://www.cisa.gov/small-business)). | Fact |
| Leaked secrets in repos | 28.65M new secrets in public commits in 2025; internal repos about 6x more likely to contain secrets; about 28% of incidents originate outside repos (Slack, Jira, Confluence); more than 64% of credentials confirmed valid in 2022 were still valid in Jan 2026 ([GitGuardian, Mar 2026](https://blog.gitguardian.com/the-state-of-secrets-sprawl-2026/)). Vendor report with commercial interest. | Fact (vendor) |
| Supply-chain compromise | Third-party involvement doubled from 15% to 30% in the 2025 DBIR ([Security Magazine](https://www.securitymagazine.com/articles/101569-verizon-2025-data-breach-investigations-report-shows-rise-in-cyberattacks)) and is near half in 2026 reporting. Concrete cases: the `tj-actions/changed-files` GitHub Action compromise (March 2025) could expose CI secrets ([CISA, Mar 2025](https://www.cisa.gov/news-events/alerts/2025/03/18/supply-chain-compromise-third-party-github-action-cve-2025-30066)); the npm "Shai-Hulud" worm (CISA alert 2025-09-23) compromised over 500 packages and harvested tokens ([CISA, Sep 2025, search snippet](https://www.cisa.gov/news-events/alerts/2025/09/23/widespread-supply-chain-compromise-impacting-npm-ecosystem)). | Fact |
| Misconfiguration (cloud storage, access control) | OWASP's 2025 list ranks Broken Access Control first and Security Misconfiguration second ([OWASP Top 10:2025](https://top10.owasp.org/2025)). IBM names cloud misconfiguration among root causes of AI-related breaches ([IBM 2026](https://www.ibm.com/think/x-force/2026-cost-of-a-data-breach-ai-adversaries-enterprise-risk)). | Fact |
| Ransomware | Present in 44% of breaches (2025 DBIR) and 48% (2026 DBIR, per [Help Net Security](https://www.helpnetsecurity.com/?p=371418)). IDC commentary in Verizon's release says smaller, less mature firms are hit hardest, with ransomware in 88% of their breaches ([Verizon EMEA release](https://www.verizon.com/about/news/2025-data-breach-investigations-report-emea)); I found that 88% only in secondary summaries, so treat as indicative. | Fact, flagged |

### What a breach costs

- **Fact:** IBM's 2026 report (published 2026-07-29, 602 organizations) puts the global average at USD 4.99 million, up 12% and a record ([IBM, Jul 2026](https://www.ibm.com/think/x-force/2026-cost-of-a-data-breach-ai-adversaries-enterprise-risk)). The 2025 report gave USD 4.44 million, down about 9% from USD 4.88 million, with a mean 241 days to identify and contain ([IBM, Jul 2025](https://www.ibm.com/think/x-force/2025-cost-of-a-data-breach-navigating-ai)). Range across the two latest years: USD 4.44M-4.99M.
- **Caveat (Inference):** These are averages over mostly large organizations. I did not find a verified small-company figure, so do not quote them as your expected loss. For you the realistic damage is lost customers, account takeover, downtime and a failed enterprise deal.
- **Fact:** Shadow AI added about USD 670,000 to average cost in 2025 data, and 63% of surveyed organizations had no AI governance policy ([IBM 2025](https://www.ibm.com/think/x-force/2025-cost-of-a-data-breach-navigating-ai)). In 2026, 92% of organizations with an AI-related breach lacked proper AI access controls ([IBM 2026](https://www.ibm.com/think/x-force/2026-cost-of-a-data-breach-ai-adversaries-enterprise-risk)).

**So what for a solo founder:** Defend identity first (your accounts), then patching and secrets; those are where the data points converge, and they are cheap.

---

## 2. The 10 controls to put in place first

Time costs are **Estimates** for one person starting from scratch; scale up if you have many systems.

### 1. Strong authentication: passkeys and MFA everywhere (about 2 hours)
- **How:** Enable passkeys or FIDO2 security keys on email, domain registrar, source host, cloud, payments, password manager. Buy two hardware keys (one spare in a safe place). Fall back to authenticator-app TOTP where passkeys are unavailable; avoid SMS. Turn on recovery codes and store them offline.
- **Why:** CISA says any MFA beats none but FIDO authentication is the strongest widely available option ([CISA small business](https://www.cisa.gov/small-business)). A Microsoft study estimated MFA cut compromise risk by about 99.22% overall and 98.56% with leaked credentials; it is a 2023 estimate and app-based MFA beat SMS ([Microsoft Research, 2023, search snippet](https://arxiv.org/abs/2305.00945)).
- **Priority accounts:** primary email and domain registrar first (they reset everything else).

### 2. Password manager (about 1 hour, plus ongoing)
- **How:** One reputable manager with a long unique master passphrase and a passkey/hardware key for the vault. Generate unique random passwords for every site. Move shared and service credentials into it, not into notes or chat.
- **Why:** Unique passwords limit credential stuffing, a main route behind credential abuse (see section 1).

### 3. Device security (about 2 hours)
- **How:** Full-disk encryption on, automatic OS and browser updates, screen lock, no admin rights for daily use, endpoint protection that ships with the OS, and a separate browser profile for admin consoles. CISA's list for small businesses includes disk encryption, removing admin privileges from everyday laptops, and auto-updates ([CISA small business](https://www.cisa.gov/small-business)).
- **Also:** Keep a device inventory (one line per device) for questionnaires.

### 4. Least-privilege access (about 3 hours)
- **How:** Use a separate admin identity for cloud consoles; day-to-day work with a non-root role. Per-service API keys with minimum scopes. Never use the root/owner account for CI. Review who and what has access to each system quarterly (contractors, apps, OAuth grants). Remove unused OAuth app grants.
- **Why:** OWASP ranks Broken Access Control first ([OWASP Top 10:2025](https://top10.owasp.org/2025)); IBM notes fewer than half of organizations actively secure non-human identities ([IBM 2026](https://www.ibm.com/think/x-force/2026-cost-of-a-data-breach-ai-adversaries-enterprise-risk)).

### 5. Secrets management (about 4 hours initially)
- **Never in git:** Keep secrets in environment variables sourced from a secrets manager (cloud provider, or a dedicated tool) and in CI secret stores. Commit only `.env.example` with placeholders. Add a `.gitignore` entry for real env files.
- **Prevent:** Install a pre-commit secret scanner and enable your host's push protection and secret scanning if available (check your plan; availability varies). GitGuardian reports AI-assisted commits leaked at 3.2% vs a 1.5% public baseline ([GitGuardian, Mar 2026](https://blog.gitguardian.com/the-state-of-secrets-sprawl-2026/)), so agent output deserves the same scanning. The report also found 24,008 unique secrets in MCP-related config files.
- **Rotate:** Use short-lived credentials where possible (OIDC from CI to cloud instead of long-lived keys). Rotate long-lived keys at least annually and immediately on suspicion, departure of a contractor, or a vendor breach.
- **After a leak:** (1) Revoke or rotate first; deleting the commit does not make the secret safe. (2) Check provider logs for use during the exposure window. (3) Only then rewrite history, and know that forks, clones and cached views may keep copies; GitHub's own documentation describes history rewriting and cleanup of forks as separate steps and says support removal is limited to cases rotation cannot mitigate ([GitHub Docs, search snippet](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)). (4) Record what happened. CISA's guidance after the `tj-actions` incident was to treat exposed secrets as compromised and rotate them ([CISA, Mar 2025](https://www.cisa.gov/news-events/alerts/2025/03/18/supply-chain-compromise-third-party-github-action-cve-2025-30066)).

### 6. Dependency and container scanning (about 2 hours)
- **How:** Enable automated dependency alerts and update PRs on your source host, commit lockfiles, scan container images and base images on every build, and use minimal base images. Triage by exploitability: prioritize CISA's Known Exploited Vulnerabilities catalog ([CISA small business](https://www.cisa.gov/small-business)).
- **Why:** Patch lag is growing (median 43 days; see section 1).

### 7. SAST (about 2 hours)
- **How:** Add one static analysis tool and a secrets scanner to CI; fail the build on high severity. Keep the ruleset small to avoid alert fatigue. Treat AI-generated code as untrusted input to this same pipeline.

### 8. Backups and restore tests (about 3 hours, then a quarterly drill)
- **How:** Automate backups of databases, object storage and configuration (infrastructure as code); keep at least one copy in a different account or provider with write-once/versioning where available; encrypt backups. Run a real restore into a scratch environment and time it. CISA tells small businesses to test partial and full restores and keep a documented restoration plan ([CISA small business](https://www.cisa.gov/small-business)).
- **Why:** Ransomware is in roughly 44-48% of breaches (section 1); restorable backups are your leverage.

### 9. Logging and alerting (about 3 hours)
- **How:** Turn on audit logs for email/identity, source host, cloud and payments; send alerts for new logins from new devices, new API keys, permission changes, billing spikes and failed deploys to a channel you will actually see. Keep logs 90+ days if affordable (Inference; auditors commonly ask for retention evidence).
- **Why:** "Security Logging and Alerting Failures" is on OWASP's 2025 list ([OWASP Top 10:2025](https://top10.owasp.org/2025)); IBM's mean time to identify and contain was 241 days ([IBM 2025](https://www.ibm.com/think/x-force/2025-cost-of-a-data-breach-navigating-ai)).

### 10. Vendor and SaaS inventory (about 2 hours)
- **How:** One spreadsheet: vendor, purpose, data types they hold, who owns the account, MFA status, contract/DPA link, security page or attestation link, renewal date. Add AI tools and agent plugins. Review annually.
- **Why:** Third parties appear in a large and rising share of breaches (section 1), and questionnaires always ask for this list.

**So what for a solo founder:** Controls 1-3 take about half a day and remove the most likely failure (a stolen login). Do those before anything else, then work down the list.

---

## 3. Secure development

### Standards to point to
- **OWASP Top 10:2025** categories: Broken Access Control; Security Misconfiguration; Software Supply Chain Failures; Cryptographic Failures; Injection; Insecure Design; Authentication Failures; Software or Data Integrity Failures; Security Logging and Alerting Failures; Mishandling of Exceptional Conditions ([OWASP](https://top10.owasp.org/2025)). It is an awareness list, not a checklist.
- **OWASP ASVS 5.0** (released May 2025) is the verification standard with levels L1-L3; secondary sources describe roughly 350 requirements across 17 chapters and L2 as the usual commercial target ([SoftwareMill, 2025, search snippet](https://softwaremill.com/whats-new-in-asvs-5-0/)). Counts vary by source; confirm in the [OWASP ASVS repository](https://github.com/OWASP/ASVS). **Inference:** use L1 as your internal target and answer customers with "built against ASVS L1, working toward L2", which is honest.

### Habits that matter most
- **Secure defaults:** deny by default on authorization checks (enforce server-side on every request), private storage buckets by default, least-privilege database users, security headers, HTTPS only.
- **Input validation:** validate on the server against an allow-list schema; use parameterized queries; encode output; limit upload types and sizes.
- **Dependency pinning:** commit lockfiles; pin CI actions to full commit SHAs, not mutable tags. The `tj-actions` attack worked by repointing version tags to a malicious commit ([CISA, Mar 2025](https://www.cisa.gov/news-events/alerts/2025/03/18/supply-chain-compromise-third-party-github-action-cve-2025-30066); the tag-repointing detail is from secondary reporting such as [The Hacker News, Mar 2025](https://thehackernews.com/2025/03/cisa-warns-of-active-exploitation-in.html)). CERT/CC notes `npm install --ignore-scripts` can block install-time execution and advises scoped tokens and isolated builds ([CERT/CC VU#534320, search snippet](https://kb.cert.org/vuls/id/534320)).
- **SLSA basics:** SLSA v1.0's Build track has Levels 1-3: provenance exists (L1), signed provenance from a hosted build (L2), hardened build platform (L3) ([SLSA spec, search snippet](https://slsa.dev/spec/v1.0/levels)). slsa.dev now lists a newer version (v1.2), so check the current text. **Inference:** a solo founder reasonably targets L1-L2 via a hosted CI that can generate provenance.
- **OpenSSF Scorecard:** an automated tool that scores a repository on checks such as Branch-Protection, Token-Permissions and Pinned-Dependencies; its authors call the checks heuristics with false positives and negatives ([OpenSSF Scorecard repo, search snippet](https://github.com/ossf/scorecard)). Weights and check counts differ across secondary sources; read the official checks doc. Useful as a free, public-facing signal.

### Protect the CI pipeline itself
- Give the CI token read-only permissions by default and elevate per job; use OIDC instead of stored cloud keys; require branch protection and review (even self-review with required status checks) on the default branch.
- Never expose secrets to workflows triggered by untrusted pull requests; keep secrets out of logs.
- Be aware CI is a target: in the Shai-Hulud dataset, 59% of compromised machines were CI/CD runners ([GitGuardian, Mar 2026](https://blog.gitguardian.com/the-state-of-secrets-sprawl-2026/)).

### AI coding agents and third-party plugins, skills and MCP servers
- **Prompt injection (Fact):** Untrusted text (a README, web page, issue, or tool result) can try to steer an agent. Anthropic's docs define prompt injection and list mitigations (permission prompts, network-command approval, trust dialogs, fail-closed matching) but state that no system is completely immune ([Claude Code security docs](https://code.claude.com/docs/en/security)).- **Over-broad permissions (Fact):** The same docs say you are responsible for reviewing commands before approving them, and that a Bash command you approve can still write anywhere your user account can. Prefer the sandbox, deny rules for network fetch tools you do not need, and a dev container or VM for untrusted repos.
- **Hooks and project config execute code (Fact):** Anthropic's docs point to a section on what a repository's files can run before you trust a folder, and project-scoped `.mcp.json` servers have their own approval prompt; plugins can add MCP servers, so reviewing one file does not show every server loaded ([Claude Code security docs](https://code.claude.com/docs/en/security)). **Inference:** treat a plugin's hooks, scripts and MCP entries as code you are installing with your own privileges; read them before enabling.
- **MCP servers (Fact):** Anthropic encourages writing your own or using trusted providers, and states it does not security-audit or manage any MCP server ([Claude Code security docs](https://code.claude.com/docs/en/security)).
- **Skill marketplaces (Fact, wide range):** Snyk scanned 3,984 skills in Feb 2026: 13.4% had a critical-level issue, 36.82% had some issue, and human review confirmed 76 malicious payloads ([Snyk ToxicSkills, search snippet](https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/)). A March 2026 academic study of 238,180 skills reported malicious shares from 6.0% to 46.8% by marketplace and argued that scanning without repository context overstates risk ([arXiv 2603.16572, search snippet](https://arxiv.org/html/2603.16572v1)). Definitions differ, so treat the numbers as "meaningfully non-zero", not as a precise rate.
- **Framework (vendor summary):** OWASP's Top 10 for Agentic Applications (2026) covers goal hijack, tool misuse and agentic supply chain, and promotes "least agency" ([Palo Alto Networks summary, search snippet](https://paloaltonetworks.com/blog/cloud-security/owasp-agentic-ai-security/)). Check OWASP's own pages for exact wording.
- **Practical rules:** pin plugin versions; install from sources you can inspect; keep secrets out of the agent's working directory and environment; use a scratch cloud account or short-lived scoped tokens for agent tasks; keep a human in the loop for pushes, deploys and anything touching money or customer data; scan agent output with the same secret scanner and SAST as human code.

**So what for a solo founder:** Treat the agent, its plugins and your CI as privileged insiders: least privilege, pinned, scanned, and never fed secrets they do not need.

---

## 4. Compliance ladder

| Rung | When it becomes relevant | Typical effort (flag vendor bias) |
|---|---|---|
| Security baseline + questionnaire answers (section 2) | Always; from first enterprise pilot | Days; self-attested |
| Privacy basics (GDPR/UK GDPR, state laws) | When you process personal data of people in those jurisdictions, regardless of size | Policies, records, DPAs; counsel review |
| SOC 2 Type 1 | Enterprise buyer or investor asks for an independent report; you need something fast | Vendor ranges below |
| SOC 2 Type 2 | Buyers want evidence controls operated over time | Vendor ranges below |
| ISO 27001 | EU/UK/international buyers who ask for certification | Vendor ranges below |
| Sector regimes (HIPAA, PCI DSS, etc.) | Only if you touch health data or card data directly | Seek specialist advice; not covered here |

### SOC 2 and "SOC 2-ready"
- **What it is (Fact):** An AICPA attestation against the Trust Services Criteria; Security is the required category, and Availability, Confidentiality, Processing Integrity and Privacy are optional. In September 2022 the AICPA revised the points of focus without altering the 2017 criteria ([Baker Tilly, 2022, search snippet](https://www.bakertilly.com/insights/aicpa-releases-updated-soc-2-guide)). Type 1 reports on design at a point in time; Type 2 reports operating effectiveness over a period.
- **"SOC 2-ready" (Inference):** the controls in section 2 are operating, the minimal policy set below is written and followed, you collect evidence (screenshots/exports of access reviews, backups, MFA, offboarding), and you can scope to Security only.
- **Timelines and costs (Vendor-sourced; treat as ranges):** Drata, a compliance-automation vendor, quotes Type 1 at 3-6 months and USD 7,500-60,000, and Type 2 at 6-15 months and USD 12,000-100,000+, with an observation window of 3-12 months (3 minimum for most auditors, 6 common for a first report) ([Drata, accessed 2026-11-11](https://drata.com/grc-central/soc-2/type-1-vs-type-2)). Drata's figures are unsourced and promotional. Another vendor-side guide estimates 2-4 months to audit-ready with basic controls and 6-12 months from scratch ([Startup Defense, search snippet](https://www.startupdefense.io/soc-2-costs-for-startups-complete-breakdown-and-budget-guide)). Search results also showed Type 1 starts as low as USD 5,000 and Type 2 as high as USD 450,000 for Big Four audits. **Estimate:** budget the audit fee plus a platform subscription plus your own time, and get two or three auditor quotes.
- **Common path (vendor advice):** Type 1 first to unblock a deal, then start the Type 2 window with the same auditor.

### ISO 27001
- Certification is by an accredited body, in two audit stages, with a three-year certificate plus annual surveillance audits, per vendor guides that quote very wide timelines (about 3-18 months) and costs (single-digit thousands for the audit alone up to USD 40,000-180,000+ all-in) ([Drata ISO cost page](https://drata.com/grc-central/iso-27001/certification-cost) and other vendor pages, search snippets). **Inference:** more common in EU/UK/APAC procurement than in US startup deals; do it only if buyers name it.

### Privacy regimes
- **GDPR / UK GDPR (Fact):** apply based on whose data you process, not where you are. Core solo-founder tasks: a record of processing, a privacy notice, a lawful basis per purpose, data processing agreements with vendors, a way to handle access/deletion requests, and an internal breach log. The ICO says every personal data breach must be recorded, whether or not reportable ([ICO guide, accessed 2026-11-11](https://ico.org.uk/for-organisations/report-a-breach/personal-data-breach/personal-data-breaches-a-guide/)).
- **Other regimes (Inference):** US state privacy laws, sector rules, and country laws (for example India's) can apply; check with counsel based on where your users live.

### Minimal policy set (Inference; each 1-2 pages)
1. Information security policy (scope, owner, principles).
2. Access control and MFA policy (including offboarding and quarterly review).
3. Acceptable use and device policy (encryption, updates, personal devices).
4. Secrets and cryptography standard.
5. Secure development and change management (code review, CI checks, dependency updates).
6. Vendor management policy and inventory.
7. Backup and recovery policy with restore-test evidence.
8. Incident response plan (section 5).
9. Data classification, retention and deletion.
10. AI and agent use policy (approved tools, what data may be pasted, plugin vetting). IBM found 63% of breached organizations lacked AI governance policies ([IBM 2025](https://www.ibm.com/think/x-force/2025-cost-of-a-data-breach-navigating-ai)).

**So what for a solo founder:** Do the controls and a 10-page policy set now; buy an attestation only when a named deal or investor requires it, and get quotes rather than trusting vendor price pages.

---

## 5. Incident response for one person

CISA asks small businesses to have a written, reviewed incident response plan and to practise it with tabletop exercises ([CISA small business](https://www.cisa.gov/small-business)). Keep this one page where you can reach it if your laptop is dead (print it or store it in a second location).

### One-page runbook
1. **Detect:** Note time, source (alert, customer report, vendor notice, scanner), and what you saw. Start a timestamped log file now; write everything down.
2. **Contain:** Revoke sessions and tokens for affected accounts; disable the leaked key or compromised service account; isolate the affected host or deployment; pause CI if the pipeline is suspected. Prefer reversible steps; preserve logs and snapshots before wiping anything.
3. **Rotate:** Change credentials from a clean device, starting with email, registrar, source host, cloud root and payments, then the exposed secret and everything reachable by it. Re-issue hardware-key-based sessions. After the 2025 npm and `tj-actions` events CISA's advice was to rotate developer credentials and exposed secrets promptly ([CISA npm alert, search snippet](https://www.cisa.gov/news-events/alerts/2025/09/23/widespread-supply-chain-compromise-impacting-npm-ecosystem)).
4. **Assess:** What data and which customers were reachable? Pull provider audit logs for the exposure window. Decide whether personal data was accessed, altered, lost or disclosed. Record facts, effects and remedial action.
5. **Notify:** Decide who must be told (see clocks below), after confirming with counsel. Also tell affected vendors, your cyber insurer if you have one, and customers as needed.
6. **Learn:** Within two weeks, write a blameless post-incident note: timeline, root cause, what worked, control changes, owner and date for each. Update the runbook and the vendor/asset inventory.

### Breach-notification clocks (examples only; they vary by jurisdiction and facts; confirm with counsel)
- **GDPR / UK GDPR:** notify the supervisory authority without undue delay and, where feasible, within 72 hours of becoming aware, unless the breach is unlikely to risk individuals; give reasons if late; individuals must be told without undue delay if there is high risk ([ICO guide](https://ico.org.uk/for-organisations/report-a-breach/personal-data-breach/personal-data-breaches-a-guide/); [GDPR Art. 33 text, search snippet](https://gdpr-text.com/read/article-33/)). Information may be provided in phases. A processor alerts the controller without undue delay.
- **US states:** vary; secondary sources list 30 days for some states (for example California as of 2026-01-01, Colorado, Florida) and longer or "without unreasonable delay" elsewhere ([Coggno summary via search snippet](https://coggno.com/blog_tag/data); [Lewis Silkin guide, Oct 2026, search snippet](https://www.lewissilkin.com/insights/2026/10/30/mission-reportable-a-guide-to-the-many-cyber-reporting-deadlines)). Verify against the statute.
- **HIPAA:** individual notice no later than 60 calendar days after discovery, per a secondary summary ([TCSA, search snippet](https://www.tcsa.in/frameworks/hipaa-sra/breach-notification)); applies only if you are a covered entity or business associate.
- **EU NIS2 (if in scope):** early warning within 24 hours, fuller report within 72 hours, final report about a month later, per secondary summaries ([Opsio, search snippet](https://opsiocloud.com/in/blogs/cert-in-vs-nis2-incident-reporting/)). **India CERT-In:** 6 hours for specified incidents (same source). **Inference:** the shortest applicable clock sets your pace.
- Customer contracts and DPAs may set their own, shorter clocks (Open question: no source verified for typical values). Check each one.

### Communication templates (described in words)
- **Customer notice:** plain language; what happened and when; what data was involved (and what was not); what you have done; what the customer should do (rotate keys, watch for phishing); a named contact and next-update time. No speculation, no blame, no jargon.
- **Regulator notice:** facts known so far, nature and categories of data and approximate numbers, likely consequences, measures taken, contact details, and a statement that more will follow if phased. Have counsel review.
- **Vendor/partner notice:** which credentials or integrations may be affected, what you are rotating, and what you need from them (logs, key re-issue).
- **Investor/board update:** short and factual; impact, status, cost estimate, next steps.
- **Public status post:** only if customers are affected; same facts as the customer notice, no blame, scheduled updates.

**So what for a solo founder:** Write the runbook before you need it, make rotation the first move, and note the time you became "aware", because the notification clock may run from it.

---

## 6. Staged plan

### Day 1 (about 4 hours)
- Passkeys or hardware keys plus authenticator MFA on email, registrar, source host, cloud, payments.
- Install a password manager; move credentials in; store recovery codes offline.
- Enable disk encryption and auto-updates; stop using an admin account day to day.
- Turn on host secret scanning/push protection; scan current repos and history for secrets and rotate any hits.

### Week 1 (about 2 days)
- Least-privilege review; separate admin and daily identities; delete unused API keys and OAuth grants.
- Dependency alerts, lockfiles, SAST and secret scanning in CI; pin CI actions by SHA; reduce CI token permissions.
- Automate backups; do one restore test.
- Turn on audit logs and basic alerts.
- Start the vendor/SaaS inventory and device inventory.

### Month 1
- Write the 10 minimal policies (section 4); store them in a repo with change history.
- Write and rehearse the incident runbook (a one-hour tabletop alone or with an advisor).
- Add an AI/agent use policy; vet installed plugins, hooks and MCP servers.
- Create a questionnaire answer bank (a spreadsheet of standard questions with your honest answers and evidence links).
- Publish a security contact page (security.txt or a short page) and a privacy notice; get counsel review for privacy and breach duties.

### Quarter 1
- Run the first quarterly access review and restore drill; record evidence.
- Run OpenSSF Scorecard on public repos and fix the top findings.
- Decide on SOC 2/ISO 27001 using actual deal pipeline; collect two or three auditor quotes and one readiness-platform quote; compare with doing evidence collection manually.
- Review vendor DPAs and sub-processor lists; confirm breach-notification clauses.

### Checklist
- [ ] Hardware keys/passkeys on email, registrar, source host, cloud, payments
- [ ] Password manager in use; unique passwords; recovery codes stored offline
- [ ] Disk encryption, auto-updates, no daily admin account
- [ ] Least-privilege roles; unused keys and grants removed
- [ ] No secrets in git; push protection and pre-commit scanning on; rotation schedule set
- [ ] Dependency and container scanning running; lockfiles committed; CI actions pinned
- [ ] SAST and secret scan in CI; branch protection on default branch
- [ ] Backups automated, encrypted, off-account; restore tested and timed
- [ ] Audit logs on; alerts reach me
- [ ] Vendor/SaaS inventory and device inventory current
- [ ] 10 minimal policies written; AI/agent policy included
- [ ] Incident runbook written and rehearsed; counsel contacts noted
- [ ] Plugins, hooks, MCP servers reviewed; agent runs sandboxed with scoped credentials
- [ ] Questionnaire answer bank and evidence folder started

**So what for a solo founder:** One focused day gets you past the most likely failure, one focused month gets you a credible answer to a questionnaire, and a certification is a later, deal-driven decision.

---

## 7. Related in-repo skills and third-party options (by name only)

- **In-repo skills:** `secret-exposure-response` (for the leak-response steps in sections 2 and 5) and `data-protection-readiness` (for the privacy items in section 4).
- **Third-party plugins (options only; I have not verified or described their contents beyond their names and descriptions):** `security-scanning`, `security-compliance`, `compliance-os`. Review any plugin's hooks, scripts and MCP entries before installing (section 3).

---

## Open questions

- Primary Verizon DBIR text was not opened; the 2026 exploitation share (31% vs 36%) and the SMB 88% ransomware figure rest on secondary reports. Verify against the DBIR PDF.
- No verified breach-cost or breach-rate figure specific to one-person companies was found; IBM and Verizon averages skew large.
- IBM's 2026 initial-vector and time-to-contain figures were not on the page I opened; check the full report.
- Contract-driven notification clocks (customer DPAs) were not sourced.
- Whether ASVS 5.0 requirement counts (about 350, 17 chapters) and OpenSSF Scorecard weights match the current official docs.
- SOC 2/ISO price and timeline figures are vendor claims with no independent benchmark; get auditor quotes.
- Which secret-scanning features are free on your source host's plan was not verified.
- Whether SLSA v1.2 changes the level definitions quoted from v1.0.

---

## Sources (accessed 2026-11-11)

Pages marked (snippet) were seen only as search-result summaries, not opened in full.

1. [Verizon 2025 DBIR, EMEA release](https://www.verizon.com/about/news/2025-data-breach-investigations-report-emea) (published Apr 2025)
2. [Security Magazine, Verizon 2025 DBIR](https://www.securitymagazine.com/articles/101569-verizon-2025-data-breach-investigations-report-shows-rise-in-cyberattacks) (Apr 2025; snippet)
3. [Help Net Security, Verizon 2026 DBIR](https://www.helpnetsecurity.com/?p=371418) (May 2026)
4. [SecureWorld, Verizon DBIR 2026](https://www.secureworld.io/industry-news/verizon-dbir-attackers-moving-faster-than-remediation) (May 2026; snippet)
5. [IBM, 2025 Cost of a Data Breach](https://www.ibm.com/think/x-force/2025-cost-of-a-data-breach-navigating-ai) (Jul 2025)
6. [IBM, 2026 Cost of a Data Breach](https://www.ibm.com/think/x-force/2026-cost-of-a-data-breach-ai-adversaries-enterprise-risk) (29 Jul 2026)
7. [GitGuardian, State of Secrets Sprawl 2026](https://blog.gitguardian.com/the-state-of-secrets-sprawl-2026/) (17 Mar 2026; vendor)
8. [OWASP Top 10:2025](https://top10.owasp.org/2025) (no release date on page; announced Nov 2025 per search results)
9. [CISA, Cyber Guidance for Small Businesses](https://www.cisa.gov/small-business)
10. [CISA, tj-actions/changed-files compromise alert](https://www.cisa.gov/news-events/alerts/2025/03/18/supply-chain-compromise-third-party-github-action-cve-2025-30066) (Mar 2025, updated 2025-03-26)
11. [CISA, npm ecosystem supply chain compromise](https://www.cisa.gov/news-events/alerts/2025/09/23/widespread-supply-chain-compromise-impacting-npm-ecosystem) (23 Sep 2025; snippet)
12. [Claude Code security documentation](https://code.claude.com/docs/en/security)
13. [Snyk, ToxicSkills](https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/) (Feb 2026; snippet; vendor)
14. [arXiv 2603.16572, agent skills study](https://arxiv.org/html/2603.16572v1) (Mar 2026; snippet)
15. [Palo Alto Networks, OWASP Agentic Top 10 2026](https://paloaltonetworks.com/blog/cloud-security/owasp-agentic-ai-security/) (snippet; vendor)
16. [SoftwareMill, what's new in ASVS 5.0](https://softwaremill.com/whats-new-in-asvs-5-0/) (2025; snippet) and [OWASP ASVS repository](https://github.com/OWASP/ASVS)
17. [SLSA v1.0 levels](https://slsa.dev/spec/v1.0/levels) (snippet)
18. [OpenSSF Scorecard repository](https://github.com/ossf/scorecard) (snippet)
19. [Drata, SOC 2 Type 1 vs Type 2](https://drata.com/grc-central/soc-2/type-1-vs-type-2) (vendor)
20. [Startup Defense, SOC 2 costs for startups](https://www.startupdefense.io/soc-2-costs-for-startups-complete-breakdown-and-budget-guide) (snippet; vendor)
21. [Baker Tilly, AICPA updated SOC 2 guide](https://www.bakertilly.com/insights/aicpa-releases-updated-soc-2-guide) (2022; snippet)
22. [Drata, ISO 27001 certification cost](https://drata.com/grc-central/iso-27001/certification-cost) (snippet; vendor)
23. [ICO, personal data breaches guide](https://ico.org.uk/for-organisations/report-a-breach/personal-data-breach/personal-data-breaches-a-guide/)
24. [GDPR Article 33 text](https://gdpr-text.com/read/article-33/) (snippet)
25. [Lewis Silkin, cyber reporting deadlines](https://www.lewissilkin.com/insights/2026/10/30/mission-reportable-a-guide-to-the-many-cyber-reporting-deadlines) (30 Oct 2026; snippet) and [Coggno summary](https://coggno.com/blog_tag/data) (snippet)
26. [TCSA, HIPAA breach notification](https://www.tcsa.in/frameworks/hipaa-sra/breach-notification) (snippet) and [Opsio, CERT-In vs NIS2](https://opsiocloud.com/in/blogs/cert-in-vs-nis2-incident-reporting/) (snippet)
27. [Microsoft Research, MFA effectiveness (arXiv 2305.00945)](https://arxiv.org/abs/2305.00945) (2023; snippet)
28. [GitHub Docs, removing sensitive data](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository) (snippet)
29. [The Hacker News, tj-actions compromise](https://thehackernews.com/2025/03/cisa-warns-of-active-exploitation-in.html) (Mar 2025; snippet) and [CERT/CC VU#534320](https://kb.cert.org/vuls/id/534320) (snippet)

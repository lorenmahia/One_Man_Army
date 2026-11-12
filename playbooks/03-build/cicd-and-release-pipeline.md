# CI/CD and Release Pipeline: Fortune-500 Discipline at Solo-Founder Scale

> Last verified: 2026-11-11. Research and planning support only; not legal, tax, investment or financial advice.

## Summary

- **Enterprise-grade delivery is a set of habits, not a toolchain.** Small batches, an always-releasable main branch, automated checks, short-lived credentials and fast rollback are all available on free tiers of common tools (Inference, from the sources below).
- **Protect main and use pull requests even when solo.** A required-checks gate is your "second reviewer"; GitHub lets you require status checks, linear history and block force pushes ([About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches), accessed 2026-11-11).
- **Pin third-party actions to full commit SHAs, set read-only token permissions, and use OIDC instead of stored cloud keys.** All three are in GitHub's own hardening and OIDC docs ([Secure use reference](https://docs.github.com/en/actions/reference/security/secure-use); [OIDC in AWS](https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments/oidc-in-aws)).
- **Measure five DORA metrics, but treat published benchmarks as context, not targets.** DORA now lists five software delivery metrics, and its cluster thresholds change by year ([DORA metrics guide](https://dora.dev/guides/dora-metrics/); [Octopus summary of 2024 clusters](https://octopus.com/blog/2024-devops-performance-clusters)).
- **Adopt in stages:** Day 1 protect main plus CI; Week 1 add scanning and a deploy with rollback; Month 1 add environments, OIDC and uptime alerts; Quarter 1 add IaC, flags and DORA tracking.

---

## 1. What "enterprise-grade" means, and what is near-zero cost

**Inference:** Large companies differ from a solo founder mainly in headcount and approvals, not in the underlying properties. Those properties are: every change is traceable, nothing reaches production without passing automated checks, secrets are scoped and short-lived, and you can undo a bad release quickly. A solo founder can have all four with free or low-cost tooling.

### Source control hygiene
- **One repo per deployable unit, default branch always releasable.** **Fact:** The trunk-based development site describes a single shared trunk, short-lived feature branches, and the CI expectation that each developer integrates to trunk at least once per 24 hours ([Trunk Based Development](https://trunkbaseddevelopment.com/), accessed 2026-11-11). It says very small teams may commit straight to trunk but gives no fixed branch lifetime.
- **Trunk-based vs branching.** **Inference:** For one person, trunk-based with short-lived branches (hours to a couple of days) and a pull request per change beats long-lived `develop`/`release` branches. Long-lived branches add merge cost with no second reader to justify them. Use a release branch only if you must patch an old version that customers still run.
- **Protect the default branch.** **Fact:** GitHub branch protection offers required pull requests, required status checks (strict mode requires the branch to be up to date), signed-commit requirements, linear history, and force-push blocking; only one branch protection rule applies to a branch at a time, which does not apply to rulesets ([About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches), accessed 2026-11-11).
- **Pull requests even when solo.** **Inference:** A PR gives CI a place to run, gives you a diff to re-read before merge, and leaves a durable record. Do not require an approving review if you are the only collaborator (you cannot approve your own PR); require the status checks instead. Whether free private repositories can enforce each rule is not confirmed here (see Open questions).
- **Conventional commits and changelogs.** **Fact:** Conventional Commits uses `<type>[scope]: <description>`; `fix` maps to a PATCH release, `feat` to MINOR, and a `!` or `BREAKING CHANGE:` footer to MAJOR ([Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/), accessed 2026-11-11). **Inference:** Squash-merge with a conventional PR title so history is machine-readable and release notes can be generated.

**So what for a solo founder:** Spend 30 minutes now to protect main and require CI; it is the cheapest control that makes every later control enforceable.

---

## 2. Pipeline stages and a minimal GitHub Actions layout

### Stages and their jobs

| Stage | Purpose | Runs on |
|---|---|---|
| Lint / format | Fast style and static-analysis gate (seconds) | every PR |
| Unit tests | Logic correctness; keep under ~5 minutes (**Estimate**, a common working target, not a sourced standard) | every PR |
| Build | Produce one immutable artifact (container image or bundle) | every PR; publish on main |
| Dependency scan | Flag vulnerable libraries and outdated actions | PR + weekly schedule |
| Secret scan | Block credentials before they land | push (push protection) + PR |
| Integration tests | Real database/queue in containers; contract tests for external APIs | PR or main |
| Preview / staging | Deploy the same artifact to a non-production environment and smoke-test | main (or PR previews if your host supports them) |
| Production deploy | Promote the same artifact; gated by environment rules | tag or manual approval |
| Rollback | Redeploy previous artifact or flip a flag; rehearsed | on demand |

**Fact:** Dependabot can keep GitHub Actions references updated. Its options reference shows `package-ecosystem: "github-actions"`, `directory: "/"`, a schedule interval and an optional `cooldown` block that delays version updates after a release ([Dependabot options reference](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/dependabot-options-reference), accessed 2026-11-11). The page states Dependabot does not raise vulnerability alerts for SHA-pinned actions ([Secure use reference](https://docs.github.com/en/actions/reference/security/secure-use)), so schedule version updates for them.

**Fact:** Secret-scanning push protection is documented as available for public repositories on GitHub.com; for private repositories, availability depends on a paid GitHub Secret Protection product (search snippet only: [About push protection](https://docs.github.com/en/code-security/concepts/secret-security/about-push-protection); [GitHub blog, May 2023](https://github.blog/changelog/2023-05-09-secret-scannings-push-protection-is-available-on-public-repositories-for-free)). A third-party article says the products were split in 2025; treat packaging details as unverified. Free alternatives for private repos (a pre-commit scanner such as gitleaks, run in CI) are an **Inference**; verify before relying.

### Workflow files (suggested layout)

- `.github/workflows/ci.yml` - trigger `pull_request` (branches: main) and `push` to main. Jobs: lint, test, build, scan.
- `.github/workflows/deploy.yml` - trigger `push` of tags matching `v*` (and optionally `workflow_dispatch` for manual redeploys/rollbacks). Jobs: deploy-staging, then deploy-production using a protected environment.
- `.github/workflows/scheduled.yml` - trigger `schedule` (cron) for weekly dependency/security scans and an infrastructure drift `plan`.
- `.github/dependabot.yml` - weekly updates for your language ecosystem and `github-actions`.

**Fact (syntax verified against [Workflow syntax reference](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax), accessed 2026-11-11):** `on.pull_request.branches`, `on.push.tags`, `on.workflow_dispatch` (only fires from the default branch's workflow file), top-level `permissions:` (any permission you list sets the unlisted ones to `none`) and `concurrency:` with `group` and `cancel-in-progress` are all valid as shown below.

```yaml
# .github/workflows/ci.yml  (sketch; replace placeholders)
name: ci
on:
  pull_request:
    branches:
      - main
permissions:
  contents: read            # least privilege: read-only token
concurrency:
  group: ci-${{ github.ref }}
  cancel-in-progress: true  # cancel superseded runs on the same ref
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@<FULL_40_CHAR_SHA>   # vX.Y.Z (look up and verify the SHA yourself)
      - run: echo "replace with your lint, test and build commands"
```

```yaml
# .github/workflows/deploy.yml  (trigger sketch only)
name: deploy
on:
  push:
    tags:
      - 'v*'
permissions:
  contents: read
```

### Why pin by commit SHA
**Fact:** GitHub says pinning to a full-length commit SHA is the way to treat an action as immutable; tags can be moved or deleted if the action's repository is compromised, and the SHA should come from the original repo rather than a fork ([Secure use reference](https://docs.github.com/en/actions/reference/security/secure-use), accessed 2026-11-11). The same page notes a workflow lockfile may supersede SHA pinning where adopted. A search-result write-up attributes the March 2025 tj-actions/changed-files compromise to rewritten tags (secondary source; snippet only). Add a trailing comment with the human-readable version, and let Dependabot propose SHA bumps.

Also from that page: default the `GITHUB_TOKEN` to read-only, avoid `pull_request_target`/`workflow_run` with untrusted checkouts, store each secret as its own value, delete logs and rotate if a secret leaks.

**So what for a solo founder:** A ~40-line CI file, SHA-pinned, with read-only permissions, gives you most of the gate; add the deploy workflow only once CI is trusted.

---

## 3. Environments, secrets and configuration

- **Environment-scoped secrets.** **Fact:** GitHub environments support required reviewers (up to 6), wait timers, branch/tag deployment restrictions, and environment secrets/variables available only to jobs that use the environment after protection rules pass ([Managing environments](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments), accessed 2026-11-11). **Fact:** On the Free plan, environments can be configured only for public repositories; private repositories need Team or Pro, and if a repo goes public-to-private its rules and environment secrets are ignored (same page). **Inference:** As a solo founder, leave "prevent self-review" off or you cannot approve your own deploys; use a wait timer and branch restrictions instead.
- **OIDC to cloud instead of long-lived keys.** **Fact:** Grant `id-token: write` (it only lets the job request a token, not write to resources) plus `contents: read`, and use the cloud provider's credentials action to exchange the token for short-lived credentials. The AWS page requires a trust-policy condition on `aud` and `sub`; for environments the `sub` takes the form `repo:ORG/REPO:environment:NAME`, wildcards are discouraged, and repositories created after July 15, 2026 or that opt in use a `sub` format that includes owner and repository IDs ([OIDC in AWS](https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments/oidc-in-aws), accessed 2026-11-11). Match your trust policy to your repo's format.

```yaml
# Adapted from GitHub's OIDC-in-AWS sample; placeholders in CAPS
permissions:
  id-token: write   # required for requesting the JWT
  contents: read    # required for actions/checkout
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@<FULL_40_CHAR_SHA>   # vX.Y.Z
      - uses: aws-actions/configure-aws-credentials@<FULL_40_CHAR_SHA>   # vX.Y.Z
        with:
          role-to-assume: ROLE-TO-ASSUME
          aws-region: AWS-REGION
```

- **Never commit secrets.** **Fact:** 12-factor config guidance is strict separation of config from code, with an open-source litmus test: could the codebase be published without leaking credentials ([The Twelve-Factor App: Config](https://12factor.net/config), search snippet only, accessed 2026-11-11). **Inference:** Keep `.env` in `.gitignore`, commit a `.env.example` with fake values, enable push protection where available, and run a scanner in CI.
- **Rotation basics.** **Fact:** GitHub advises rotating secrets periodically, removing unused ones, and rotating immediately if one appears unredacted in a log ([Secure use reference](https://docs.github.com/en/actions/reference/security/secure-use)). **Inference:** Prefer OIDC (nothing to rotate); for remaining keys (payment, email, third-party APIs) keep an inventory with owner, scope and a 90-day review date (the 90 days is a convention, not a sourced requirement). If a secret leaks, use the in-repo skill `secret-exposure-response`.

**So what for a solo founder:** Replace every long-lived cloud key in CI with OIDC first; it removes the most damaging secret you could leak.

---

## 4. Release management

- **Semantic versioning.** **Fact:** SemVer 2.0.0 uses MAJOR.MINOR.PATCH (incompatible API change, backward-compatible feature, backward-compatible fix); 0.y.z is initial development; a released version must never be modified ([Semantic Versioning 2.0.0](https://semver.org/), accessed 2026-11-11). **Inference:** For a SaaS with no public API, SemVer is mostly a labelling convention; use tags for traceability and map conventional commits to bumps.
- **Tags and releases.** Tag `vX.Y.Z` on main; the tag triggers the deploy workflow; the GitHub Release holds generated notes. Deploy the exact artifact that passed CI (**Inference**: build once, promote many).
- **Feature flags.** **Fact:** Fowler and Hodgson classify toggles as release (days to weeks), experiment, ops (including long-lived kill switches) and permissioning; they treat toggles as inventory with carrying cost and suggest expiry dates, removal tasks and a cap on toggle count; the same artifact should be tested with toggles on and off ([Feature Toggles](https://martinfowler.com/articles/feature-toggles.html), accessed 2026-11-11; undated article, long-established guidance). Start with a config-file or environment-variable flag before buying a flag service.
- **Blue-green / canary at small scale.** **Fact:** Blue-green runs two identical environments and switches the router; rollback is switching back, with the gap being transactions handled by the new side ([Blue Green Deployment](https://martinfowler.com/bliki/BlueGreenDeployment.html), accessed 2026-11-11; undated). **Inference:** Many small hosts give this for free as instant rollback to a previous build. A canary can be a flag enabled for your own account, then 5-10% of users (the percentages are illustrative, not sourced). You do not need a service mesh.
- **Database migrations safety.** **Fact:** Parallel change (expand, migrate, contract) lets old and new coexist until clients move, but the contract step must actually be completed ([Parallel Change](https://martinfowler.com/bliki/ParallelChange.html), accessed 2026-11-11). Fowler's blue-green article advises deploying schema changes separately from app upgrades, with a version that supports both old and new app code, then removing old support after stability. **Inference:** Rules of thumb: additive migrations only in the release that ships code; never drop or rename a column in the same release; take a backup or snapshot before migrating; test migrations against a copy of production-shaped data.
- **Rollback rehearsal.** **Inference:** Once a month, deliberately roll staging back to the previous tag and time it. An untested rollback is a hope, not a control.

**So what for a solo founder:** Make every release reversible: build once, tag it, keep the previous artifact deployable, and split risky schema changes across two releases.

---

## 5. Measuring delivery performance (DORA)

**Fact:** DORA's current guide lists five software delivery metrics, grouped into throughput (change lead time, deployment frequency, failed deployment recovery time) and instability (change fail rate, deployment rework rate); the guide page itself gives no benchmarks ([DORA metrics guide](https://dora.dev/guides/dora-metrics/), page "last updated January 5, 2026", accessed 2026-11-11). A RedMonk write-up lists the fifth as a rework rate added in 2024 and describes time to restore as moved into throughput; this is a secondary source ([RedMonk on DORA 2025](https://redmonk.com/rstephens/2025/12/18/dora2025/), accessed 2026-11-11).

**Fact:** DORA's 2025 year-in-review states that AI improves throughput but often at the cost of stability if the foundation is not solid, and lists a DORA AI Capabilities Model (December 2025) with seven capabilities ([DORA 2025 year in review](https://dora.dev/insights/dora-2025-year-in-review/), accessed 2026-11-11). This matters if you generate much code with AI: keep the test and review gates strict.

### What "good" looked like (2024 clusters)
These figures come from a secondary summary of the 2024 report; the 2024 PDF was too large for my fetch tool and I did not read it directly. They are now two years old, so treat them as **dated** on a fast-moving topic.

| Cluster | Lead time | Deploy frequency | Change failure rate | Time to recover |
|---|---|---|---|---|
| Elite | under 1 day | on demand | 5% | under 1 hour |
| High | 1 day - 1 week | daily - weekly | 20% | under 1 day |
| Medium | 1 week - 1 month | weekly - monthly | 10% | under 1 day |
| Low | 1 - 6 months | monthly - biannually | 40% | 1 week - 1 month |

Source: [Octopus, 2024 DevOps performance clusters](https://octopus.com/blog/2024-devops-performance-clusters) (accessed 2026-11-11). The table shows medium with a lower failure rate (10%) than high (20%), as the summary reports it; I did not verify this against the PDF. A snippet from other summaries gives respondent shares of 19% elite, 22% high, 35% medium and 25% low ([search snippet, DLS Thoughts](https://dlsthoughts.substack.com/p/doras-state-of-devops-in-2024)); Octopus says only that elite is under 20% of organizations. Another summary notes cluster definitions are re-derived each year, so thresholds are not fixed ([DX newsletter, search snippet](https://newsletter.getdx.com/p/2024-dora-report)). **Open:** a search summary says the 2025 report replaced performance tiers with seven team archetypes (only two names confirmed by RedMonk).

### Cheap tracking for one person
**Inference** (no source prescribes this):
- **Deployment frequency:** count GitHub Releases/tags or successful deploy runs per week.
- **Lead time:** merge time (or first commit time) to deploy-success time; the Actions run log and PR metadata have both timestamps.
- **Change failure rate:** label any release that needed a rollback, hotfix or flag-off as `failed-release`; divide by releases.
- **Time to restore:** alert timestamp to recovery timestamp, recorded in a one-line incident note.
- **Rework rate:** count unplanned deploys triggered by a production incident (per DORA's definition above).
- Record in a spreadsheet or a small script run from the scheduled workflow; review monthly. With a sample of a few releases a month, the percentages are noisy; read trends, not decimals (**Inference**).

**So what for a solo founder:** Track the five numbers monthly in a spreadsheet; aim at direction of travel, not at elite labels.

---

## 6. Infrastructure as code, cost guardrails and observability

### IaC and reproducibility
- **Inference:** Put infrastructure (hosting, DNS, database, buckets, IAM roles for OIDC) in version-controlled code, with remote state and locking, so a lost laptop or an account mistake is recoverable. Pin tool and provider versions; commit lockfiles; use containers or a devcontainer for identical local and CI builds.
- **Tool choice.** **Fact (vendor-heavy sources):** Terraform is under the Business Source License 1.1, OpenTofu is Linux Foundation governed with an MPL 2.0 core; state formats are broadly portable except for HashiCorp's hosted backend ([Encore comparison, Oct 2026](https://encore.dev/articles/opentofu-vs-terraform-2026) and related snippets, accessed 2026-11-11). **Inference:** For internal use either works; the licence change mainly affects vendors who build on it. Managed-platform users may prefer their provider's native IaC.
- **Drift:** A scheduled `plan` in CI that fails on unexpected changes is a low-cost drift check (suggested in the same search results; a vendor-source **Inference**).
- **Supply-chain provenance (optional later).** **Fact:** `actions/attest-build-provenance` v4 wraps `actions/attest`, which new workflows should use; attestations in private repositories need GitHub Enterprise Cloud; sources disagree on whether the basic setup reaches SLSA Build Level 2 or 3 ([GitHub attest-build-provenance repo](https://github.com/actions/attest-build-provenance); [GitHub blog on SLSA Level 3](https://github.blog/enterprise-software/devsecops/enhance-build-security-and-reach-slsa-level-3-with-github-artifact-attestations/); search snippets only, accessed 2026-11-11).

### Cost guardrails
- **Fact:** GitHub Free includes 2,000 Actions minutes per month for private repositories, with 500 MB artifact storage; standard hosted runners are free for public repositories; the default spending limit for monthly-billed accounts is 0 USD ([About billing for GitHub Actions](https://docs.github.com/en/billing/managing-billing-for-github-actions/about-billing-for-github-actions), search snippet, accessed 2026-11-11). A news item reports a 2026 pricing change affecting self-hosted runner usage; unverified (Open questions).
- **Fact:** AWS's tutorial recommends a total monthly cost budget with an alert (its example uses 80% of the amount) and notes Free Tier usage alerts are separate ([AWS: Control your costs with Free Tier budgets](https://aws.amazon.com/getting-started/hands-on/control-your-costs-free-tier-budgets), search snippet, accessed 2026-11-11). Other clouds have equivalents; confirm in their docs.
- **Inference:** Set a budget alert on day one on every cloud account and AI/API vendor; cap `concurrency` and use `cancel-in-progress` to avoid wasting minutes; set a spend limit on any usage-billed vendor; tag resources by environment.

### Observability for one person on call
- **Inference** (basic set): structured logs with request IDs; a handful of metrics (request rate, error rate, latency, saturation, queue depth); an external uptime check on the homepage and one critical API/health endpoint; error tracking; alerts routed to a phone push, not email.
- **Alert on symptoms, not causes.** **Fact:** The Google SRE Workbook's multiwindow, multi-burn-rate approach pairs a long and short window (short about one-twelfth of long) and fires only when both exceed a burn-rate threshold; one summary cites 1h/5min at 14.4x and 6h/30min at 6x as page-level tiers, with other summaries differing on tiers ([SRE Workbook: Alerting on SLOs](https://sre.google/workbook/alerting-on-slos/), chapter not opened; figures from search snippets, accessed 2026-11-11). **Inference:** For one person, start simpler: page only on "site down" or "error rate above X% for 5 minutes"; ticket everything else; review alert noise weekly, because every false page wears down your only on-call engineer.
- **Runbook.** Keep a one-page runbook per critical failure (deploy rollback, database restore, rotate a leaked key) next to the code.

**So what for a solo founder:** Codify infrastructure, set budget alerts before spend surprises you, and page yourself only for user-visible outages.

---

## 7. Staged adoption plan

| Horizon | Do this | Done when |
|---|---|---|
| **Day 1** | Create repo hygiene: `.gitignore`, `.env.example`; protect main (PR + required checks + no force push); `ci.yml` with lint, test, build; read-only `permissions:`; Dependabot config; enable push protection / secret scan if available; budget alert on cloud account | A PR cannot merge unless CI is green |
| **Week 1** | SHA-pin all actions; add dependency scan; staging deploy on merge; production deploy by tag with one-click rollback; uptime check + phone alert; document rollback in a runbook | You can ship and undo a release in under 15 min (**Estimate**, self-set target) |
| **Month 1** | Environments with scoped secrets and branch restrictions; OIDC replaces cloud keys; integration tests with real DB; first flag; conventional commits and generated release notes; first rollback rehearsal; start DORA spreadsheet | No long-lived cloud key in CI; rehearsed rollback timed |
| **Quarter 1** | IaC with remote state and scheduled drift plan; expand/contract discipline for migrations; SLO-based alerts; monthly DORA review; evaluate artifact attestations and OpenSSF Scorecard; quarterly secret rotation and access review | Metrics trend reviewed three months running |

**OpenSSF Scorecard (optional check).** **Fact (snippets):** Scorecard includes Branch-Protection, Pinned-Dependencies and Token-Permissions checks, scoring each 0-10 ([OpenSSF Scorecard FAQ/mirror](https://securityscorecards.dev), search snippets only, accessed 2026-11-11). It is a handy external audit of the controls above on public repositories.

**So what for a solo founder:** Do Day 1 today; do not build Quarter 1 items until Week 1 and Month 1 items are boring.

---

## 8. Pointers (by name only)

- **In-repo skill:** `secret-exposure-response` - use when a credential may have been committed or logged.
- **Third-party plugins (options; contents not verified here):** `cicd-automation`, `deployment-strategies`, `observability-monitoring`, `security-scanning`, `superpowers`. Review each plugin's own description and permissions before installing; this playbook makes no claims about what they contain.

---

## Checklist

- [ ] Default branch protected: PR required, required status checks, force pushes blocked
- [ ] Squash merge with conventional-commit titles
- [ ] `ci.yml` runs lint, tests, build on every PR; read-only `permissions:` at top
- [ ] Every third-party action pinned to a full commit SHA with a version comment
- [ ] Dependabot enabled for code dependencies and GitHub Actions
- [ ] Secret scanning / push protection (or CI scanner) active; `.env` ignored
- [ ] Production deploy triggered by version tag; same artifact as staging
- [ ] Environments with scoped secrets; OIDC instead of long-lived cloud keys
- [ ] Migrations follow expand/migrate/contract; backup taken before migration
- [ ] Previous release redeployable; rollback rehearsed and timed
- [ ] Feature flags have an owner and an expiry date
- [ ] Uptime check and phone alert live; one-page runbooks exist
- [ ] Budget alerts on all cloud and usage-billed vendors
- [ ] Five DORA metrics recorded monthly
- [ ] Leak procedure known (`secret-exposure-response`)

## Open questions

- Which branch protection and ruleset features (required checks, linear history) are enforceable on private repos on GitHub Free in 2026? Not confirmed; verify in your repo's settings.
- Current status and amount of GitHub Actions free minutes and any 2026 pricing change for self-hosted runners (a news snippet mentions a change; official docs not read in full).
- Exact 2024 DORA cluster figures (primary PDF not read) and the 2025 archetype names and any 2025 numeric benchmarks.
- Whether secret scanning push protection is available free for private repositories (snippet suggests paid product).
- Whether the SRE Workbook's alert tiers match the figures in search snippets (chapter not opened).
- Current latest versions and SHAs of `actions/checkout` and the cloud credential actions: look them up yourself; none are stated here.
- Whether job-level `environment:` syntax matches the docs exactly (the workflow-syntax page section was not visible in my fetch); check the docs before use.

## Sources

Access date for all: 2026-11-11. "Opened" means fetched and read; "snippet" means seen only in search results.

1. [DORA metrics guide](https://dora.dev/guides/dora-metrics/) - opened.
2. [DORA 2025 year in review](https://dora.dev/insights/dora-2025-year-in-review/) - opened.
3. [RedMonk on DORA 2025](https://redmonk.com/rstephens/2025/12/18/dora2025/) - opened (secondary).
4. [Octopus: 2024 DevOps performance clusters](https://octopus.com/blog/2024-devops-performance-clusters) - opened (secondary).
5. [DLS Thoughts on DORA 2024](https://dlsthoughts.substack.com/p/doras-state-of-devops-in-2024) - snippet (secondary).
6. [DX newsletter on DORA 2024](https://newsletter.getdx.com/p/2024-dora-report) - snippet (secondary).
7. [GitHub Docs: About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) - opened.
8. [GitHub Docs: Secure use reference](https://docs.github.com/en/actions/reference/security/secure-use) - opened.
9. [GitHub Docs: OIDC in AWS](https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments/oidc-in-aws) - opened.
10. [GitHub Docs: Managing environments](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments) - opened.
11. [GitHub Docs: Workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax) - opened (first 100,000 characters).
12. [GitHub Docs: Dependabot options reference](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/dependabot-options-reference) - opened (first 100,000 characters).
13. [GitHub Docs: About push protection](https://docs.github.com/en/code-security/concepts/secret-security/about-push-protection) - snippet.
14. [GitHub changelog, 2023-05-09](https://github.blog/changelog/2023-05-09-secret-scannings-push-protection-is-available-on-public-repositories-for-free) - snippet.
15. [GitHub Docs: About billing for GitHub Actions](https://docs.github.com/en/billing/managing-billing-for-github-actions/about-billing-for-github-actions) - snippet.
16. [actions/attest-build-provenance](https://github.com/actions/attest-build-provenance) - snippet.
17. [GitHub blog: SLSA Level 3 with artifact attestations](https://github.blog/enterprise-software/devsecops/enhance-build-security-and-reach-slsa-level-3-with-github-artifact-attestations/) - snippet.
18. [Trunk Based Development](https://trunkbaseddevelopment.com/) - opened.
19. [Semantic Versioning 2.0.0](https://semver.org/) - opened.
20. [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/) - opened.
21. [Fowler: Feature Toggles](https://martinfowler.com/articles/feature-toggles.html) - opened.
22. [Fowler: Blue Green Deployment](https://martinfowler.com/bliki/BlueGreenDeployment.html) - opened.
23. [Fowler: Parallel Change](https://martinfowler.com/bliki/ParallelChange.html) - opened.
24. [The Twelve-Factor App: Config](https://12factor.net/config) - snippet.
25. [Encore: OpenTofu vs Terraform 2026](https://encore.dev/articles/opentofu-vs-terraform-2026) - snippet (vendor).
26. [AWS: Control your costs with Free Tier budgets](https://aws.amazon.com/getting-started/hands-on/control-your-costs-free-tier-budgets) - snippet.
27. [Google SRE Workbook: Alerting on SLOs](https://sre.google/workbook/alerting-on-slos/) - snippet only (chapter not opened).
28. [OpenSSF Scorecard](https://securityscorecards.dev) - snippet.

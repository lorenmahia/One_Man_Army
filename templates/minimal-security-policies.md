# Minimal Security Policies

> Template. Research and planning support only; not legal, tax, investment or financial advice.

Short outlines for a minimal policy set for a one-person company. The playbook's full list has ten policies of 1-2 pages each (an Inference); this template covers the seven you are most likely to be asked about in customer questionnaires: access control, secrets, device, backup, incident, vendor, and AI/agent use. Each is a set of commitments to adapt: delete what you will not do, because an unkept policy is worse than none. Buy an attestation only when a named deal or investor requires it.

Owner: `[you]`   Version: `[ ]`   Date: `[YYYY-MM-DD]`   Review: at least annually

## 1. Access control

- Passkeys or FIDO2 keys on email, registrar, source host, cloud, payments and the password manager; authenticator-app TOTP as fallback; no SMS where avoidable.
- Priority accounts: primary email and domain registrar first (they reset everything else).
- Separate admin identity for cloud consoles; day-to-day work with a non-root role; never use root/owner for CI.
- Per-service API keys with minimum scopes; review access and OAuth grants quarterly and remove unused ones.
- Offboarding (contractors, tools) revokes access the same day: `[ ]`.

## 2. Secrets

- Secrets never in git; use a secrets manager or CI secret store; commit only `.env.example` placeholders.
- Pre-commit secret scanner on; host secret scanning and push protection on where available.
- Prefer short-lived credentials (OIDC from CI to cloud); rotate long-lived keys at least annually and immediately on suspicion, contractor departure or vendor breach.
- After a leak: rotate first, check logs, then clean history.

## 3. Device

- Full-disk encryption, automatic OS and browser updates, screen lock.
- No admin rights for daily use; separate browser profile for admin consoles.
- One-line device inventory (for questionnaires): `[ ]`.
- Personal-device rules: `[allowed / not allowed, and conditions]`.

## 4. Backup

- Automated backups of databases, object storage and configuration (infrastructure as code); encrypted.
- At least one copy in a different account or provider, with versioning or write-once where available.
- Restore test into a scratch environment, timed, quarterly; keep the evidence.
- Documented restoration plan: `[location]`.

## 5. Incident

- A written one-page runbook (detect, contain, rotate, assess, notify, learn) stored in two places.
- Log the time of awareness; confirm notification duties with counsel.
- Blameless post-incident note within two weeks.
- Practise with a tabletop exercise `[frequency]`.

## 6. Vendor

- One inventory: vendor, purpose, data held, account owner, MFA status, DPA/contract link, security page or attestation link, renewal date.
- Include AI tools and agent plugins.
- Review annually and before sharing customer data with a new vendor.
- Check each vendor's breach-notice duty to you.

## 7. AI and agent use

- Approved tools: `[list]`; data that may never be pasted into them: `[customer data / secrets / ...]`.
- Treat the agent, its plugins and MCP servers as privileged insiders: read hooks, scripts and MCP entries before enabling; pin versions; install only from sources you can inspect.
- Keep secrets out of the agent's working directory and environment; use scratch accounts or short-lived scoped tokens.
- Human approval for pushes, deploys, external messages and anything touching money or customer data.
- Scan agent output with the same secret scanner and SAST as human code.

## Example commitment line (ILLUSTRATIVE)

"Restore test: last done `[date]`, took `[minutes]`, result `[pass / fail]`, next due `[date]`." Fill with real values or remove the claim.

Source playbook: [Security and secrets baseline for a one-person startup](../playbooks/03-build/security-and-secrets-baseline.md)

# Data Protection Readiness

> A country-specific checklist for data-controller registration, consent, retention and breach response, with links to the regulator to confirm each point.

For products that collect personal or financial data. It names the regulator, works out whether you are a controller or a processor, and walks through the compliance basics. Each item is marked done, not started, or unclear.

**Not legal advice.** Requirements change; confirm with the regulator and a local lawyer.

## When to use it

- "My app collects users' bank details in Nigeria. What do I need to register?"
- "Do I need to register as a data controller in Kenya and the UK?"
- "What should my consent screen say?"

## What it covers

1. Which country's rules apply (both, if company and users are in different countries)
2. The data protection authority, its registration page, and the fee or how to confirm it
3. Controller vs. processor, feature by feature
4. Lawful basis for each data use, and what the consent screen must show
5. A retention period for each data type
6. Security basics: encryption, access logs, deleting raw uploads
7. Breach response: who is told, the time limit, and how
8. Data localisation requirements and cloud region options

## Output

A checklist with a status for each item, the regulator's official links, and a list of questions to ask a local lawyer.

## Rules it follows

- Every requirement cites the regulator's own page.
- No fines or deadlines from memory; they are always checked.
- Anything unverified is marked.

## Install

**Claude Code:** `cp -r skills/data-protection-readiness ~/.claude/skills/` from the repo root, then restart Claude Code.

**Claude.ai / Desktop:** zip the `data-protection-readiness` folder and upload it under **Settings → Capabilities → Skills**.

Full instructions are in [`SKILL.md`](./SKILL.md).

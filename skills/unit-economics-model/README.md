# Unit Economics Model

> Turn price, volume, fee, loss and cost assumptions into per-unit and annual economics with sensitivity cases, so you can test an idea before building it.

Shows where a product makes or loses money and which assumption matters most. Every number is labelled "assumed", "sourced" or "from interviews" until it comes from real data.

## When to use it

- "Does this business make money at a 5% take rate?"
- "What's my break-even volume?"
- "How much do I earn per customer after fees and refunds?"

## What you get

| View | Answers |
|---|---|
| **Per unit** | Contribution per unit (amount and %) after variable costs, fees and losses |
| **Scale** | Monthly and annual profit after fixed costs, and the break-even volume |
| **Capital** | Peak capital tied up (float, inventory) and how fast it recycles; often the real deciding factor |
| **Sensitivity** | Base / pessimistic / optimistic cases, and the single assumption that moves the result most |
| **Verdict** | Does it work, what it would take to work, and which assumption to test first |

## Rules it follows

- The currency is always explicit; for foreign currencies it shows the exchange rate and its date.
- Assumed figures are never presented as facts.
- It names the two or three assumptions that would change the decision.
- The model stays simple enough to rebuild in a spreadsheet.

## Works well with

[`customer-discovery-interviews`](../customer-discovery-interviews/) to turn "assumed" numbers into "from interviews" ones.

## Install

**Claude Code:** `cp -r skills/unit-economics-model ~/.claude/skills/` from the repo root, then restart Claude Code.

**Claude.ai / Desktop:** zip the `unit-economics-model` folder and upload it under **Settings → Capabilities → Skills**.

Full instructions are in [`SKILL.md`](./SKILL.md).

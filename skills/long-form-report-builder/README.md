# Long-Form Report Builder

> Build long, sourced documents in stages (outline, research, fill, verify) so they don't drift or lose their sources.

A long report written in one pass drifts and loses sources. This skill scaffolds the outline as pending sections, does all the research up front, fills one section at a time, then checks every figure against its source.

## When to use it

- "Write a 20-page market analysis of e-bike rentals in Lisbon."
- "I need a detailed report on X with sources."
- Any multi-section document too long to produce in one pass.

## How it works

```
Confirm scope (topic, reader, depth, format, must-have sections)
   → Scaffold: title + one pending block per section, each with an intent line
   → Research all sections in parallel, logging source + date
   → Fill sections one at a time, each ending with a "so what"
   → Verify every figure; unverified items go to "Open questions"
   → Deliver with main finding, open questions, next step
```

## Quality rules

- Facts, estimates and inference are labelled separately.
- Tables are used for comparisons; charts only when they show a trend a table can't.
- Sources seen only as search snippets are marked as such.
- Quotes are never longer than a short phrase.
- Money, law or health topics get a single "not advice" line at the top.

## Install

**Claude Code:** `cp -r skills/long-form-report-builder ~/.claude/skills/` from the repo root, then restart Claude Code.

**Claude.ai / Desktop:** zip the `long-form-report-builder` folder and upload it under **Settings → Capabilities → Skills**.

Full instructions are in [`SKILL.md`](./SKILL.md).

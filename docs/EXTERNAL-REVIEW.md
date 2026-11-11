# How external repos are reviewed

External plugins are **referenced, pinned and flagged, never copied**. This page says exactly what was checked and, just as important, what was not.

## What was checked (2026-11-11)

For every external entry, at the commit SHA recorded in [`registry/registry.yaml`](../registry/registry.yaml):

1. **Licence.** Read from the GitHub API. Only repos with a recognised open licence (MIT, Apache-2.0) are installable. Repos with no licence, or `NOASSERTION`, are **link-only**.
2. **Pinning.** Every installable entry carries a full 40-character commit SHA, so a later push to the upstream repo cannot change what you install.
3. **Plugin manifest.** Each installable folder contains its own `.claude-plugin/plugin.json`.
4. **Contents scan (by file path).** Counts of skills, agents, commands, and whether the folder contains any of:
   - `hooks`: files under a `hooks/` folder or a `hooks.json`. Hooks run code automatically on events such as every tool call.
   - `mcp-server`: a `.mcp.json`. This starts a local or remote tool server.
   - `helper-scripts`: `.py`, `.js`, `.sh` and similar files. Usually tools a skill calls on request; they do not run by themselves.

Entries with `hooks` or `mcp-server` are shown as **REVIEW** in the Journey and Departments pages.

## What was NOT checked

- **The scan is path-based, not a code audit.** It tells you where to look; it does not read or vouch for the code. A folder with no flags can still contain a skill that tells Claude to do something unwise, and a flagged folder may be harmless.
- Upstream repos can have any contents later. The pin protects you until *we* bump it; each bump must be re-reviewed.
- Star counts and licences are a snapshot and are re-verified when an entry is added or updated.

## Before you enable a flagged plugin

1. Open the repo at the pinned SHA (the links in the tables point to the repo; append `/tree/<sha>` to see exactly that version).
2. Read the `hooks/` files and `.mcp.json`: what command runs, on which event, and does it make network calls?
3. If you are not comfortable, skip it. Most stages have unflagged alternatives; the flagged ones are marked in the tables.

## Updating a pin

1. `gh api repos/<owner>/<repo>/commits/<branch> --jq .sha`
2. Diff the old and new SHA on GitHub, focusing on hooks, `.mcp.json` and scripts.
3. Update `sha` and `last_verified` in the registry, run `python scripts/build_views.py` and `python scripts/validate.py`, and open a PR.

## Third-party licences

Each upstream project keeps its own licence and authorship. This repo links to them and records their licence; it does not redistribute their code.

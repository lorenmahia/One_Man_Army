# Contributing

## Add a skill

1. Create `skills/<name>/SKILL.md` with frontmatter containing `name` (equal to the folder name) and `description`.
2. Add `skills/<name>/README.md` for humans: summary, when to use it, what you get, boundaries, install.
3. Add an entry to [`registry/registry.yaml`](../registry/registry.yaml) with one `stage`, one or more `domains`, a one-line `summary` and today's `last_verified`. Field rules are in [`registry/SCHEMA.md`](../registry/SCHEMA.md).
4. Regenerate the views and validate:

```bash
pip install pyyaml
python scripts/build_views.py
python scripts/validate.py
```

5. Commit the skill, the registry change and the regenerated `journey/` and `departments/` together, then open a PR. CI runs the same validator.

## Add an external repo

External repos are **referenced and pinned**, never copied.

1. Read its README, licence and file tree. Read any hook (`hooks/`, `hooks.json`) or MCP server (`.mcp.json`) you will recommend, since they run with the user's permissions. Method and limits: [EXTERNAL-REVIEW.md](./EXTERNAL-REVIEW.md).
2. Get the current full commit SHA: `gh api repos/<owner>/<repo>/commits/<default-branch> --jq .sha`.
3. Add a `kind: external` entry with `source`, `mode`, `license`, `stars`, `stage`, `domains`, `summary`, `why`. For `mode: marketplace` also add `plugin`, `sha` and, if the plugin sits in a subfolder, `subdir`. Record `includes` and `runs_code` from your review. Use `mode: link-only` if the licence is missing or unclear, or if the repo is not a Claude plugin.
4. Regenerate (this rewrites `.claude-plugin/marketplace.json`) and validate as above, then run `claude plugin validate .`.

## Rules

- Never hand-edit `journey/` or `departments/`.
- Never put stage or domain tags inside a `SKILL.md`.
- Research and planning support only: no content that presents itself as legal, tax, investment or financial advice.

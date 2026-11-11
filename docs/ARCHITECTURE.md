# Architecture

One_Man_Army gives a solo founder a structured, from-scratch path to a company that runs like a much bigger one. The structure is the product, so it is deliberately simple and machine-checked.

## One source of truth, two lenses

```
registry/registry.yaml ──► scripts/build_views.py ──► journey/      (by lifecycle stage)
        ▲                                        └──► departments/  (by function)
        │
 every skill, agent, template, playbook and pinned external repo is one entry
```

- **Journey** answers "what do I do next?" Eight stages (00 Idea → 07 Scale), each with a purpose and an **exit gate**. Don't move on until you pass the gate.
- **Departments** answers "where is everything about finance / SEO / investors?" Ten functions.
- Both are generated from the same tagged entries, so they can never disagree. Founders pick the lens they prefer.

## Folder map

| Path | What lives there |
|---|---|
| `registry/` | `registry.yaml` (source of truth) and `SCHEMA.md` |
| `skills/<name>/` | `SKILL.md` (instructions for Claude) + `README.md` (for humans) |
| `journey/`, `departments/` | **Generated.** Never edit by hand. |
| `scripts/` | `build_views.py` generates views; `validate.py` checks everything |
| `.github/workflows/` | CI runs `validate.py` on every PR and push to `main` |
| `docs/` | This file and `CONTRIBUTING.md` |

Planned (see the roadmap in the root README): `agents/`, `templates/`, `playbooks/`, and `.claude-plugin/marketplace.json` for installable stage packs and pinned external repos.

## Design rules

1. **Registry first.** If it is not in the registry, it does not exist as far as the views and CI are concerned.
2. **Tags live in the registry, not in skills.** `SKILL.md` files stay standard and untouched, so skills from other authors drop in without edits.
3. **Reference, don't copy.** External repos are pinned to a full commit SHA and listed with their licence. Repos without a clear licence are link-only.
4. **Every claim is checkable.** `validate.py` fails the build on a missing file, a bad tag, a broken link or a stale generated view.
5. **Review before you trust.** Third-party skills run with your permissions. Read them before listing them, and never auto-update.

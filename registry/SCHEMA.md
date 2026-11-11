# Registry schema

`registry/registry.yaml` is the single source of truth. Everything in `journey/` and `departments/` is generated from it. Never edit those folders by hand.

## Top level

| Key | Meaning |
|---|---|
| `version` | Schema version (currently `1`). |
| `stages` | Ordered company lifecycle stages. Each has `id`, `name`, `purpose`, `exit_gate`. |
| `domains` | Functional departments. Each has `id`, `name`. |
| `entries` | Every skill, agent, template, playbook and external repo. |

## Entry fields

| Field | Required | Notes |
|---|---|---|
| `id` | yes | Unique, kebab-case. For skills it must equal the folder name. |
| `kind` | yes | `skill`, `agent`, `template`, `playbook` or `external`. |
| `stage` | yes | Exactly one stage id: where a founder should first reach for it. |
| `domains` | yes | One or more domain ids. |
| `summary` | yes | One sentence. |
| `last_verified` | yes | `YYYY-MM-DD`: when the entry was last checked. |
| `path` | skill, agent, template, playbook | Repo-relative path that must exist. Skills need `SKILL.md` and `README.md`. |
| `source` | external | `owner/repo` on GitHub. |
| `mode` | external | `marketplace` (installable, must be pinned) or `link-only` (reference only). |
| `sha` | external with `marketplace` | Full 40-character commit SHA. Never a branch name. |
| `license` | external | SPDX id as reported by GitHub, or `none-reported`. Unlicensed repos must be `link-only`. |
| `stars` | external | Informational, as of `last_verified`. |
| `why` | external | Why it is included. |

## Rules

- Stage and domain tags live here, never inside a `SKILL.md`, so third-party and existing skills stay unmodified.
- External repos are referenced and pinned, never copied.
- After any change run `python scripts/build_views.py`, then `python scripts/validate.py`.

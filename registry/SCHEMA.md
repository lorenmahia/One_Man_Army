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
| `plugin` | external with `marketplace` | Unique plugin name in our marketplace. Installed as `/plugin install <plugin>@one-man-army`. |
| `subdir` | optional | Folder inside the upstream repo that holds the plugin. Omit when the whole repo is the plugin. |
| `sha` | external with `marketplace` | Full 40-character commit SHA. Never a branch name. Link-only entries must not have one. |
| `license` | external | SPDX id as reported by GitHub, or `none-reported`. Unlicensed repos must be `link-only`. |
| `stars` | external | Integer, informational, as of `last_verified`. |
| `why` | external | Why it is included. |
| `includes` | optional list | Counts from the contents scan, e.g. `[5 skills, 2 agents]`. |
| `runs_code` | optional list | From the contents scan: `hooks`, `mcp-server`, `helper-scripts`. `hooks` or `mcp-server` shows as **REVIEW** in the views. See [EXTERNAL-REVIEW](../docs/EXTERNAL-REVIEW.md). |

## Generated outputs

`scripts/build_views.py` writes `journey/`, `departments/` and `.claude-plugin/marketplace.json` from this file. The marketplace lists the in-repo `one-man-army` plugin plus every `mode: marketplace` entry, using `{source: url, sha}` for whole repos and `{source: git-subdir, path, sha}` for plugins inside a larger repo.

## Rules

- Stage and domain tags live here, never inside a `SKILL.md`, so third-party and existing skills stay unmodified.
- External repos are referenced and pinned, never copied.
- After any change run `python scripts/build_views.py`, then `python scripts/validate.py`.

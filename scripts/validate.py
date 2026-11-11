#!/usr/bin/env python3
"""Validate the One_Man_Army repo. Exit 1 on any error.

Checks:
  * registry parses; stage/domain ids valid; entry ids unique; required fields present
  * every skill entry has skills/<id>/SKILL.md + README.md, frontmatter name == folder name, description present
  * every skills/* folder is registered
  * external entries: source, mode, license; marketplace mode needs a 40-char SHA and a real licence
  * relative markdown links in README/skills/journey/departments/docs resolve
  * generated views are up to date
"""
import re
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
errors = []


def err(msg):
    errors.append(msg)


def frontmatter(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"---\r?\n(.*?)\r?\n---", text, re.S)
    if not m:
        return None
    fm = {}
    for key in ("name", "description"):
        km = re.search(rf"^{key}:\s*(.+)$", m.group(1), re.M)
        if km:
            fm[key] = km.group(1).strip()
    return fm


def check_registry():
    reg = yaml.safe_load((ROOT / "registry" / "registry.yaml").read_text(encoding="utf-8"))
    stage_ids = [s["id"] for s in reg["stages"]]
    domain_ids = [d["id"] for d in reg["domains"]]
    if len(set(stage_ids)) != len(stage_ids):
        err("duplicate stage ids")
    if len(set(domain_ids)) != len(domain_ids):
        err("duplicate domain ids")
    seen = set()
    required = ("id", "kind", "stage", "domains", "summary", "last_verified")
    kinds = {"skill", "agent", "template", "playbook", "external"}
    for e in reg["entries"]:
        eid = e.get("id", "<missing id>")
        for f in required:
            if f not in e or e[f] in (None, "", []):
                err(f"[{eid}] missing field '{f}'")
        if eid in seen:
            err(f"[{eid}] duplicate id")
        seen.add(eid)
        if e.get("kind") not in kinds:
            err(f"[{eid}] bad kind {e.get('kind')!r}")
        if e.get("stage") not in stage_ids:
            err(f"[{eid}] unknown stage {e.get('stage')!r}")
        for d in e.get("domains") or []:
            if d not in domain_ids:
                err(f"[{eid}] unknown domain {d!r}")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(e.get("last_verified", ""))):
            err(f"[{eid}] last_verified must be YYYY-MM-DD")
        if e.get("kind") == "external":
            for f in ("source", "mode", "license", "why"):
                if not e.get(f):
                    err(f"[{eid}] external entry missing '{f}'")
            if e.get("mode") not in ("marketplace", "link-only"):
                err(f"[{eid}] mode must be marketplace or link-only")
            if e.get("mode") == "marketplace":
                if not re.fullmatch(r"[0-9a-f]{40}", str(e.get("sha", ""))):
                    err(f"[{eid}] marketplace entries need a full 40-char sha")
                if e.get("license") in (None, "none-reported", "NOASSERTION"):
                    err(f"[{eid}] unlicensed repos must be link-only")
        else:
            p = e.get("path")
            if not p or not (ROOT / p).exists():
                err(f"[{eid}] path {p!r} does not exist")
            elif e.get("kind") == "skill":
                folder = ROOT / p
                if folder.name != eid:
                    err(f"[{eid}] skill id must equal folder name '{folder.name}'")
                for fn in ("SKILL.md", "README.md"):
                    if not (folder / fn).exists():
                        err(f"[{eid}] missing {fn}")
                if (folder / "SKILL.md").exists():
                    fm = frontmatter(folder / "SKILL.md")
                    if fm is None:
                        err(f"[{eid}] SKILL.md has no frontmatter")
                    else:
                        if fm.get("name") != eid:
                            err(f"[{eid}] frontmatter name {fm.get('name')!r} != folder")
                        if not fm.get("description"):
                            err(f"[{eid}] frontmatter description missing")
    registered = {Path(e["path"]).name for e in reg["entries"] if e.get("kind") == "skill" and e.get("path")}
    for d in sorted((ROOT / "skills").iterdir()):
        if d.is_dir() and d.name not in registered:
            err(f"skills/{d.name} is not in the registry")


LINK = re.compile(r"\]\(([^)\s]+)\)")


def check_links():
    files = [ROOT / "README.md"]
    for sub in ("skills", "journey", "departments", "docs", "registry", "playbooks", "templates"):
        base = ROOT / sub
        if base.exists():
            files += list(base.rglob("*.md"))
    for f in files:
        if f.name == "SKILL.md":
            continue  # instructions for Claude; may contain placeholder text like [Title](URL)
        for target in LINK.findall(f.read_text(encoding="utf-8")):
            if re.match(r"^(https?:|mailto:|#)", target):
                continue
            rel = target.split("#")[0]
            if rel and not (f.parent / rel).exists():
                err(f"{f.relative_to(ROOT)}: broken link {target}")


def check_views():
    r = subprocess.run([sys.executable, str(ROOT / "scripts" / "build_views.py"), "--check"],
                       capture_output=True, text=True)
    if r.returncode != 0:
        err("generated views are stale: " + r.stdout.strip().replace("\n", " "))


def main():
    check_registry()
    check_links()
    check_views()
    if errors:
        print(f"{len(errors)} problem(s):")
        for e in errors:
            print("  -", e)
        return 1
    print("OK: registry, skills, links and generated views all valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Read-only checks for this repository's package conventions (Python 3.10+)."""

import argparse
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit


def check(root: Path) -> dict:
    errors = []
    skill = root / "skills" / "project-coordination"
    required = [
        root / "README.md", root / "README.zh-CN.md", root / "LICENSE",
        root / "VALIDATION.md", root / "CHANGELOG.md", root / "CONTRIBUTING.md",
        root / "examples" / "first-project.md", root / "evaluations" / "SCENARIOS.md",
        skill / "SKILL.md", skill / "LICENSE", skill / "agents" / "openai.yaml",
    ]
    for path in required:
        if not path.is_file():
            errors.append(f"Missing file: {path.relative_to(root)}")

    # Only maintained documentation and package metadata, not user caches or Git internals.
    paths = set(root.glob("*.md"))
    for folder in (skill, root / "examples", root / "evaluations"):
        paths.update(folder.rglob("*.md"))
        paths.update(folder.rglob("*.yaml"))
    contents = {}
    for path in sorted(paths):
        relative = path.relative_to(root).as_posix()
        if path.is_symlink() or not path.resolve().is_relative_to(root):
            errors.append(f"Unexpected external or linked content: {relative}")
            continue
        try:
            body = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"Cannot read {relative}: {type(exc).__name__}")
            continue
        contents[relative] = body
        fence = None
        prose = []
        for line in body.splitlines():
            marker = re.match(r"^\s*(`{3,}|~{3,})(.*)$", line)
            if marker:
                ticks, suffix = marker.groups()
                if fence is None:
                    fence = ticks
                elif ticks[0] == fence[0] and len(ticks) >= len(fence) and not suffix.strip():
                    fence = None
                continue
            if fence is None:
                prose.append(line)
        if fence is not None:
            errors.append(f"Unclosed code fence: {relative}")
        for target in re.findall(r"\]\(([^\s)]+)\)", "\n".join(prose)):
            parsed = urlsplit(target)
            if parsed.scheme or not parsed.path:
                continue
            linked = (path.parent / unquote(parsed.path)).resolve()
            if not linked.is_relative_to(root) or not linked.is_file():
                errors.append(f"Broken or external local file link: {relative} -> {target}")
        # Deliberately bounded; not a secret detector or a security audit.
        markers = [r"\b[A-Za-z]:[/\\]", r"/Users/[^/\s]+/", r"/home/[^/\s]+/",
                   r"gh[pousr]_[A-Za-z0-9]{20,}", r"sk-[A-Za-z0-9_-]{20,}",
                   r"-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----"]
        if any(re.search(pattern, body) for pattern in markers):
            errors.append(f"Possible private marker (inspect manually): {relative}")

    core = contents.get("skills/project-coordination/SKILL.md", "")
    front = re.match(r"\A---\n(.*?)\n---(?:\n|$)", core, re.S)
    version = None
    if not front:
        errors.append("Missing skill frontmatter")
    else:
        # A narrow convention check, not a general YAML parser.
        header = front.group(1)
        for key, expected in (("name", "project-coordination"), ("license", "MIT")):
            if not re.search(rf"^{key}: {re.escape(expected)}$", header, re.M):
                errors.append(f"Unexpected {key} metadata")
        description = re.search(r"^description: (.+)$", header, re.M)
        if not description or not 1 <= len(description.group(1)) <= 1024:
            errors.append("Description must be one nonempty line of at most 1024 characters")
        metadata = re.search(r"^metadata:\n((?:[ \t]+[^\n]*(?:\n|$))+)", header, re.M)
        found = re.search(r'^  version: "(\d+\.\d+\.\d+)"$', metadata.group(1), re.M) if metadata else None
        if found:
            version = found.group(1)
        else:
            errors.append("Missing quoted semantic version under metadata")
        if not metadata:
            errors.append("Missing metadata mapping")
    if version:
        declarations = {
            "README.md": r"^Version (\d+\.\d+\.\d+) ·",
            "README.zh-CN.md": r"^当前版本：(\d+\.\d+\.\d+)。",
            "CHANGELOG.md": r"^## (\d+\.\d+\.\d+) —",
            "VALIDATION.md": r"^Version (\d+\.\d+\.\d+) ·",
        }
        for name, pattern in declarations.items():
            current = re.search(pattern, contents.get(name, ""), re.M)
            if not current or current.group(1) != version:
                errors.append(f"Current version declaration mismatch: {name}")
    ui = contents.get("skills/project-coordination/agents/openai.yaml", "")
    if not re.search(r'^  default_prompt: .*\$project-coordination', ui, re.M):
        errors.append("UI invocation does not name the skill")
    if (root / "LICENSE").is_file() and (skill / "LICENSE").is_file():
        license_text = (root / "LICENSE").read_text(encoding="utf-8")
        if license_text != (skill / "LICENSE").read_text(encoding="utf-8"):
            errors.append("License copies differ")
        if "MIT License" not in license_text or "Permission is hereby granted" not in license_text:
            errors.append("MIT license notice missing")
    return {"status": "FAIL" if errors else "PASS", "version": version,
            "documents_checked": len(contents), "entry_words": len(core.split()), "errors": errors}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    result = check(args.root.resolve())
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(result["status"] != "PASS")

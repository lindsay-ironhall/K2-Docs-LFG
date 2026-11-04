#!/usr/bin/env python3
"""Convert a GitBook Git Sync export into an MkDocs docs folder.

Usage: python scripts/gitbook_to_mkdocs.py [repo_root] [out_dir]
Defaults: repo_root=".", out_dir="_docs"
"""
import re
import shutil
import sys
from pathlib import Path

SKIP = {".git", ".github", "scripts", "site", "_docs", "overrides"}
SKIP_FILES = {"mkdocs.yml", "requirements.txt", ".gitbook.yaml", "SETUP.md"}
ASSET_DIR = "gitbook-assets"

repo = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
out = Path(sys.argv[2] if len(sys.argv) > 2 else "_docs").resolve()

# Respect GitBook's root setting, if any
root = repo
cfg = repo / ".gitbook.yaml"
if cfg.exists():
    m = re.search(r"^root:\s*['\"]?([^'\"\n]+)", cfg.read_text(), re.M)
    if m:
        root = (repo / m.group(1).strip()).resolve()

if out.exists():
    shutil.rmtree(out)
out.mkdir(parents=True)

# Copy content. Hidden ".gitbook/assets" is renamed, MkDocs ignores dot folders.
for p in root.rglob("*"):
    rel = p.relative_to(root)
    if rel.parts[0] in SKIP or p.is_dir():
        continue
    if len(rel.parts) == 1 and rel.name in SKIP_FILES:
        continue
    parts = list(rel.parts)
    if parts[0] == ".gitbook":
        if len(parts) > 1 and parts[1] == "assets":
            parts = [ASSET_DIR] + parts[2:]
        else:
            continue
    elif any(x.startswith(".") for x in parts):
        continue
    dest = out.joinpath(*parts)
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(p, dest)

HINT = {"info": "info", "warning": "warning", "danger": "danger", "success": "success"}


def indent(text, n=4):
    pad = " " * n
    return "\n".join(pad + l if l.strip() else "" for l in text.strip("\n").split("\n"))


def embed(url, caption=""):
    yt = re.search(r"(?:youtube\.com/(?:watch\?v=|embed/|shorts/|live/)|youtu\.be/)([\w-]{6,})", url)
    if yt:
        html = (f'<div class="video"><iframe src="https://www.youtube-nocookie.com/embed/{yt.group(1)}" '
                'title="Video" frameborder="0" allow="accelerometer; clipboard-write; encrypted-media; '
                'picture-in-picture" allowfullscreen></iframe></div>')
    else:
        html = f"[{caption.strip() or url}]({url})"
        caption = ""
    return "\n\n" + html + (f"\n\n*{caption.strip()}*" if caption.strip() else "") + "\n\n"


def convert(md):
    md = md.replace(".gitbook/assets/", f"{ASSET_DIR}/")

    def tabs(m):
        out_parts = []
        for t in re.finditer(r'{%\s*tab\s+title="([^"]*)"\s*%}(.*?){%\s*endtab\s*%}', m.group(1), re.S):
            out_parts.append(f'=== "{t.group(1)}"\n\n{indent(t.group(2))}\n')
        return "\n\n" + "\n".join(out_parts) + "\n\n"

    # Inner blocks first so nesting works reasonably
    for _ in range(3):
        md = re.sub(r"{%\s*tabs\s*%}(.*?){%\s*endtabs\s*%}", tabs, md, flags=re.S)
        md = re.sub(
            r'{%\s*hint\s+style="(\w+)"\s*%}(.*?){%\s*endhint\s*%}',
            lambda m: f'\n\n!!! {HINT.get(m.group(1), "note")} ""\n\n{indent(m.group(2))}\n\n',
            md, flags=re.S)
    md = re.sub(r'{%\s*embed\s+url="([^"]+)"[^%]*%}((?:(?!{%\s*embed).)*?){%\s*endembed\s*%}',
                lambda m: embed(m.group(1), m.group(2)), md, flags=re.S)
    md = re.sub(r'{%\s*embed\s+url="([^"]+)"[^%]*%}', lambda m: embed(m.group(1)), md)
    md = re.sub(r'{%\s*content-ref\s+url="[^"]*"\s*%}(.*?){%\s*endcontent-ref\s*%}',
                lambda m: m.group(1).strip(), md, flags=re.S)
    md = re.sub(r'{%\s*file\s+src="([^"]+)"\s*%}(.*?){%\s*endfile\s*%}',
                lambda m: f"[:material-file-download: {m.group(2).strip() or Path(m.group(1)).name}](<{m.group(1)}>)",
                md, flags=re.S)
    md = re.sub(r'{%\s*file\s+src="([^"]+)"\s*%}',
                lambda m: f"[:material-file-download: {Path(m.group(1)).name}](<{m.group(1)}>)", md)
    # Wrappers that have no MkDocs equivalent: keep the content
    md = re.sub(r"{%\s*(?:code|stepper|step|columns|column|swagger|openapi)[^%]*%}\n?", "", md)
    md = re.sub(r"{%\s*end(?:code|stepper|step|columns|column|swagger|openapi)\s*%}\n?", "", md)
    # Escaped GitBook characters like \$ are fine in MkDocs; drop leftover unknown tags loudly
    for tag in set(re.findall(r"{%\s*(\w[\w-]*)", md)):
        print(f"  ! unhandled GitBook block: {tag}", file=sys.stderr)
    return md


for f in out.rglob("*.md"):
    f.write_text(convert(f.read_text(encoding="utf-8")), encoding="utf-8")

# README.md -> index.md so each folder has a landing page
for f in out.rglob("README.md"):
    idx = f.with_name("index.md")
    if not idx.exists():
        f.rename(idx)
for f in out.rglob("*.md"):
    t = f.read_text(encoding="utf-8")
    t2 = re.sub(r"(\(<?[^()\s<>]*?)README\.md", r"\1index.md", t)
    if t2 != t:
        f.write_text(t2, encoding="utf-8")

# SUMMARY.md: GitBook uses "## Group" headings and 2-space indents; literate-nav wants 4
summary = out / "SUMMARY.md"


def is_hidden(link):
    f = (out / link.split("#")[0]).resolve()
    if not f.exists():
        return False
    head = f.read_text(encoding="utf-8")[:500]
    return bool(re.match(r"^---\n(?:.*\n)*?hidden:\s*true", head))


if summary.exists():
    lines, group, hide_below = [], False, None
    for line in summary.read_text(encoding="utf-8").splitlines():
        if re.match(r"^#\s", line) or not line.strip():
            continue
        h = re.match(r"^##+\s+(.*)", line)
        if h:
            lines.append(f"* {h.group(1).strip()}")
            group = True
            continue
        m = re.match(r"^(\s*)([*\-+])\s+(.*)", line)
        if m:
            depth = len(m.group(1).replace("\t", "  ")) // 2 + (1 if group else 0)
            if hide_below is not None and depth > hide_below:
                continue
            hide_below = None
            lk = re.search(r"\]\(<?([^)>]+)>?\)", m.group(3))
            if lk and is_hidden(lk.group(1)):
                hide_below = depth
                continue
            lines.append("    " * depth + "* " + m.group(3))
    summary.write_text("\n".join(lines) + "\n", encoding="utf-8")

print(f"Converted {sum(1 for _ in out.rglob('*.md'))} pages into {out}")

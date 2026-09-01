#!/usr/bin/env python3
"""Find documentation pages that need style improvements.

Scans Markdown pages and reports, per file:

  - long-paragraph   prose paragraphs longer than a character threshold
  - heading-case     ATX headings that don't look like sentence case (heuristic)
  - long-code-line   lines longer than a threshold inside shell code fences
  - vale             Vale findings (errors / warnings / suggestions), opt-in

The structural checks (paragraph, heading, code line) are pure Python and
fast enough to run across the whole content tree. The Vale check shells out
to the same Docker image used by the `improve-style` skill and is therefore
opt-in via `--vale`.

Usage:
  python3 find_style_issues.py [PATH ...]            # structural scan
  python3 find_style_issues.py --vale [PATH ...]     # also run Vale
  python3 find_style_issues.py --top 20              # only worst 20 files

PATH defaults to src/content. A PATH may be a file or a directory.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass, field

VALE_IMAGE = (
    "gsoci.azurecr.io/giantswarm/vale:v3.15.1@sha256:"
    "1e4449aba172e268fcb40fad8fa47a3c713c568154afe0fcb5bc2a0a42420efe"
)

# Proper nouns, brand names and acronyms that may legitimately be capitalized
# in the middle of a sentence-case heading. Lower-cased for comparison.
ALLOWLIST = {
    "giant", "swarm", "kubernetes", "k8s", "aws", "azure", "gcp", "vmware",
    "vsphere", "proxmox", "ve", "cilium", "grafana", "prometheus", "loki",
    "mimir", "tempo", "alloy", "flux", "fluxcd", "helm", "cluster", "api",
    "capi", "capa", "capz", "capv", "capmox", "argo", "argocd", "backstage",
    "oidc", "iam", "irsa", "dns", "tls", "ssl", "cni", "csi", "crd", "rbac",
    "sso", "mcp", "ide", "vlan", "sdn", "acl", "cidr", "ip", "vm", "vms",
    "coredns", "kube", "vip", "etcd", "kubeadm", "kubectl", "json", "yaml",
    "http", "https", "url", "urls", "api", "cpu", "gpu", "ram", "os", "ssh",
    "tcp", "udp", "bgp", "arp", "efs", "ebs", "s3", "iso", "ca", "ui", "cli",
    "az", "azs", "github", "gitlab", "linux", "windows", "macos", "docker",
    "ingress", "egress",  # k8s resource-ish, commonly capitalized in headings
    "prepare", "az",
    "i", "i'm", "i've",
    "giantswarm",
}

SHELL_LANGS = {"sh", "bash", "shell", "zsh", "console", "shell-session"}

# Strip helpers for measuring the *reading* length of a paragraph.
RE_SHORTCODE = re.compile(r"\{\{[<%].*?[%>]\}\}", re.DOTALL)
RE_LINK = re.compile(r"\[([^\]]*)\]\([^)]*\)")          # [text](url) -> text
RE_IMAGE = re.compile(r"!\[([^\]]*)\]\([^)]*\)")        # ![alt](url) -> alt
RE_HTML_TAG = re.compile(r"<[^>]+>")
RE_INLINE_CODE = re.compile(r"`[^`]*`")
RE_EMPHASIS = re.compile(r"(\*\*|__|\*|_)")
RE_HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
RE_ANCHOR = re.compile(r"\{#[^}]*\}\s*$")
RE_FENCE = re.compile(r"^(\s*)(`{3,}|~{3,})(.*)$")
RE_LIST = re.compile(r"^\s*([-*+]|\d+[.)])\s+")
RE_WORD_LEAD = re.compile(r"^[^A-Za-z0-9`]*")


@dataclass
class FileReport:
    path: str
    long_paragraphs: list = field(default_factory=list)   # (line, length)
    heading_case: list = field(default_factory=list)       # (line, text, reason)
    long_code_lines: list = field(default_factory=list)    # (line, length, lang)
    vale_error: int = 0
    vale_warning: int = 0
    vale_suggestion: int = 0

    @property
    def vale_total(self) -> int:
        return self.vale_error + self.vale_warning + self.vale_suggestion

    @property
    def total(self) -> int:
        return (
            len(self.long_paragraphs)
            + len(self.heading_case)
            + len(self.long_code_lines)
            + self.vale_total
        )


def reading_length(text: str) -> int:
    """Approximate visible length of a paragraph, ignoring markup/URLs."""
    text = RE_SHORTCODE.sub("", text)
    text = RE_IMAGE.sub(r"\1", text)
    text = RE_LINK.sub(r"\1", text)
    text = RE_INLINE_CODE.sub(lambda m: m.group(0).strip("`"), text)
    text = RE_HTML_TAG.sub("", text)
    text = RE_EMPHASIS.sub("", text)
    return len(text.strip())


def is_code_token(tok: str) -> bool:
    """A heading token that's an identifier/path/code rather than a word."""
    if "`" in tok:
        return True
    core = tok.strip(".,:;!?()[]\"'")
    if not core:
        return False
    # identifiers / paths / domains / flags
    if re.search(r"[./@_]", core) or core.startswith("-"):
        return True
    # camelCase field names (e.g. apiVersion, serviceAccountIssuers)
    if not core.isupper() and any(c.isupper() for c in core[1:]):
        return True
    return False


def check_heading_case(text: str):
    """Return a reason string if the heading isn't sentence case, else None.

    Heuristic: the first real word should be capitalized; later words should
    be lower case unless they're acronyms, brand names (allowlist), code
    identifiers, or contain internal capitals/digits. Vale's Microsoft.Headings
    rule is the authoritative check; this is a fast pre-filter.
    """
    text = RE_ANCHOR.sub("", text).strip()
    # Resolve links/images to their visible text, drop emphasis markers.
    text = RE_IMAGE.sub(r"\1", text)
    text = RE_LINK.sub(r"\1", text)
    text = RE_EMPHASIS.sub("", text)
    if not text:
        return None

    tokens = text.split()
    # Skip headings that are purely an identifier (e.g. label/CRD reference names)
    word_tokens = [t for t in tokens if not is_code_token(t)]
    if not word_tokens:
        return None

    after_colon = False
    first_real_seen = False
    for i, tok in enumerate(tokens):
        if is_code_token(tok):
            after_colon = tok.endswith(":")
            continue
        core = tok.strip(".,:;!?()[]\"'")
        if not core:
            after_colon = tok.endswith(":")
            continue

        first_alpha = next((c for c in core if c.isalpha()), "")
        if not first_alpha:
            after_colon = tok.endswith(":")
            continue

        if not first_real_seen:
            first_real_seen = True
            # Only require capitalization when the heading literally starts
            # with this word (a leading code token, e.g. `Chart.yaml`, means
            # the following word need not be capitalized).
            if i == 0 and first_alpha.islower() and core.lower() not in ALLOWLIST:
                return f"first word '{core}' is not capitalized"
            after_colon = tok.endswith(":")
            continue

        # Subsequent words
        if first_alpha.isupper():
            if after_colon:
                pass  # capital after a colon is acceptable
            elif core.lower() in ALLOWLIST:
                pass
            elif core.isupper() and len(core) <= 6:
                pass  # short acronym
            elif any(c.isupper() for c in core[1:]) or any(c.isdigit() for c in core):
                pass  # CamelCase / has digits (CoreDNS, v1.2)
            else:
                return f"word '{core}' is capitalized mid-heading"
        after_colon = tok.endswith(":")

    return None


def scan_file(path: str, max_paragraph: int, max_code_line: int) -> FileReport:
    rep = FileReport(path=path)
    try:
        with open(path, encoding="utf-8") as fh:
            lines = fh.readlines()
    except (OSError, UnicodeDecodeError):
        return rep

    in_frontmatter = False
    frontmatter_done = False
    in_fence = False
    fence_marker = ""
    fence_indent = 0
    fence_lang = ""

    para_lines: list[str] = []
    para_start = 0

    def flush_paragraph():
        nonlocal para_lines, para_start
        if para_lines:
            text = " ".join(l.strip() for l in para_lines)
            length = reading_length(text)
            if length > max_paragraph:
                rep.long_paragraphs.append((para_start, length))
        para_lines = []

    for idx, raw in enumerate(lines, start=1):
        line = raw.rstrip("\n")
        stripped = line.strip()

        # Frontmatter (leading --- ... ---)
        if idx == 1 and stripped == "---":
            in_frontmatter = True
            continue
        if in_frontmatter:
            if stripped == "---":
                in_frontmatter = False
                frontmatter_done = True
            continue

        # Code fences
        fence_match = RE_FENCE.match(line)
        if fence_match and not in_fence:
            flush_paragraph()
            in_fence = True
            fence_indent = len(fence_match.group(1))
            fence_marker = fence_match.group(2)[0] * 3
            fence_lang = fence_match.group(3).strip().split()[0].lower() if fence_match.group(3).strip() else ""
            continue
        if in_fence:
            if fence_match and fence_match.group(2)[0] * 3 == fence_marker and not fence_match.group(3).strip():
                in_fence = False
                fence_lang = ""
                continue
            if fence_lang in SHELL_LANGS:
                # Measure logical length without the list-indentation of the fence.
                content = line[fence_indent:] if len(line) >= fence_indent else line
                if len(content) > max_code_line:
                    rep.long_code_lines.append((idx, len(content), fence_lang))
            continue

        # Headings
        head = RE_HEADING.match(line)
        if head:
            flush_paragraph()
            reason = check_heading_case(head.group(2))
            if reason:
                rep.heading_case.append((idx, head.group(2), reason))
            continue

        # Paragraph accumulation: skip non-prose block starters.
        if stripped == "":
            flush_paragraph()
            continue
        if (
            stripped.startswith("|")
            or stripped.startswith(">")
            or stripped.startswith("<")
            or stripped.startswith("{{")
            or RE_LIST.match(line)
        ):
            flush_paragraph()
            continue

        if not para_lines:
            para_start = idx
        para_lines.append(line)

    flush_paragraph()
    return rep


# Auto-generated or non-prose sections that aren't worth manual style review.
# (The /changes changelogs and the generated platform-api references are
# produced by tooling and largely exempt from Vale anyway.)
DEFAULT_EXCLUDES = [
    "src/content/changes",
    "src/content/reference/platform-api/cluster-apps",
    "src/content/reference/platform-api/crd",
]


def collect_markdown(paths: list[str], excludes: list[str]) -> list[str]:
    def excluded(path: str) -> bool:
        norm = os.path.normpath(path)
        return any(ex in norm for ex in excludes)

    files: list[str] = []
    for p in paths:
        if os.path.isfile(p) and p.endswith(".md"):
            if not excluded(p):
                files.append(p)
        elif os.path.isdir(p):
            for root, _, names in os.walk(p):
                for n in names:
                    if n.endswith(".md"):
                        full = os.path.join(root, n)
                        if not excluded(full):
                            files.append(full)
    return sorted(set(files))


def run_vale(files: list[str], reports: dict[str, FileReport]):
    """Run Vale via Docker over the given files and fold counts into reports."""
    cwd = os.getcwd()
    cmd = [
        "docker", "run", "--rm",
        "-v", f"{cwd}:/workdir",
        "-w", "/workdir",
        VALE_IMAGE,
        "--config=/workdir/.vale.ini",
        "--output=JSON",
        *files,
    ]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True)
    except FileNotFoundError:
        print("WARNING: docker not found; skipping Vale checks.", file=sys.stderr)
        return
    if not proc.stdout.strip():
        if proc.returncode != 0:
            print(f"WARNING: Vale produced no output (exit {proc.returncode}).", file=sys.stderr)
            if proc.stderr.strip():
                print(proc.stderr.strip(), file=sys.stderr)
        return
    try:
        data = json.loads(proc.stdout)
    except json.JSONDecodeError:
        print("WARNING: could not parse Vale JSON output.", file=sys.stderr)
        return
    for fname, alerts in data.items():
        norm = os.path.normpath(fname)
        rep = reports.get(norm) or reports.get(fname)
        if rep is None:
            rep = FileReport(path=norm)
            reports[norm] = rep
        for a in alerts:
            sev = a.get("Severity", "")
            if sev == "error":
                rep.vale_error += 1
            elif sev == "warning":
                rep.vale_warning += 1
            elif sev == "suggestion":
                rep.vale_suggestion += 1


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("paths", nargs="*", default=["src/content"], help="Files or directories to scan (default: src/content)")
    parser.add_argument("--max-paragraph", type=int, default=600, help="Paragraph length threshold in characters (default: 600)")
    parser.add_argument("--max-code-line", type=int, default=65, help="Shell code line length threshold (default: 65)")
    parser.add_argument("--vale", action="store_true", help="Also run Vale (requires Docker; slower)")
    parser.add_argument("--top", type=int, default=0, help="Only show the N files with the most issues")
    parser.add_argument("--exclude", action="append", default=[], metavar="SUBSTR", help="Skip paths containing SUBSTR (repeatable)")
    parser.add_argument("--no-default-excludes", action="store_true", help=f"Don't apply default excludes ({', '.join(DEFAULT_EXCLUDES)})")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    args = parser.parse_args(argv)

    paths = args.paths or ["src/content"]
    excludes = list(args.exclude)
    if not args.no_default_excludes:
        excludes += DEFAULT_EXCLUDES
    files = collect_markdown(paths, excludes)
    if not files:
        print("No Markdown files found.", file=sys.stderr)
        return 1

    reports: dict[str, FileReport] = {}
    for f in files:
        reports[os.path.normpath(f)] = scan_file(f, args.max_paragraph, args.max_code_line)

    if args.vale:
        run_vale(files, reports)

    ranked = sorted(
        (r for r in reports.values() if r.total > 0),
        key=lambda r: (r.vale_error, r.total),
        reverse=True,
    )
    if args.top:
        ranked = ranked[: args.top]

    if args.json:
        out = []
        for r in ranked:
            out.append({
                "path": r.path,
                "long_paragraphs": r.long_paragraphs,
                "heading_case": r.heading_case,
                "long_code_lines": r.long_code_lines,
                "vale": {"error": r.vale_error, "warning": r.vale_warning, "suggestion": r.vale_suggestion},
                "total": r.total,
            })
        print(json.dumps(out, indent=2))
        return 0

    if not ranked:
        print("No style issues found. 🎉")
        return 0

    total_files = len(ranked)
    print(f"Found style issues in {total_files} file(s):\n")
    for r in ranked:
        print(r.path)
        if r.long_paragraphs:
            worst = max(n for _, n in r.long_paragraphs)
            lines_str = ", ".join(f"L{ln} ({n})" for ln, n in r.long_paragraphs)
            print(f"  long-paragraph : {len(r.long_paragraphs)} (longest {worst} chars) — {lines_str}")
        if r.heading_case:
            for ln, text, reason in r.heading_case:
                print(f"  heading-case   : L{ln} — {reason}: \"{text}\"")
        if r.long_code_lines:
            worst = max(n for _, n, _ in r.long_code_lines)
            lines_str = ", ".join(f"L{ln} ({n})" for ln, n, _ in r.long_code_lines)
            print(f"  long-code-line : {len(r.long_code_lines)} (longest {worst} chars) — {lines_str}")
        if r.vale_total:
            print(f"  vale           : {r.vale_total} ({r.vale_error} error, {r.vale_warning} warning, {r.vale_suggestion} suggestion)")
        print()

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

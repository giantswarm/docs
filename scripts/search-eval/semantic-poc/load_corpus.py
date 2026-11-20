#!/usr/bin/env python3
"""Load the docs content into a local OpenSearch 'docs' index for the PoC.

Walks src/content for Markdown pages, extracts title, description and body,
derives the published URL from the file path, and bulk-indexes them. This is
the keyword corpus the semantic PoC samples from (setup reindexes it into the
vector index). File-path URLs approximate the real site, which is good enough
to judge relevance in a PoC. Standard library only.

    python3 load_corpus.py --host localhost --port 9200
"""
import argparse
import json
import os
import re
import urllib.error
import urllib.request

FRONTMATTER = re.compile(r"^---\s*\n(.*?)\n---\s*\n(.*)$", re.S)


def req(method, url, body=None, ndjson=False):
    data = None
    ctype = "application/json"
    if ndjson:
        data = body.encode("utf-8")
        ctype = "application/x-ndjson"
    elif body is not None:
        data = json.dumps(body).encode("utf-8")
    r = urllib.request.Request(url, data=data, method=method, headers={"Content-Type": ctype})
    try:
        with urllib.request.urlopen(r, timeout=60) as resp:
            return resp.read()
    except urllib.error.HTTPError as e:
        if method == "DELETE":
            return b""  # index may not exist yet
        raise RuntimeError("%s %s -> %d: %s" % (method, url, e.code, e.read().decode("utf-8")[:300]))


def field(fm, name):
    m = re.search(r'^%s:\s*(.+)$' % name, fm, re.M)
    if not m:
        return ""
    return m.group(1).strip().strip('"').strip("'")


def url_for(relpath):
    d = os.path.dirname(relpath).replace(os.sep, "/")
    return "/" + d + "/" if d else "/"


def clean_body(body):
    body = re.sub(r"{{[<%].*?[%>]}}", " ", body, flags=re.S)   # Hugo shortcodes
    body = re.sub(r"```.*?```", " ", body, flags=re.S)          # code fences
    body = re.sub(r"<!--.*?-->", " ", body, flags=re.S)         # comments
    body = re.sub(r"[#>*_`\[\]()|]", " ", body)                 # markdown punctuation
    return re.sub(r"\s+", " ", body).strip()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    here = os.path.dirname(os.path.abspath(__file__))
    ap.add_argument("--content", default=os.path.join(here, "..", "..", "..", "src", "content"))
    ap.add_argument("--host", default="localhost")
    ap.add_argument("--port", type=int, default=9200)
    ap.add_argument("--index", default="docs")
    args = ap.parse_args()

    base = "http://%s:%d" % (args.host, args.port)
    req("DELETE", base + "/" + args.index)
    req("PUT", base + "/" + args.index, {"mappings": {"properties": {
        "title": {"type": "text"}, "description": {"type": "text"},
        "body": {"type": "text"}, "url": {"type": "keyword"}, "type": {"type": "keyword"}}}})

    root = os.path.abspath(args.content)
    lines = []
    count = 0

    def flush():
        if lines:
            req("POST", base + "/_bulk", "\n".join(lines) + "\n", ndjson=True)
            del lines[:]

    for dirpath, _, files in os.walk(root):
        for fn in files:
            if not fn.endswith(".md"):
                continue
            rel = os.path.relpath(os.path.join(dirpath, fn), root)
            # Skip release notes: thousands of pages that are noise for a
            # synonym relevance test and otherwise swamp the corpus.
            if rel.split(os.sep)[0] == "changes":
                continue
            with open(os.path.join(dirpath, fn), encoding="utf-8") as f:
                raw = f.read()
            m = FRONTMATTER.match(raw)
            if not m:
                continue
            title = field(m.group(1), "title")
            if not title:
                continue
            doc = {"title": title, "description": field(m.group(1), "description"),
                   "body": clean_body(m.group(2))[:5000], "url": url_for(rel), "type": "Documentation"}
            lines.append(json.dumps({"index": {"_index": args.index}}))
            lines.append(json.dumps(doc))
            count += 1
            if len(lines) >= 2000:
                flush()
    flush()
    req("POST", base + "/" + args.index + "/_refresh")
    print("indexed %d pages into '%s'" % (count, args.index))


if __name__ == "__main__":
    main()

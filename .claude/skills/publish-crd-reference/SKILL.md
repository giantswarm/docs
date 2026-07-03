---
name: publish-crd-reference
description: Understand and maintain how the CRD reference pages under /reference/platform-api/crd/ are generated — register a new CRD source repo, make sure every published CRD has an example CR, and fix pages that render without an example
user-invocable: true
argument-hint: "[CRD full name, repo short_name, or 'audit']"
---

# Publish CRD reference pages

The CRD reference under
[`/reference/platform-api/crd/`](https://docs.giantswarm.io/reference/platform-api/crd/)
is **fully generated** — never hand-edit those pages. This skill explains the
machinery and the two everyday tasks: registering a new CRD and making sure a
CRD's page shows an **example CR**.

## How it works

- Pages are produced by
  [`giantswarm/crd-docs-generator`](https://github.com/giantswarm/crd-docs-generator)
  (a container), driven by `scripts/update-crd-reference/config.yaml` and the
  `scripts/update-crd-reference/crd.template` layout.
- Regenerate locally with `make update-crd-reference` (runs
  `scripts/update-crd-reference/main.sh`). Output lands in
  `src/content/reference/platform-api/crd/` — these files are wiped and rewritten
  each run, so commit the generated result, don't edit it.
- `.github/workflows/check-update-crd-reference.yaml` validates the config on any
  change under `scripts/update-crd-reference/`. The config has a JSON schema
  (`$schema` line at the top of `config.yaml`) — your editor will flag mistakes.

### How a CRD gets a page

For each source repo the config lists:

- `commit_reference` — the tag the repo is cloned at (bump this to pick up new
  CRDs or newly added examples).
- `crd_paths` — directories walked **recursively** for CRD YAML files.
- `cr_paths` — directories searched for **example CRs** (one example per file).
- `metadata.<full-name>` — per-CRD `owner`, `topics`, `deprecation`, `hidden`.

A page is published for a CRD **only if it has a `metadata` entry** for its full
name (e.g. `silences.observability.giantswarm.io`) and that entry is not
`hidden: true`. A CRD found in `crd_paths` with no metadata is skipped with a
`WARN` — so adding a new CRD means adding a metadata block, not just the path.

### How an example CR is matched — the rule that trips people up

For **each version** of a CRD, the generator does an **exact file lookup** (an
`os.Stat`, *not* a recursive search) in each `cr_path`. It accepts either name:

1. Giant Swarm format — `{cr_path}/{group}_{version}_{singular}.yaml`
   e.g. `docs/cr/observability.giantswarm.io_v1alpha1_grafanaorganization.yaml`
2. kube-builder format — `{cr_path}/{first-segment-of-group}_{version}_{singular}.yaml`
   e.g. `config/samples/observability_v1alpha1_grafanaorganization.yaml`

where `group` / `version` / `singular` come from the CRD's own
`spec.group`, `spec.versions[].name`, and `spec.names.singular`.

Consequences to remember:

- The file must sit **directly inside** a `cr_path` — subdirectories are ignored.
- The repo must actually **declare `cr_paths`** in this config. If it's absent,
  no example is ever looked for (even if a sample exists in the repo).
- `version` and `singular` must match the CRD **exactly**. A v1alpha2-only CRD
  needs a `_v1alpha2_` file; a `_v1alpha1_` file won't match.
- One example file per CRD version.

## Task: make a published CRD show an example

1. Identify the CRD's `group`, `version(s)`, and `singular` from its CRD YAML in
   the source repo (under one of its `crd_paths`).
2. Check the repo already has, or add, an example CR file named per the rule
   above, **directly inside** a directory. Convention across most repos is
   `docs/cr/` with the Giant Swarm format; kube-builder repos use
   `config/samples/`. Put a realistic, minimal, valid resource in it — the repo
   README often already contains a usable example.
3. In `config.yaml`, make sure this repo's entry has a `cr_paths` list that
   includes that directory, and bump `commit_reference` to a tag that contains
   the example file.
4. Run `make update-crd-reference`, then confirm the page now renders an
   "Example CR" section. Commit the regenerated pages.

If the example lives in the source repo but the page is still blank, the usual
cause is a `cr_paths` mismatch — the configured directory doesn't exist in the
repo, or the file is in a subfolder. Point `cr_paths` at the directory that
actually holds the file.

## Task: register a new CRD / source repo

Add (or extend) a `source_repositories` entry:

```yaml
  - url: https://github.com/giantswarm/<repo>
    organization: giantswarm
    short_name: <repo>
    commit_reference: <tag>
    crd_paths:
      - config/crd/bases        # wherever the CRD YAMLs live
    cr_paths:
      - docs/cr                 # wherever example CRs live (see rule above)
    metadata:
      <plural>.<group>:
        owner:
          - https://github.com/orgs/giantswarm/teams/<team>
        topics:
          - <topic>
```

Order matters: if two repos provide the same CRD full name, the **first** entry
wins and later ones are warned and skipped. To keep a CRD out of the published
docs, either omit its metadata or set `hidden: true`.

## Verifying

- Locally: `make update-crd-reference` and inspect the file under
  `src/content/reference/platform-api/crd/<full-name>/`.
- The generator log lines are the authoritative gap report — watch for
  `WARN - No example CR found for <crd> version <v>` and
  `WARN - skipping <crd> as no metadata found`.

## `$ARGUMENTS`

- a **CRD full name** (e.g. `silences.observability.giantswarm.io`) → locate its
  source repo in the config, check whether it has a matching example, and fix it.
- a **repo short_name** → audit every published CRD from that repo for examples.
- `audit` (or empty) → walk the whole config and report which published CRDs are
  missing an example CR.

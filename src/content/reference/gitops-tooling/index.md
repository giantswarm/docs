---
linkTitle: GitOps tooling
title: GitOps tooling reference
diataxis_content_type: reference
description: The commands, sources, and behavior of the tools used to build and validate Flux manifests locally, in one lookup table.
weight: 50
menu:
  principal:
    parent: reference
    identifier: reference-gitops-tooling
user_questions:
- Which tools can I use to build and validate Flux manifests locally?
- What is the command for fake-flux, test-all-ff, flux tree, or flux trace?
- Where do the Giant Swarm GitOps helper scripts live?
last_review_date: 2026-08-19
owner:
- https://github.com/orgs/giantswarm/teams/team-honeybadger
---

This page lists the tools for building and validating Flux manifests, with the command to invoke each one and where it comes from. For guidance on which tool to reach for when something breaks, see [tools for your GitOps workflow]({{< relref "/tutorials/continuous-deployment/tools/" >}}).

## Local build and validation

These tools run against files in your GitOps repository. They don't need cluster access.

| Tool | Command | What it does | Source |
|---|---|---|---|
| `fake-flux` | `fake-flux usage` | Mimics the `flux` CLI locally, generating resources with patches applied and variables filled in. Uses `flux build kustomization` by default, or `kustomize build` with `--use-kustomize`. | [giantswarm/gitops-template](https://github.com/giantswarm/gitops-template/tree/main/tools) |
| `test-all-ff` | `test-all-ff validate` | Finds all Flux `kustomization` files from the repository root, builds the manifests with `fake-flux`, then checks them with [`yamllint`](https://github.com/adrienverge/yamllint) and [`kubeconform`](https://github.com/yannh/kubeconform). Works in a GitHub action, locally, or as a git pre-commit hook. | [giantswarm/gitops-template](https://github.com/giantswarm/gitops-template/tree/main/tools) |
| `validate.sh` | `./validate.sh` | Like `test-all-ff`, but skips `yamllint` and checks manifests against the [OpenAPI Specification](https://github.com/OAI/OpenAPI-Specification) with `kubeconform`. Not a Giant Swarm tool. | [fluxcd/flux2-kustomize-helm-example](https://github.com/fluxcd/flux2-kustomize-helm-example/tree/main/scripts) |
| `flux build kustomization` | `flux build kustomization <name> --dry-run` | Builds a kustomization the way Flux would. In dry-run mode, secret and configmap variables aren't substituted, so the output is close to but not identical with what Flux applies. | [Flux CLI](https://fluxcd.io/flux/cmd/flux_build_kustomization/) |
| `kustomize build` | `kustomize build <dir> \| envsubst` | Builds a kustomization without substituting variables. Export them and pipe through `envsubst` yourself. Prints encrypted secrets in full, where `flux build` shows only the encryption type. Useful for checking that every secret is encrypted and for comparing key fingerprints. | [Kustomize](https://kubectl.docs.kubernetes.io/references/kustomize/cmd/build/) |

## Cluster inspection

These commands query a cluster. They don't work against local files.

| Tool | Command | What it does | Source |
|---|---|---|---|
| `flux tree` | `flux tree kustomization <name>` | Prints a tree of the resources a kustomization manages, organized by sub-kustomization and type. | [Flux CLI](https://fluxcd.io/flux/cmd/) |
| `flux trace` | `flux trace <kind> <name>` | Reports which kustomization controls a given resource, and the source revision it came from. Use it to find duplicated resources that two kustomizations are fighting over, and to check whether a resource carries the latest changes. | [Flux CLI](https://fluxcd.io/flux/cmd/) |

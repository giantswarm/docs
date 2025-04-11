---
linkTitle: Tooling
title: Tools for your GitOps workflow
description: Helpful tools for your GitOps workflow and how to use them.
weight: 80
menu:
  principal:
    parent: tutorials-continuous-deployment
    identifier: tutorials-continuous-deployment-tools
user_questions:
- What tools should I use to validate my gitops manifests?
- How can I trace resources that Flux controls?
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
last_review_date: 2025-03-14
---

These tools can help you solve issues when deploying resources with Flux. Some are created by Giant Swarm, while others come from Flux or the wider community.

We've selected tools that we find most helpful for troubleshooting Flux-controlled resources.

## Flux script

Giant Swarm created a script that mimics the `flux` CLI locally.

This script ensures your resources are correctly generated with patches applied and variables filled in.

Find it in our [gitops-template tooling](https://github.com/giantswarm/gitops-template/tree/main/tools)

For help, run `fake-flux usage` or check the examples in the repository.

## Test all with a custom script

This script works best in a GitHub action but can also run locally or in a git pre-commit hook.

It checks all manifests for errors using [`yamllint`](https://github.com/adrienverge/yamllint) and [`kubeconform`](https://github.com/yannh/kubeconform). These tools verify manifests built from Flux kustomization paths.

To use it, run `test-all-ff validate` from your GitOps repository root. The script finds all Flux `kustomization` files, builds manifests with `fake-flux`, and checks them with `yamllint` and `kubeconform`.

Find this script in our [gitops-template tooling](https://github.com/giantswarm/gitops-template/tree/main/tools).

## Flux validation

The `validate.sh` script works like `test-all-ff` but uses `kubeconform` differently. Instead of running `yamllint`, it checks manifests against the [OpenAPI Specification](https://github.com/OAI/OpenAPI-Specification).

This script isn't from Giant Swarm - find it in the [kustomize examples](https://github.com/fluxcd/flux2-kustomize-helm-example/tree/main/scripts).

## Flux build

When other tools don't help, try `flux build kustomization` with `--dry-run`. This is what `fake-flux` uses by default.

Note that in dry-run mode, secret and configmap variables aren't replaced. Your manifests won't exactly match what Flux uses on the server, but they'll be close enough to spot problems.

Learn more in the [Flux documentation](https://fluxcd.io/flux/cmd/flux_build_kustomization/).

## Kustomize build

Using `kustomize build` is more complex than `flux build kustomization`. It doesn't replace variables automatically. You need to:

1. Export environment variables
2. Build the manifest
3. Use `envsubst` in a pipe

You can do this with `fake-flux` using the `--use-kustomize` flag.

While similar to `flux build kustomization`, `kustomize build` shows encrypted secrets differently. Flux shows only the encryption type (like SOPS), while kustomize shows the entire encrypted secret.

This helps you quickly check if all secrets are encrypted and compare key fingerprints.

Find more details in the [Kustomize documentation](https://kubectl.docs.kubernetes.io/references/kustomize/cmd/build/).

## flux CLI

The `flux` CLI has many useful commands. Check their [CLI documentation](https://fluxcd.io/flux/cmd/) to learn more.

Two commands are especially helpful for checking resources on your cluster:

1. `flux tree`
2. `flux trace`

### flux tree

`flux tree` shows resources managed by a kustomization.

This command only works on a cluster, not with local files. It displays a tree of resources organized by sub-kustomization and type.

### flux trace

When looking at a cluster resource, it can be hard to know if Flux controls it and which kustomization manages it.

Sometimes resources are duplicated in your repository, causing multiple kustomizations to fight for control. Or you might create a child kustomization while the parent already controls those files.

`flux trace` helps identify which kustomization controls a resource and shows its source revision, helping you check if it has the latest changes.

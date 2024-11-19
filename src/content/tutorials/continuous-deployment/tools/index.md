---
linkTitle: Tooling
title: Tooling to support the GitOps journey
description: A description of the tools availble and how to use them to augment the GitOps journey.
weight: 80
aliases:
  - /advanced/gitops/tools
menu:
  principal:
    parent: tutorials-continuous-deployment
    identifier: tutorials-continuous-deployment-tools
user_questions:
- What tools should I use to validate my gitops manifests?
- How can I trace resources that flux controls?
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
last_review_date: 2024-11-07
---

The following scripts and tools may be used to support you in understanding issues which may arise during the deployment of resources managed by flux. Some of these tools are introduced by us here at Giant Swarm, whilst others are provided as part of the upstream package or from the community.

This is a selection of the tools we ourselves find to be the most beneficial in understanding where and how `Flux` controlled resources may fail.

### Flux script

Giant Swarm created a script to emulate the behaviour of `Flux` CLI in a local environment.

The purpose of this script is to ensure that all resources are generated correctly, patches are applied and variables substituted.

The script can be found as part of our [gitops-template tooling](https://github.com/giantswarm/gitops-template/tree/main/tools)

For advanced usage and examples, please run `fake-flux usage` or see the examples provided in the repository.

### Test all with flux custom script

This script has the most benefit when tied in with a GitHub action but may also be run locally either independently or as part of a git pre-commit hook.

The purpose of the script is to check all generated manifests for linting and validation errors. It achieves this by using both [`yamllint`](https://github.com/adrienverge/yamllint) and [`kubeconform`](https://github.com/yannh/kubeconform) to verify a compiled version of all manifests discovered from a flux `kustomization`
`spec.path`.

Usage of the script is simple; from the root of your GitOps repository run `test-all-ff validate`. The script will then find all Flux `kustomization` files, execute `fake-flux` to build a monolithic manifest for each `kustomization` found, and then parse that manifest with `yamllint` and `kubeconform`.

The script can be found as part of our [gitops-template tooling](https://github.com/giantswarm/gitops-template/tree/main/tools).

### Flux validation

Similar to `test-all-ff`, validation script `validate.sh` also parses your manifests with `kubeconform`, however it does this slightly differently and whilst it doesn't execute `yamllint` over your generated manifests for you, it instead parses your manifests against the [OpenAPI Specification](https://github.com/OAI/OpenAPI-Specification).

Validation script isn't provided by Giant Swarm directly but instead can be found as part of the [`Kustomize`
examples](https://github.com/fluxcd/flux2-kustomize-helm-example/tree/main/scripts).

### Flux build

When none of the above tools give you the output you are looking for, it's possible to call `flux build `kustomization`` in `--dry-run` mode. In fact when using `fake-flux` in its default mode, this is exactly what it does under the hood.

When using dry-run mode, it's important to note that variable substitutions from `Secrets` or `ConfigMaps` are skipped so your manifests may not be exactly what's parsed by flux on the server but it will give you a close enough approximation to allow you to verify your manifests are likely build and succeed when deployed to the cluster.

Documentation on `flux build kustomization` can be found in the [`Flux` documentation here](https://fluxcd.io/flux/cmd/flux_build_kustomization/).

### Kustomize build

This is slightly more complex than using `flux build kustomization` as by default, `kustomize` won't carry out any substitutions for you. These should instead be carried out at the end of the process by first exporting them as environment variables, building the manifest and then finally calling `envsubst` as part of a chained pipe.

This behaviour is also integrated into `fake-flux` for you and can be activated with the `--use-kustomize` flag to the script.

Whilst there aren't many benefits to using `kustomize build` over `flux build kustomization` it can, in certain instances offer a quick visual check to ensure your secrets have all been encrypted correctly.

The difference here is `flux build kustomization` replaces the contents of your secret with the type of encryption used such as `**SOPS**` whilst `kustomize build` will display instead the entire encrypted secret.

__Note__: As a quick visual guide, this may be preferable to ensure your secrets are all encrypted and gives you the opportunity to visually compare key fingerprints.

Documentation on `kustomize build` can be found in the [`Kustomize` documentation here](https://kubectl.docs.kubernetes.io/references/kustomize/cmd/build/).

### flux

There are many useful commands in flux and to understand this as a tool we recommend you browse their comprehensive CLI documentation which can be found at [https://fluxcd.io/flux/cmd/](https://fluxcd.io/flux/cmd/). However, when understanding resources on the cluster, there are two commands in particular that should be brought to your attention as these offer a great deal of benefit in determining if a resource is controlled by flux and whether it has the latest changes.

#### flux tree

The `flux tree`command will show you a list of resources a `kustomization` manages.

This command can't be used against local manifests but is instead run against the server and will print out
a tree of all resources organized by sub-kustomization and sorted by type.

#### flux trace

When looking at any given resource on a cluster, it's not always easy to understand if that resource is controlled via `Flux`, and if so, which `kustomization` controls it.

Occasionally you might find a resource has been duplicated in your repository so it's now being controlled by multiple `kustomizations` which are fighting for control, other times you may create a child `kustomization` but the child directory is actually controlled at a higher level.

`Flux` trace helps identify the `kustomization` controlling the resource you're looking interested in and will show you the source revision for that resource, additionally helping you determine if it's received the latest changes.

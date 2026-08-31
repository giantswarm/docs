---
title: Create and deploy an agent
diataxis_content_type: tutorial
linkTitle: Create an agent
description: Create an AI agent in the developer portal, review the Kubernetes manifests the form generates, deploy it with your own identity, and watch it become ready.
weight: 8
menu:
  principal:
    parent: tutorials-agent-platform
    identifier: tutorials-agent-platform-create-an-agent
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
last_review_date: 2026-08-31
user_questions:
  - How do I create an AI agent on the platform?
  - What resources does the create-agent form generate?
  - Why does my agent only appear after a while?
  - How do I change an agent after deploying it?
---

In this tutorial you create an AI agent through the developer portal and deploy it to the platform. Along the way you'll see what the flow really does. The form generates plain Kubernetes manifests, applies them with *your* identity, and the agent comes to life when the cluster reconciles them. There's no hidden agent API—what you deploy is what any teammate could read back with `kubectl`.

## Before you start

You need:

- A developer portal with the [Agent Platform section enabled]({{< relref "/tutorials/agent-platform/enable-portal-features" >}}), including the deploy prerequisites.
- Permission to create resources in the target namespace. The flow applies manifests with your token, so your Kubernetes RBAC decides whether the deploy succeeds.
- At least one model configuration on the installation—the form lists the models the platform offers and won't proceed without one.

## Step 1: Describe the agent

In the portal, go to **Agent Platform** → **Agents** and choose to create a new agent. The first step asks for:

- **Installation**: which cluster the agent runs on. Only installations with at least one model configuration are offered.
- **Name**: the display name. A URL-friendly technical name is derived from it—that becomes the name of the agent's Kubernetes resources, and it also seeds the agent's avatar, which you see rendered live as you type.
- **Description**: one sentence on what the agent is for.
- **Model**: pick one of the installation's model configurations.
- **System prompt**: the agent's standing instructions. The field is pre-seeded with the platform's default; make it your own.

## Step 2: Pick skills

If your portal has skill repositories configured, the second step offers every skill discovered in them—capability bundles the agent gets mounted at runtime. Search, pick what fits, and continue. No selection is fine: an agent without skills is just a model with your system prompt.

## Step 3: Review what will be applied

The review step shows the exact manifests the form generated—this is the honest heart of the flow. Two resources:

- An `OCIRepository` pointing at the platform's agent Helm chart. It tracks the chart by SemVer range, so your agent picks up chart releases automatically.
- A `HelmRelease` named after your agent, carrying your form inputs—system prompt, model, skills—as inline chart values.

What you see is what gets applied, verbatim. The review page also offers the equivalent `helm install` command: the portal has no special powers, and the same values deployed from your terminal produce the same agent.

An agent is versioned as **one unit**: prompt, toolchain, and skills ship together in one release. There's no way to patch one of them independently—changing anything means deploying a new revision of the whole unit, which keeps every agent version reproducible.

## Step 4: Deploy

Deploy applies the two manifests to the cluster **with your token**. This is where RBAC gates the flow. If you aren't allowed to create these resources in the target namespace, the apply fails with a real `403` error: the portal doesn't escalate for you. On success you land on the live task log of the apply.

## Step 5: Watch it become ready

Applying the manifests isn't the end: the agent exists once **Flux reconciles the release**, typically within a minute. Watch your agent's detail page: it shows readiness, the controller's status message, and every condition verbatim.

Two things are normal here:

- A short gap between "deployed" and "ready" while the release reconciles and the agent's pod starts.
- Some invalid configurations only surface *now*: the form validates what it can, but the chart and controller have the final word, so a value the schema allows can still fail at reconcile time. The status conditions on the detail page tell you why.

Once ready, the agent appears in the portal's agent list and in the platform's chat surfaces. It reaches its tools through the same gateway as you do—acting with the identity of whoever talks to it.

## Changing or removing the agent

- **Change**: deploy a new revision with updated values—the same flow, same name. There's no in-place edit, by design.
- **Remove**: delete the agent from its detail page. The delete is gated on your RBAC for the underlying release, and the portal refuses to delete an agent whose desired state lives in Git—removing that one means removing it from the repository it's managed in.

## What you learned

The portal's create flow is a manifest generator with a review step: Kubernetes resources applied with your identity, reconciled by the cluster, versioned as one unit. That's the platform principle at work—the portal is a peer client of the Kubernetes API, not a privileged control panel.

## Related

- [Agent Platform in the developer portal]({{< relref "/overview/developer-portal/agent-platform" >}}) - The whole section, including sessions and the tool explorer.
- [What's the Agent Platform]({{< relref "/overview/agent-platform/introduction" >}}) - The concepts behind what you just deployed.

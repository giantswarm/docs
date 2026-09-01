---
title: Run the Agent Platform locally with agentlab
diataxis_content_type: tutorial
linkTitle: Local playground
description: Stand up the real Agent Platform topology on a throwaway kind cluster with one binary, sign in as lab users, and connect your MCP client to a local Muster.
weight: 5
menu:
  principal:
    parent: tutorials-agent-platform
    identifier: tutorials-agent-platform-local-playground
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
last_review_date: 2026-09-01
user_questions:
  - How do I try the Agent Platform without a real cluster?
  - What is agentlab?
  - Why does agentlab ask for sudo once?
  - How do I remove the agentlab certificate trust again?
  - How do I run agents on my own self-hosted model in agentlab?
---

**agentlab** stands up the real Agent Platform topology—agentgateway edge, Muster, the developer portal, the agent runtime, and a bundled Dex identity provider—on a throwaway [kind](https://kind.sigs.k8s.io/) cluster, with one binary. It's the fastest way to experience the platform end to end: real OAuth logins, real RBAC, real MCP tool calls, all on your laptop and fully disposable.

In this tutorial you bring the lab up, trust its certificate authority, sign in as different users, and connect your MCP client to the local Muster.

## Prerequisites

- `docker`
- `kind` (0.31 or newer)
- `kubectl`
- `helm` (**version 4**: Helm 3 can't store the platform chart's release, because the dependency archives put the release Secret over the 1 MiB cap)
- `git`, and Go 1.25 or newer if you build from source
- Optional: an `ANTHROPIC_API_KEY`, which powers the agents and the portal's AI chat

Port 443 must be free on your machine: the lab's edge gateway binds it, and the portal breaks behind a non-443 edge.

## Step 1: Install agentlab

```sh
go install github.com/giantswarm/agentlab@latest
```

Alternatively, download a release asset (named `agentlab-<os>-<arch>`) from the [releases page](https://github.com/giantswarm/agentlab/releases) and save it as `agentlab`, or clone the repository and `go build -o agentlab .`.

## Step 2: Bring the lab up

```sh
export ANTHROPIC_API_KEY=sk-ant-...   # optional
agentlab configure --defaults
agentlab up
```

`configure --defaults` writes the canonical lab: the agent platform behind the agentgateway edge, the developer portal on, three users, Dex on port 32000. `up` mints certificates, creates the kind cluster, deploys Dex, RBAC, and the platform—and verifies each step. Running `agentlab` with no arguments opens an interactive dashboard with live component status instead.

## Step 3: Trust the lab CA

```sh
agentlab trust    # one sudo prompt; agentlab untrust reverts it
```

Everything the lab serves over TLS chains to a **lab certificate authority** minted per machine, whose private key never leaves your computer. `trust` installs it into your system trust store (and Firefox/Chromium profiles where the NSS `certutil` tool is present), so every lab URL gets a green lock.

The CA you're trusting is narrow by design:

- **X.509 name constraints** pin it to the lab's own hostnames and to `127.0.0.0/8`, so a leaked key couldn't sign for the web at large.
- `agentlab untrust` removes exactly the lab CA again; `agentlab down` never touches trust stores.
- A public certificate authority can't serve a laptop lab: public CAs don't issue for `127.0.0.1` addresses, which is the whole point of a name-constrained local CA.

Skipping this step also works—expect browser warnings once per hostname, and set `NODE_EXTRA_CA_CERTS` to the lab's CA file for Node-based clients.

## Step 4: Connect your MCP client

```sh
claude mcp add --transport http muster https://muster.127.0.0.1.nip.io/mcp
```

Then, in Claude Code, run `/mcp`, choose authenticate, and sign in on the real Dex login page as one of the lab users. Any MCP client that supports remote OAuth-protected servers works the same way.

The lab's URLs:

| Surface | URL |
|---|---|
| Muster MCP endpoint | `https://muster.127.0.0.1.nip.io/mcp` |
| Developer portal | `https://backstage.127.0.0.1.nip.io` |
| Identity provider (Dex) | `https://localhost:32000/dex` |

The `nip.io` wildcard DNS resolves these names to `127.0.0.1`, so the lab needs public DNS resolution to work, even though all traffic stays on your machine.

## Step 5: Things to try

The default lab ships three users, all with the password `password`:

| User | Effective access |
|---|---|
| `admin@lab.local` | Cluster admin |
| `dev@lab.local` | Edit, inside the `demo` namespace only |
| `viewer@lab.local` | View, cluster-wide |

- **Watch RBAC work.** Ask your assistant to list pods as `admin@lab.local`, then sign out and repeat as `dev@lab.local`: the same tool call now answers with what that user may see. `agentlab test` asserts the RBAC matrix headless.
- **Run the seeded workflow.** The lab seeds one Muster workflow, `lab-cluster-overview`, which lists namespaces and pods through the Kubernetes MCP server—one click in the portal's workflow tab exercises the whole chain.
- **Create an agent.** Open the portal, sign in, and walk the [create-an-agent flow]({{< relref "/tutorials/agent-platform/create-an-agent" >}}) against your own lab.
- **Prove the platform headless.** `agentlab platform-test` drives Dex → Muster → the Kubernetes MCP server → the API server without a browser.
- **Bring your own model.** The default agents run on Anthropic, but `platform.extraModels` in `agentlab.yaml` adds more model configurations: a self-hosted OpenAI-compatible endpoint (vLLM, llama.cpp), OpenRouter, Gemini, or an Ollama host.

  ```yaml
  platform:
    extraModels:
      - name: qwen3                # a self-hosted vLLM, no API key needed
        provider: OpenAI
        model: qwen3-8-27b
        baseUrl: https://qwen.example.internal/v1
      - name: openrouter-deepseek  # any OpenAI-compatible SaaS works the same way
        provider: OpenAI
        model: deepseek/deepseek-chat
        baseUrl: https://openrouter.ai/api/v1
        apiKeyEnv: OPENROUTER_API_KEY
  ```

  Re-run `agentlab platform` and pick the model when creating an agent. `apiKeyEnv` names an environment variable read from your shell at deploy time, so keys stay out of the file; keyless endpoints work without it. The `baseUrl` must be reachable from inside the cluster, meaning a LAN address rather than `localhost`. Entries you remove are pruned on the next run.

When you're done: `agentlab down` deletes the cluster; `agentlab untrust` removes the CA.

## Limitations

The lab is honest about being a lab:

- Ports are fixed at cluster creation; changing them means recreating the cluster. Port 443 is required.
- The `nip.io` hostnames depend on public DNS resolution.
- Firefox without `certutil` doesn't see the system trust store, and on WSL2 the Windows-side browser has its own trust store. `agentlab trust` inside WSL covers curl, Node, and Claude Code there.
- The Kubernetes MCP server runs a **write-capable** profile by default: agents you authorize can change the lab cluster. That's the point of a playground—and it's your laptop, not production.
- The bundled Dex ships static users and throwaway passwords by design. Nothing about the lab's identity setup is production guidance—for the real thing, see [Install the Agent Platform on your own cluster]({{< relref "/tutorials/agent-platform/install-standalone" >}}).

## Related

- [What's the Agent Platform]({{< relref "/overview/agent-platform/introduction" >}}) - The concepts the lab makes tangible.
- [Agent Platform architecture]({{< relref "/overview/agent-platform/architecture" >}}) - The topology the lab reproduces.
- [Set up your AI agent]({{< relref "/getting-started/ai-agent-setup" >}}) - The same client setup against a real installation.

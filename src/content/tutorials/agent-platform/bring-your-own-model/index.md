---
title: Bring your own model for the Agent Platform
diataxis_content_type: how-to-guide
linkTitle: Bring your own model
description: Give the Agent Platform's agent runtime a model to run on. Supply the API key for the default model configuration, add your own model configuration for any provider, or create one in the UI.
weight: 68
menu:
  principal:
    parent: tutorials-agent-platform
    identifier: tutorials-agent-platform-bring-your-own-model
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
last_review_date: 2026-09-08
user_questions:
  - Why does the default model show as not accepted in the developer portal?
  - How do I provide the API key for the Agent Platform's default model?
  - How do I add a model from OpenAI, Azure OpenAI, Gemini, Ollama or a self-hosted endpoint?
  - Why does my agent not start although its model configuration is accepted?
  - How do I check which models the Agent Platform can run agents on?
---

The Agent Platform's agent runtime runs every agent on a **model configuration**: a `ModelConfig` resource in the `kagent` namespace of the management cluster that names a provider, a model, and the Secret holding the provider's API key. Giant Swarm installs the runtime **without any model credential**. The model, the provider and the key are yours: your contract, your bill, your data-processing terms.

Out of the box, one model configuration exists, `default-model-config` (Anthropic, `claude-sonnet-4-6`). It references a Secret named `kagent-anthropic-key` in the `kagent` namespace that doesn't exist yet. Until you create it, the developer portal's **Models** tab shows the model as **Not accepted**, the create-an-agent flow has no model to offer, and an agent deployed against it doesn't start. Everything else works: the runtime, its UI, the API and the portal integration.

This guide shows three ways to make a model available. Pick one:

- [Provide the API key for the default model](#option-1-provide-the-api-key-for-the-default-model) through your GitOps repository. The least work if Anthropic is your provider.
- [Add your own model configuration](#option-2-add-your-own-model-configuration) through your GitOps repository, for any supported provider: Anthropic, OpenAI, Azure OpenAI, Gemini, Ollama, or an OpenAI-compatible endpoint you host yourself.
- [Create a model configuration in the UI](#option-3-create-a-model-configuration-in-the-ui), in the developer portal or in the UI of the agent runtime. Quickest to try, but the result lives on the cluster only, not in Git.

## Before you start

You need:

- An API key from your model provider, or a self-hosted endpoint that agents can reach from inside the management cluster.
- For the GitOps options: write access to your management-clusters repository, the one Flux on the management cluster reconciles, and the `sops` command line tool. The repository's `.sops.yaml` carries the installation's public age key, so you can encrypt Secrets without holding any private key.
- For the UI option: a developer portal with the [Agent Platform section enabled]({{< relref "/tutorials/agent-platform/enable-portal-features" >}}), or access to the agent runtime UI at `https://kagent.<installation>.<base domain>`. Both sign you in through your installation's single sign-on.
- To check the result with `kubectl`: read access to the `kagent` namespace of the management cluster.

## How model configurations work

A `ModelConfig` is small. The controller reads it, looks up the referenced Secret in the same namespace, and sets an `Accepted` condition on the resource:

```yaml
apiVersion: kagent.dev/v1alpha2
kind: ModelConfig
metadata:
  name: default-model-config
  namespace: kagent
spec:
  provider: Anthropic
  model: claude-sonnet-4-6
  apiKeySecret: kagent-anthropic-key
  apiKeySecretKey: ANTHROPIC_API_KEY
```

Three things are worth knowing before you create anything:

- **The key reaches the agent as the provider's environment variable.** The controller mounts the value found under `apiKeySecretKey` in the Secret as `ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, `AZURE_OPENAI_API_KEY` or `GOOGLE_API_KEY`, whichever the provider expects. The key name inside the Secret is yours to choose, but naming it after that variable, as the default configuration and the portal do, keeps every Secret self-explanatory. Ollama needs no key.
- **Accepted means the configuration is well-formed and its Secret exists.** It doesn't prove the key is valid or the endpoint reachable. That only shows when an agent starts.
- **An endpoint that ignores API keys still needs one.** A self-hosted OpenAI-compatible server such as vLLM or llama.cpp never checks the key, but an agent without the environment variable stops at boot. Give such a model a Secret with a placeholder value.

The portal's **Models** tab lists every model configuration of every installation with its `Accepted` state, and shows the controller's message as a tooltip on a **Not accepted** model. Typically the message names the missing Secret.

If a firewall or proxy restricts the management cluster's outbound traffic, allow the provider's domain first. The [Agent Platform section of the domain allowlist]({{< relref "/overview/security/domain-allowlist#agent-platform" >}}) lists the domain per provider.

## Option 1: Provide the API key for the default model

Create the Secret the default model configuration already references. On the management cluster's GitOps repository, the Agent Platform's extra resources live under `management-clusters/<installation>/extras/agent-platform/`, and its Secrets in a `secrets` directory next to them. Encrypted Secrets are decrypted by Flux on the cluster.

1. Write the Secret as a manifest. Generating it with `kubectl` avoids typos in the key name:

    ```sh
    kubectl create secret generic kagent-anthropic-key \
      --namespace kagent \
      --from-literal=ANTHROPIC_API_KEY=<your Anthropic API key> \
      --dry-run=client --output yaml \
      > management-clusters/<installation>/extras/agent-platform/secrets/kagent-anthropic-key.yaml
    ```

2. Encrypt it in place. The repository's `.sops.yaml` selects the installation's age recipient by path, so the file must sit under the installation's directory before you encrypt:

    ```sh
    sops --encrypt --in-place management-clusters/<installation>/extras/agent-platform/secrets/kagent-anthropic-key.yaml
    ```

    Check the result before you commit: `data:` values now start with `ENC[`, and a `sops:` block with your installation's age recipient closes the file. Never commit the plaintext version. The repository's pre-merge scans reject a plaintext key in any commit of a pull request, including commits you later amend.

3. Add the file to `secrets/kustomization.yaml` in the same directory. On a managed installation that directory already exists with the other Secrets of the runtime, so this is one more line:

    ```yaml
    apiVersion: kustomize.config.k8s.io/v1beta1
    kind: Kustomization
    resources:
      - kagent-oauth2-proxy-credentials.yaml
      - kagent-anthropic-key.yaml
    ```

    If your installation has no `secrets` directory yet, create it with that `kustomization.yaml` and add `- ./secrets` to the `resources` list of `extras/agent-platform/kustomization.yaml`.

4. Open a pull request and merge it. Flux applies the Secret on its next reconciliation, typically within a few minutes, and the controller flips `default-model-config` to `Accepted`.

To rotate the key later, replace the value in the plaintext manifest, encrypt again and merge. The controller tracks a hash of the Secret and picks up the change.

## Option 2: Add your own model configuration

Any provider the runtime supports works the same way: a `ModelConfig` plus, for every provider except Ollama, a Secret with the provider's canonical key name. Both go into the same `secrets` directory as in option 1, and both are listed in its `kustomization.yaml`. Only the Secret is encrypted; the `ModelConfig` holds no credential.

{{% notice note %}}
The `.sops.yaml` of a managed installation encrypts every file whose path contains `secret` or `credential`. A `ModelConfig` manifest placed in the `secrets` directory is therefore encrypted too if you run `sops` on it. That's harmless, since Flux decrypts it, but you can also keep model configurations one level up next to `kustomization.yaml` and list them there.
{{% /notice %}}

The name of the `ModelConfig` is what agents reference and what the portal displays. Keep it short and lowercase.

### Anthropic

The Secret can be the same `kagent-anthropic-key` as the default model uses, so a second Anthropic model needs no second key:

```yaml
apiVersion: kagent.dev/v1alpha2
kind: ModelConfig
metadata:
  name: anthropic-opus
  namespace: kagent
spec:
  provider: Anthropic
  model: claude-opus-5
  apiKeySecret: kagent-anthropic-key
  apiKeySecretKey: ANTHROPIC_API_KEY
```

### OpenAI

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: kagent-openai-key
  namespace: kagent
stringData:
  OPENAI_API_KEY: <your OpenAI API key>
---
apiVersion: kagent.dev/v1alpha2
kind: ModelConfig
metadata:
  name: openai-gpt
  namespace: kagent
spec:
  provider: OpenAI
  model: gpt-4.1
  apiKeySecret: kagent-openai-key
  apiKeySecretKey: OPENAI_API_KEY
```

### Azure OpenAI

The endpoint and API version are required. The model is the name of your Azure deployment:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: kagent-azure-openai-key
  namespace: kagent
stringData:
  AZURE_OPENAI_API_KEY: <your Azure OpenAI key>
---
apiVersion: kagent.dev/v1alpha2
kind: ModelConfig
metadata:
  name: azure-gpt
  namespace: kagent
spec:
  provider: AzureOpenAI
  model: <your deployment name>
  apiKeySecret: kagent-azure-openai-key
  apiKeySecretKey: AZURE_OPENAI_API_KEY
  azureOpenAI:
    azureEndpoint: https://<your resource>.openai.azure.com/
    apiVersion: "2025-04-01-preview"
    azureDeployment: <your deployment name>
```

### Gemini

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: kagent-gemini-key
  namespace: kagent
stringData:
  GOOGLE_API_KEY: <your Gemini API key>
---
apiVersion: kagent.dev/v1alpha2
kind: ModelConfig
metadata:
  name: gemini-flash
  namespace: kagent
spec:
  provider: Gemini
  model: gemini-2.5-flash
  apiKeySecret: kagent-gemini-key
  apiKeySecretKey: GOOGLE_API_KEY
```

### Ollama

No Secret. The host must be reachable from pods on the management cluster:

```yaml
apiVersion: kagent.dev/v1alpha2
kind: ModelConfig
metadata:
  name: ollama-llama
  namespace: kagent
spec:
  provider: Ollama
  model: llama3.2
  ollama:
    host: http://ollama.models.svc.cluster.local:11434
```

### OpenAI-compatible endpoint

vLLM, llama.cpp, LiteLLM, OpenRouter and most inference servers speak the OpenAI API. Use the `OpenAI` provider with a `baseUrl`. If the endpoint doesn't check keys, the Secret still has to exist, with any value:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: kagent-qwen-key
  namespace: kagent
stringData:
  OPENAI_API_KEY: unused
---
apiVersion: kagent.dev/v1alpha2
kind: ModelConfig
metadata:
  name: qwen
  namespace: kagent
spec:
  provider: OpenAI
  model: Qwen/Qwen3-32B
  apiKeySecret: kagent-qwen-key
  apiKeySecretKey: OPENAI_API_KEY
  openAI:
    baseUrl: https://inference.example.internal/v1
```

For an endpoint with a certificate from your own certificate authority, add a `tls` block: `tls.caCertSecretRef` and `tls.caCertSecretKey` point at a Secret holding the CA bundle, and `tls.disableVerify: true` skips verification altogether for lab endpoints.

The full field list of every provider block is in the resource definition on your cluster:

```sh
kubectl explain modelconfig.spec
kubectl explain modelconfig.spec.openAI
```

## Option 3: Create a model configuration in the UI

Both interfaces write the same two resources as option 2, directly to the cluster with your identity. Nothing is committed to Git, so a model created this way is visible and editable in the portal and doesn't survive a rebuild of the cluster from its repository.

**In the developer portal**, open **Agent Platform** → **Models** and choose **Add model**. The form covers OpenAI (including any OpenAI-compatible endpoint), Anthropic, Gemini and Ollama, with an optional endpoint, a switch for endpoints that need no key, and a TLS verification toggle. The API key you enter is stored as a Secret named `kagent-<model name>` next to the model configuration and never displayed again. The write goes through the Kubernetes API with your token, so your RBAC on the `kagent` namespace decides whether it succeeds.

**In the agent runtime UI** at `https://kagent.<installation>.<base domain>`, sign in and open **Models** → **New model**. Its form offers every provider the runtime supports and creates the Secret for you as well.

Models the portal or the runtime UI can't edit are the ones something else manages: the chart's default model, or anything applied from Git. The portal says so in place.

## Check the result

On the cluster, the `Accepted` column tells you whether each model is ready for agents:

```sh
kubectl --namespace kagent get modelconfig \
  --output custom-columns='NAME:.metadata.name,PROVIDER:.spec.provider,MODEL:.spec.model,ACCEPTED:.status.conditions[?(@.type=="Accepted")].status'
```

```text
NAME                   PROVIDER    MODEL               ACCEPTED
default-model-config   Anthropic   claude-sonnet-4-6   True
```

When a model stays `False`, the condition's message says why:

```sh
kubectl --namespace kagent get modelconfig default-model-config \
  --output jsonpath='{.status.conditions[?(@.type=="Accepted")].message}{"\n"}'
```

In the developer portal, the **Models** tab shows the same state with an **Accepted** or **Not accepted** label per model. Once a model is accepted, the installation appears in the create-an-agent flow and the model in its picker. From there, [create and deploy an agent]({{< relref "/tutorials/agent-platform/create-an-agent" >}}) to see the model answer.

## Troubleshooting

**The model isn't accepted and the message says the Secret wasn't found.** The Secret's name or namespace doesn't match `apiKeySecret`, or Flux hasn't applied it yet. Check `kubectl --namespace kagent get secret <name>`. If it's missing although the pull request is merged, check the Flux `Kustomization` that reconciles the installation's extras for an error: a Secret whose file isn't listed in a `kustomization.yaml`, or one that couldn't be decrypted, shows up there.

**The model is accepted but the agent's pod never starts and reports a missing Secret key.** `apiKeySecretKey` names a key the Secret doesn't have. Compare it with `kubectl --namespace kagent get secret <name> --output jsonpath='{.data}'`, which lists the key names, and fix whichever side is wrong.

**The model is accepted but the agent's pod restarts with an error that the API key isn't set.** The model configuration references no Secret at all, which the controller accepts for a keyless endpoint but the agent runtime doesn't. Add a Secret with a placeholder value and reference it, as in the OpenAI-compatible example above.

**The agent starts but every request fails with an authentication error.** The key is present but invalid or lacks access to the model. Test the key against the provider's API directly with the same model name.

**The model is accepted but every request fails with a connection reset or a TLS error.** An egress firewall or proxy in front of the management cluster allows only listed domains, and the provider's domain isn't among them. The requests leave from pods on the management cluster, so the rule has to cover the cluster's nodes, not your workstation. Allow the domain for your provider from the [Agent Platform section of the domain allowlist]({{< relref "/overview/security/domain-allowlist#agent-platform" >}}) and try again.

**A self-hosted endpoint times out.** The `baseUrl` must be reachable from pods in the `kagent` namespace of the management cluster, and network policies on that cluster may need an egress rule for the endpoint's address and port. `localhost` and machine-local addresses never work from a pod.

## Related

- [Create and deploy an agent]({{< relref "/tutorials/agent-platform/create-an-agent" >}}) - The flow that needs an accepted model.
- [Agent Platform in the developer portal]({{< relref "/overview/developer-portal/agent-platform" >}}) - The section the Models tab belongs to.
- [Enable Agent Platform features in Backstage]({{< relref "/tutorials/agent-platform/enable-portal-features" >}}) - Turning the section on in your portal instance.
- [Install the Agent Platform on your own cluster]({{< relref "/tutorials/agent-platform/install" >}}) - Where the same model configurations live when you run the platform yourself.

---
title: Sharing secrets with our team
diataxis_content_type: how-to-guide
description: When getting started with Giant Swarm, some secrets and credentials need to be shared. Learn how to do it securely.
weight: 50
menu:
  principal:
    parent: overview-security
    identifier: overview-security-sharing-secrets
owner:
  - https://github.com/orgs/giantswarm/teams/team-shield
user_questions:
  - How do I share a secret with Giant Swarm?
  - How do I share cloud provider credentials with Giant Swarm?
last_review_date: 2026-07-16
---

Getting started with Giant Swarm involves an initial setup that includes sharing some credentials with us, and other secrets may need to be shared as our partnership grows. Our goal is to make sharing secrets with us as easy and secure as possible. There are two ways to do it.

## Use your own secure sharing method

We're happy to receive secrets through whatever secure sharing method you already use. Ask your Giant Swarm engineer, agree on a method that works for both sides, and confirm it before sending anything sensitive.

One convenient command-line option is [`age`](https://github.com/FiloSottile/age), which can encrypt a file to the public keys attached to a GitHub profile. Ask your engineer for their GitHub username, then encrypt your secret to their keys:

```bash
curl https://github.com/<username>.keys | age --recipients-file - my_secret.txt > my_secret.txt.age
```

Share the resulting `.age` file with the engineer, who can decrypt it with their private key. To decrypt a secret that's been shared with you, run:

```bash
age --decrypt -i <path-to-ssh-key> -o my_secret.txt my_secret.txt.age
```

## Let us create a 1Password share item

Alternatively, we can create a [1Password](https://1password.com/) share item and send you a secure link to exchange the secret. Ask your Giant Swarm engineer to set one up.

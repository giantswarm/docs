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
  - Can I share a secret with Giant Swarm through 1Password?
last_review_date: 2026-09-16
---

Getting started with Giant Swarm involves an initial setup that includes sharing some credentials with us, such as cloud provider credentials or a VPN passphrase. Other secrets may need to be shared as our partnership grows. Our goal is to make sharing secrets with us as easy and secure as possible.

Whatever option you pick, please don't send secrets in plain text via Slack, email, a GitHub issue, or an onboarding checklist. Agree on a method with your Giant Swarm account engineer first, then send the secret.

## Use your own secure sharing method

We're happy to receive secrets through whatever secure sharing method you already use. Most password managers, for example, can share an item with an external email address. Ask your Giant Swarm engineer, agree on a method that works for both sides, and confirm it before sending anything sensitive.

One convenient command-line option is [`age`](https://github.com/FiloSottile/age), which can encrypt a file to the public keys attached to a GitHub profile. Ask your engineer for their GitHub username, then encrypt your secret to their keys:

```bash
curl https://github.com/<username>.keys | age --recipients-file - my_secret.txt > my_secret.txt.age
```

Share the resulting `.age` file with the engineer, who can decrypt it with their private key. To decrypt a secret that's been shared with you, run:

```bash
age --decrypt -i <path-to-ssh-key> -o my_secret.txt my_secret.txt.age
```

## Use a 1Password guest vault

If you don't have a sharing method in place, we can invite you as a guest to our [1Password](https://1password.com/) account. You get access to a dedicated vault that exists only for this handover. Here's how it works:

1. Tell your engineer the email address of the person who will share the secret.
2. Accept the invitation you receive from 1Password and set up your guest account. Let your engineer know once you're in, and we grant you access to the vault.
3. Create an item in the vault and add the secret.
4. Wait for your engineer to confirm that the item has been moved into our own vault.
5. Expect us to remove the guest access and the vault afterward.

## Encrypt with our GPG key

As a fallback, your engineer can share a GPG public key with you. Encrypt the secret with that key and send us the encrypted file. Only we can decrypt it.

## When we share a secret with you

When we need to send you a secret, we create a 1Password share link. We restrict the link to your email address and set it to expire after a short time.

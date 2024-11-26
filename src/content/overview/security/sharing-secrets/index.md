---
title: Sharing secrets with our team
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
last_review_date: 2024-11-26
---

Getting started with Giant Swarm involves an initial setup that includes sharing some credentials with us. It can also happen that some other secrets need to be shared along our partnership, as customers progress in their cloud-native journey. Our goal is that customers can share secrets in the easiest and most secure ways: hence, in this page two different tools are presented for sharing secrets with us.

## Option #1: Using `Keybase`

The [`Keybase`](https://keybase.io/) project provides a secure messaging and file-sharing app that enjoys end-to-end encryption by means of public-key cryptography. In other words, every user has its own private-public key pair for sending messages securely. Since messages are encrypted using the recipient's public key, only the recipient can decrypt them as it's the only entity owning the private key needed for decryption.

If `Keybase` is your tool of choice for sharing secrets with us, ask our engineer for their `Keybase` username, verify with them that everything is working, and share the secret securely with them.

## Option #2: Using `age`

The [`age`](https://github.com/FiloSottile/age) project offers a simple command-line tool that allows for encrypting secrets easily and in a classic UNIX-style fashion. A lovely feature about `age` is the possibility to encrypt messages using the public keys associated with a `GitHub` profile.

If `age` is your tool of choice for sharing secrets with us, ask our engineer for their `GitHub` username, run a command such as `curl https://github.com/<USERNAME>.keys | age --recipients-file - my_secret.txt > my_secret.txt.age` in your shell and share the `.age` file with the engineer. The engineer will be able to decrypt it using their private key.

In case you need to decrypt a secret shared with you, run a command such as `age --decrypt -i <PATH_TO_SSH_KEY> -o my_secret.txt my_secret.txt.age` in your shell.

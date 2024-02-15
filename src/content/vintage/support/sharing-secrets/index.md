---
linkTitle: Sharing secrets with us
title: Sharing secrets with Giant Swarm
description: When getting started with Giant Swarm, some secrets will need to be shared. In this page, we describe how to do it safely and effectively.
weight: 40
menu:
  main:
    parent: support-training
owner:
  - https://github.com/orgs/giantswarm/teams/team-teddyfriends
user_questions:
  - How do I share a secret with Giant Swarm?
  - How do I share cloud provider credentials with Giant Swarm?
last_review_date: 2022-12-13
aliases:
  - /getting-started/sharing-secrets/
---

Getting started with Giant Swarm involves an initial setup that includes sharing some credentials with us. It can also happen that some other secrets need to be shared along our partnership, as customers progress in their cloud-native journey. We want our customers to be able to share secrets in the easiest and most secure ways: hence, in this page we suggest two approaches which we think get the best of both worlds.

## Option #1: Using Keybase

[Keybase](https://keybase.io/) is a secure messaging and file-sharing app that enjoys end-to-end encryption by means of public-key cryptography. In other words, every user has its own private-public key pair for sending messages safely. Since messages are encrypted using the recipient's public key, only the recipient can decrypt them as they are the only entity owning the private key needed for decryption.

If Keybase is your tool of choice for sharing secrets with us, ask your Account Engineer for their Keybase username, verify with them that everything is working, and share the secret safely with them.

## Option #2: Using `age`

[age](https://github.com/FiloSottile/age) is a simple command-line tool that allows for encrypting secrets easily and in a classic UNIX-style fashion.
A lovely feature about `age` is the possibility to encrypt messages using the public key(s) associated with a GitHub profile.

If `age` is your tool of choice for sharing secrets with us, ask your Account Engineer for their GitHub username, run a command such as
`curl https://github.com/AE_USERNAME.keys | age --recipients-file - my_secret.txt > my_secret.txt.age` in your shell and share the `.age` file with your Account Engineer.

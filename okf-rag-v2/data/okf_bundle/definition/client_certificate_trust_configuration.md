---
type: Definition
title: Client Certificate Trust Configuration
description: Describes the requirement for CA certificate configuration on the client
  side when using a private certificate authority.
resource: source://security__controlling-access.md
tags:
- certificate
- client configuration
- trust
- ca
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- CA certificate
- ~/.kube/config
- client certificate trust
- private CA
---

If your cluster uses a private certificate authority, you need a copy of that CA certificate configured into your `~/.kube/config` on the client, so that you can trust the connection and be confident it was not intercepted.

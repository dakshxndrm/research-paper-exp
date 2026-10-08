---
type: Procedure
title: Configuring Client Certificate Trust
description: How to configure client certificate trust for the Kubernetes API server.
resource: source://security__controlling-access.md
tags:
- security
- tls
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- client certificate trust
- API server certificate
---

If your cluster uses a private certificate authority, you need a copy of that CA certificate configured into your `~/.kube/config` on the client, so that you can trust the connection and be confident it was not intercepted.

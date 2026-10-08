---
type: Definition
title: Authentication Module
description: A module responsible for authenticating requests to the Kubernetes API
  server.
resource: source://security__controlling-access.md
tags:
- security
- api access control
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- authenticator
- authentication step
---

The cluster creation script or cluster admin configures the [API server](/policy/api_server_behavior_in_kubernetes.md) to run one or more Authenticator modules.

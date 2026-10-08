---
type: Lifecycle Phase
title: Deploy Lifecycle Phase
description: Enforces restrictions on deployment authorization and location, using
  namespace isolation and image verification.
resource: source://security__cloud-native-security.md
tags:
- security
- lifecycle
- deployment
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- deploy phase
- deployment lifecycle
- application deployment security
---

The Deploy lifecycle phase ensures appropriate restrictions on what can be deployed, who can deploy it, and where it can be deployed. Measures from the [distribute phase](/lifecycle_phase/distribute_lifecycle_phase.md) such as verifying the cryptographic identity of container image artifacts can be enforced. Applications and [cluster components](/definition/kubernetes_cluster_architecture_overview.md) can be deployed into different namespaces, which provide isolation mechanisms relevant to information security. Kubernetes cluster infrastructure must provide the security guarantees that higher layers expect.

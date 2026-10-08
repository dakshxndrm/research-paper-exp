---
type: Procedure
title: Switch Services between Single-Stack and Dual-Stack
description: Procedure to switch services between single-stack and dual-stack for
  Kubernetes clusters.
resource: source://services-networking__dual-stack.md
tags:
- kubernetes
- networking
- service
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- switch service
- dual-stack service switching
---

[Services](/procedure/configuring_load_balancing_and_services.md) can be changed from single-stack to [dual-stack](/classification/kubernetes_cluster_networking_types.md) and from dual-stack to single-stack. Change the `.spec.ipFamilyPolicy` field from `SingleStack` to `PreferDualStack` or `RequireDualStack`.

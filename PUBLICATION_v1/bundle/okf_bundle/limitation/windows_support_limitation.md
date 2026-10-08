---
type: Limitation
title: Windows Support Limitation
description: Windows support limitation for dual-stack networking.
resource: source://services-networking__dual-stack.md
tags:
- kubernetes
- networking
- windows
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- windows support
- dual-stack
---

[Kubernetes](/policy/garbage_collection_in_kubernetes.md) on Windows does not support single-stack "IPv6-only" networking. However, [dual-stack](/classification/kubernetes_cluster_networking_types.md) [IPv4/IPv6](/policy/dual_stack_networking_policy.md) networking for pods and [nodes](/definition/kubernetes_cluster_architecture.md) with single-family [services](/procedure/configuring_load_balancing_and_services.md) is supported.

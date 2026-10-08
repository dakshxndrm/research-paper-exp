---
type: Concept
title: Node Configuration
description: A description of node configuration.
resource: source://containers__runtime-class.md
tags:
- kubernetes
- nodes
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- node setup
- cluster configuration
---

[RuntimeClass](/entity/runtimeclass.md) assumes a homogeneous [node configuration](/procedure/configure_node_selector_and_tolerations.md) across the cluster by default (which means that all [nodes](/definition/kubernetes_cluster_architecture.md) are configured the same way with respect to container runtimes).

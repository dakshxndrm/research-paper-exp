---
type: Policy
title: Built-in Priority Classes
description: Two built-in PriorityClasses provided by Kubernetes.
resource: source://workloads__pods__advanced-pod-config.md
tags:
- kubernetes
- pods
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- system-cluster-critical
- system-node-critical
---

[Kubernetes](/policy/garbage_collection_in_kubernetes.md) provides two built-in PriorityClasses: `system-cluster-critical` and `system-[node](/entity/node.md)-critical`. These classes have the highest priority values.

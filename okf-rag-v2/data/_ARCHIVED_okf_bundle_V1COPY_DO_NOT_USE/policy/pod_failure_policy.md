---
type: Policy
title: Pod Failure Policy
description: Kubernetes treats critical node failures as final.
resource: source://workloads.md
tags:
- kubernetes
- failure
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- node failure policy
- pod recovery
---

Once a pod is running in your cluster, a critical fault on the [node](/entity/node.md) where that pod is running means that all the [pods](/definition/kubernetes_cluster_architecture.md) on that [node](/entity/worker_node.md) fail. [Kubernetes](/policy/garbage_collection_in_kubernetes.md) treats that level of failure as final: you would need to create a new Pod to recover.

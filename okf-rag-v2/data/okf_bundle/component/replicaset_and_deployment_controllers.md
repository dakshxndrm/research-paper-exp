---
type: Component
title: ReplicaSet and Deployment Controllers
description: ReplicaSet, Deployment, StatefulSet, and DaemonSet controllers maintain
  the desired number of Pod replicas by creating replacement Pods when failures occur.
resource: source://architecture__self-healing.md
tags:
- kubernetes
- component
- controller
- replica
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- ReplicaSet
- Deployment controller
- StatefulSet
- DaemonSet
- replica controller
---

- **[Replica replacement](/definition/pod_replica_replacement.md):** If a Pod in a [Deployment](/definition/workload_resources.md) or StatefulSet fails, Kubernetes creates a replacement Pod to maintain the specified number of replicas. If a Pod that is part of a DaemonSet fails, the [control plane](/definition/control_plane_components.md) creates a replacement Pod to run on the same node.

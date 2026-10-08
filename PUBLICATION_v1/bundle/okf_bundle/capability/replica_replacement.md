---
type: Capability
title: Replica Replacement
description: Details how Kubernetes replaces failed Pods to maintain the desired number
  of replicas for Deployments, StatefulSets, and DaemonSets.
resource: source://architecture__self-healing.md
tags:
- pod
- deployment
- statefulset
- daemonset
- replica
- self-healing
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- Pod replacement
- Deployment replica replacement
- StatefulSet replica replacement
- DaemonSet replica replacement
---

If a Pod in a [Deployment](/entity/deployment.md) or [StatefulSet](/entity/statefulset.md) fails, [Kubernetes](/policy/garbage_collection_in_kubernetes.md) creates a replacement Pod to maintain the specified number of replicas.
If a Pod that is part of a [DaemonSet](/entity/daemonset.md) fails, the [control plane](/definition/kubernetes_cluster_architecture.md) creates a replacement Pod to run on the same [node](/entity/node.md).

---
type: Definition
title: Pod Replica Replacement
description: Kubernetes creates replacement Pods to maintain the specified replica
  count when Pods fail in Deployments, StatefulSets, or DaemonSets.
resource: source://architecture__self-healing.md
tags:
- kubernetes
- definition
- replica
- replacement
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- replica replacement
- Pod replacement
- replica maintenance
---

- **Replica replacement:** If a Pod in a [Deployment](/definition/workload_resources.md) or [StatefulSet](/component/replicaset_and_deployment_controllers.md) fails, Kubernetes creates a replacement Pod to maintain the specified number of replicas. If a Pod that is part of a DaemonSet fails, the [control plane](/definition/control_plane_components.md) creates a replacement Pod to run on the same node.

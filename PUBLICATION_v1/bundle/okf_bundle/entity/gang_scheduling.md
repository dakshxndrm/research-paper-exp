---
type: Entity
title: Gang Scheduling
description: Gang scheduling mechanism in Kubernetes.
resource: source://scheduling-eviction__workload-aware-preemption.md
tags:
- kubernetes
- configuration
- preemption
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- scheduling
---

The [gang scheduling](/procedure/gang_scheduling.md) mechanism is used exclusively during [PodGroup scheduling](/process/podgroup_scheduling_process.md) and replaces the default [preemption](/procedure/preemption.md) mechanism for [pods](/definition/kubernetes_cluster_architecture.md) from a given [PodGroup](/definition/podgroup.md).

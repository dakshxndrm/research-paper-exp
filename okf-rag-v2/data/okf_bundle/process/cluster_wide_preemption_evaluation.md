---
type: Process
title: Cluster-wide preemption evaluation
description: The scheduler evaluates the entire cluster as a single domain to select
  a set of victims across multiple nodes that can be removed to make enough room for
  the preemptor PodGroup to be scheduled.
resource: source://scheduling-eviction__workload-aware-preemption.md
tags:
- preemption
- cluster
- scheduling
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- cluster-wide domain
- preemption evaluation
- victim selection
---

The [workload-aware preemption](/feature/workload_aware_preemption_mechanism.md) process follows the same principles as [default preemption](/defaultbehavior/default_pod_preemption_for_single_pods.md) with a few differences. 1. Cluster-wide domain: Instead of evaluating [preemption](/definition/podgroup_preemption_and_disruption.md) node by node, the [scheduler](/definition/kube_scheduler.md) evaluates the entire cluster as a single domain. It selects a set of victims across multiple nodes that can be removed to make enough room for the preemptor [PodGroup](/entity/podgroup.md) to be scheduled.

---
type: Procedure
title: Topology-Aware Scheduling with Basic Scheduling Policy
description: May exhibit inconsistent behavior due to limited visibility of pods.
resource: source://workloads__workload-api__topology-aware-scheduling.md
tags:
- scheduling-policy
- topology-aware-scheduling
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- basic scheduling policy
- placement-based scheduling
---

Using TAS with `basic` [scheduling policy](/concept/workload_placement.md) may exhibit inconsistent behavior. The scheduler may only observe a subset of [pods](/definition/kubernetes_cluster_architecture.md) when entering the [PodGroup scheduling cycle](/policy/podgroup_scheduling_cycle.md) - therefore placement feasibility is only evaluated for the observed pods, rather than the entire [PodGroup](/definition/podgroup.md).

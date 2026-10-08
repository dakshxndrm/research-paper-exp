---
type: Procedure
title: Topology-Aware Scheduling with Gang Scheduling Policy
description: Simulates the potential assignment of pods at once to guarantee placement
  within a topology domain.
resource: source://workloads__workload-api__topology-aware-scheduling.md
tags:
- scheduling-policy
- topology-aware-scheduling
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- gang scheduling policy
- placement-based scheduling
---

When applied to PodGroups with `gang` [scheduling policy](/concept/workload_placement.md), TAS simulates the potential assignment of the full [group of pods](/definition/podgroup.md) at once. It guarantees that at least the specified `[minCount](/metric/mincount.md)` [pods](/definition/kubernetes_cluster_architecture.md) can fit together into the same [topology domain](/entity/topology_domain.md) before committing resources.

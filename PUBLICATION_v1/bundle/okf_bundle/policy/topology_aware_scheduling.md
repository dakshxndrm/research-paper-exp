---
type: Policy
title: Topology-Aware Scheduling
description: A feature of the Workload API that optimizes pod placement within a cluster.
resource: source://workloads__workload-api__topology-aware-scheduling.md
tags:
- workload-api
- scheduling
timestamp: '2026-07-27T19:53:46+00:00'
---

Topology-Aware [Scheduling](/concept/scheduling.md) (TAS) is a feature of the [Workload API](/entity/workload_api.md) that optimizes the placement of [pods](/definition/kubernetes_cluster_architecture.md) within the cluster. It ensures that all pods within a [PodGroup](/definition/podgroup.md) are co-located into a specific [topology domain](/entity/topology_domain.md), such as a single server rack or zone.

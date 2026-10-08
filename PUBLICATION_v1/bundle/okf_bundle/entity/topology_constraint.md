---
type: Entity
title: Topology Constraint
description: A constraint that enforces pod placement within a specific topology domain.
resource: source://workloads__workload-api__topology-aware-scheduling.md
tags:
- workload-api
- scheduling
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- placement constraint
---

A topology constraint is a constraint that enforces [pod placement](/concept/scheduling.md) within a specific [topology domain](/entity/topology_domain.md). It corresponds to a [Kubernetes](/policy/garbage_collection_in_kubernetes.md) [node](/entity/node.md) label, representing the target topology [domain](/metric/cluster_wide_domain.md).

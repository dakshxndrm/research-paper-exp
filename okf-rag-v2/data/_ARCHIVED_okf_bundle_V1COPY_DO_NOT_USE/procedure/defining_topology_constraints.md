---
type: Procedure
title: Defining Topology Constraints
description: Sets a key corresponding to a Kubernetes node label.
resource: source://workloads__workload-api__topology-aware-scheduling.md
tags:
- workload-api
- scheduling
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- defining topology constraint
- setting placement constraint
---

To define a [topology constraint](/entity/topology_constraint.md) for a [PodGroup](/definition/podgroup.md), you need to set a `key`, which corresponds to a [Kubernetes](/policy/garbage_collection_in_kubernetes.md) [node](/entity/node.md) label, representing the target [topology domain](/entity/topology_domain.md).

---
type: Plugin
title: GangScheduling Plugin
description: The GangScheduling plugin alters the lifecycle for Pods belonging to
  a PodGroup with a gang scheduling policy.
resource: source://scheduling-eviction__gang-scheduling.md
tags:
- kubernetes
- plugin
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- gang scheduling plugin
- plugin
---

When the `GangScheduling` plugin is enabled, the scheduler alters the [lifecycle](/policy/podgroup_ownership_and_lifecycle.md) for [Pods](/definition/kubernetes_cluster_architecture.md) belonging to a [PodGroup](/definition/podgroup.md) that has a `gang` [scheduling policy](/concept/workload_placement.md).

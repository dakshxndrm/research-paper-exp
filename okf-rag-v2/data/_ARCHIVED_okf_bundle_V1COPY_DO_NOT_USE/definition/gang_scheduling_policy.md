---
type: Definition
title: Gang Scheduling Policy
description: A scheduling policy that groups Pods together for parallel execution.
resource: source://workloads__workload-api.md
tags:
- kubernetes
- scheduling policy
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- gang policy
- parallel execution
---

The [gang policy](/policy_type/gang_policy.md)'s `[minCount](/metric/mincount.md)` is set to the [Job](/entity/job.md)'s parallelism, so all Pods must be schedulable together before any of them are bound to [nodes](/definition/kubernetes_cluster_architecture.md).

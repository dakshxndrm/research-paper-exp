---
type: Procedure
title: Basic Scheduling Policy with TAS
description: Using TAS with basic scheduling policy may observe only a subset of pods
  during the scheduling cycle, evaluating placement feasibility only for observed
  pods rather than the entire PodGroup; scheduling gates can mitigate this limitation
  by holding off PodGroup scheduling until all pods are in the queue.
resource: source://workloads__workload-api__topology-aware-scheduling.md
tags:
- scheduling
- basic
- policy
- topology
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- basic scheduling
- scheduling gates
- pod placement
- PodGroup scheduling cycle
---

Using TAS with `basic` [scheduling policy](/definition/podgroup_scheduling_policy.md) may exhibit inconsistent behavior. The [scheduler](/definition/kube_scheduler.md) may only observe a subset of pods when entering the [PodGroup scheduling cycle](/procedure/podgroup_scheduling_cycle.md) - therefore [placement feasibility](/procedure/gang_scheduling_policy_with_tas.md) is only evaluated for the observed pods, rather than the entire [PodGroup](/entity/podgroup.md). To partially mitigate this limitation, you can use [scheduling](/scheduling/runtimeclass_scheduling_constraints.md) gates to hold off [PodGroup scheduling](/concept/podgroup_lifecycle_and_controller_relationship.md) until all pods within the PodGroup are in the scheduling queue. If no feasible placement is found for the entire PodGroup, only a subset of pods may be scheduled, and they are guaranteed to meet the [scheduling constraints](/definition/gang_scheduling_constraints.md). If new pods are added to the PodGroup where some pods are already scheduled, the scheduler will act the same as in case of `gang` policy - forcing the new pods into the same domain, unless there is insufficient capacity (in which case the new pods will remain pending).

---
type: Policy
title: PodGroup Scheduling Policy Types
description: 'Defines the two scheduling policy types available for PodGroups: basic
  and gang, where basic evaluates Pods on a best-effort basis and gang enforces all-or-nothing
  scheduling.'
resource: source://workloads__workload-api__policies.md
tags:
- scheduling
- policy
- workload
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- scheduling policy
- PodGroup policy
- basic policy
- gang policy
---

Every [PodGroup](/entity/podgroup.md) must declare a [scheduling](/scheduling/runtimeclass_scheduling_constraints.md) policy in its `[spec.schedulingPolicy](/definition/podgroup_scheduling_policy.md)` field, which dictates how the [scheduler](/definition/kube_scheduler.md) treats the collection of Pods in the group. The `schedulingPolicy` field supports two [policy types](/definition/podgroup_basic_vs_gang_scheduling_policy.md): `basic` and `gang`, and exactly one must be specified. The `basic` policy instructs the scheduler to evaluate all Pods on a best-effort basis, considering the group feasible regardless of how many Pods are currently schedulable. This policy is suited for organizing Pods into a group for better observability and management, or for groups that do not require simultaneous startup but logically belong together. The `gang` policy enforces "all-or-nothing" scheduling, which is essential for tightly-coupled workloads where partial startup results in deadlocks or wasted resources, such as Jobs or batch processes where all workers must run concurrently to make progress. The `gang` policy requires a `[minCount](/definition/gang_scheduling_constraints.md)` field specifying the minimum number of Pods that must be schedulable simultaneously for the group to be feasible.

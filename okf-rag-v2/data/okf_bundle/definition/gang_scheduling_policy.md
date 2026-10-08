---
type: Definition
title: Gang Scheduling Policy
description: Defines the gang scheduling policy requiring minimum Pod count for all-or-nothing
  placement.
resource: source://workloads__workload-api__policies.md
tags:
- scheduling
- policy
- gang
- mincount
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- gang policy
- all-or-nothing scheduling
- minCount policy
---

The `gang` policy enforces "all-or-nothing" [scheduling](/scheduling/runtimeclass_scheduling_constraints.md), which is essential for tightly-coupled workloads where partial startup results in deadlocks or wasted resources. This can be used for Jobs or any other batch process where all workers must run concurrently to make progress. The `gang` policy requires a `[minCount](/definition/gang_scheduling_constraints.md)` field, which is the minimum number of Pods that must be schedulable simultaneously for the group to be feasible.

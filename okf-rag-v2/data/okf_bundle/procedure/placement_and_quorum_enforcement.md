---
type: Procedure
title: Placement and Quorum Enforcement
description: If minCount Pods are placed successfully, they are bound to nodes; otherwise
  all Pods go to the unschedulable queue.
resource: source://scheduling-eviction__gang-scheduling.md
tags:
- procedure
- quorum
- placement
timestamp: '2026-09-02T17:04:11+00:00'
---

If the [scheduler](/definition/kube_scheduler.md) finds valid placements for at least the [minCount](/definition/gang_scheduling_constraints.md) number of Pods, it allows those successfully placed Pods to be bound to their assigned nodes. If it cannot find enough placements to satisfy the minCount requirement, none of the Pods are scheduled. Instead, they are moved to the unschedulable queue to wait for cluster resources to free up, allowing other workloads to be scheduled in the meantime.

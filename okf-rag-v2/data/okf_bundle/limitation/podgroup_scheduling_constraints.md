---
type: Limitation
title: PodGroup scheduling constraints
description: All Pods in a PodGroup must use the same scheduler name; mismatch causes
  all Pods to be rejected as unschedulable. The schedulingPolicy.gang.minCount field
  is immutable once created.
resource: source://workloads__podgroup-api__lifecycle.md
tags:
- podgroup
- scheduling
- limitation
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- scheduling constraints
- scheduler name
- minCount immutable
---

All Pods in a [PodGroup](/entity/podgroup.md) must use the same .spec.schedulerName. If a mismatch is detected, the [scheduler](/definition/kube_scheduler.md) rejects all Pods in the group as unschedulable. The [spec.schedulingPolicy](/definition/podgroup_scheduling_policy.md).gang.[minCount](/definition/gang_scheduling_constraints.md) field on a PodGroup is immutable. Once created, you cannot change the minimum number of Pods that must be schedulable for the group to be admitted.

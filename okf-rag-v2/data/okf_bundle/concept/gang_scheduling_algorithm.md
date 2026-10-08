---
type: Concept
title: Gang scheduling algorithm
description: PodGroups enforce gang scheduling where all Pods must be schedulable
  together; the PodGroupScheduled condition captures the initial scheduling result
  only.
resource: source://workloads__podgroup-api__lifecycle.md
tags:
- podgroup
- gang scheduling
- algorithm
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- gang scheduling
- scheduling algorithm
- PodGroup scheduling
---

PodGroups enforce [gang scheduling](/definition/workload_placement_and_podgrouptemplates.md) where all Pods must be schedulable together. The [PodGroupScheduled condition](/limitation/podgroupscheduled_condition_stability.md) reflects the outcome of the initial [scheduling](/scheduling/runtimeclass_scheduling_constraints.md) attempt only. Once set to True, the [scheduler](/definition/kube_scheduler.md) does not [update](/operations/kubectl_resource_management_operations.md) it if Pods later fail, are evicted, or stop running.

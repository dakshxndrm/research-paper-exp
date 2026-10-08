---
type: Definition
title: PodGroup scheduling status conditions
description: The scheduler updates status.conditions to report scheduling success,
  primarily using the PodGroupScheduled condition which is True when all required
  Pods have been placed and False when scheduling fails.
resource: source://workloads__podgroup-api.md
tags:
- kubernetes
- scheduling status
- conditions
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- status.conditions
- PodGroupScheduled
- scheduling conditions
- scheduling status
---

The [scheduler](/definition/kube_scheduler.md) updates status.conditions to report whether the group has been successfully scheduled. The primary condition is PodGroupScheduled, which is True when all required Pods have been placed and False when [scheduling](/scheduling/runtimeclass_scheduling_constraints.md) fails. The [PodGroupScheduled condition](/limitation/podgroupscheduled_condition_stability.md) reflects the initial [scheduling decision](/definition/binding_process.md) only; the scheduler does not [update](/operations/kubectl_resource_management_operations.md) it if Pods later fail or are evicted.

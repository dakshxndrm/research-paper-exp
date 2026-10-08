---
type: Limitation
title: PodGroupScheduled condition stability
description: The PodGroupScheduled condition reflects only the initial scheduling
  attempt outcome; the scheduler does not update it if Pods later fail, are evicted,
  or stop running.
resource: source://workloads__podgroup-api__lifecycle.md
tags:
- podgroup
- limitation
- scheduling condition
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- PodGroupScheduled condition
- scheduling condition
- initial scheduling
---

The [PodGroupScheduled](/definition/podgroup_scheduling_status_conditions.md) condition reflects the outcome of the initial [scheduling](/scheduling/runtimeclass_scheduling_constraints.md) attempt only. Once the condition is set to True, the [scheduler](/definition/kube_scheduler.md) does not [update](/operations/kubectl_resource_management_operations.md) it if Pods later fail, are evicted, or stop running.

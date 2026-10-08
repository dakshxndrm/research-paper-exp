---
type: Procedure
title: Understanding How to Use PodGroups with Custom Controllers
description: A step-by-step guide to understanding how to use podgroups with custom
  controllers.
resource: source://workloads__podgroup-api.md
tags:
- kubernetes
- custom-controller-podgroup-usage
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- custom controller usage
- podgroup usage
---

[Custom controllers](/deployment/running_kubernetes_controllers.md) can implement the same flow for their own [workload](/entity/workload.md) types. They need to create a Workload that defines [PodGroupTemplates](/template/podgrouptemplates.md) with [scheduling policies](/policy/scheduling_policies_in_kube_scheduler.md) and then create a [PodGroup](/definition/podgroup.md) from one of the Workload's PodGroupTemplates.

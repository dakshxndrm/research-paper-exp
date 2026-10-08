---
type: Template
title: PodGroupTemplates
description: Define scheduling policies inside `PodGroupTemplates`.
resource: source://workloads__workload-api__policies.md
tags:
- kubernetes
- workloads
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- pod group templates
- workload api
---

When using the [Workload API](/entity/workload_api.md), you define [scheduling policies](/policy/scheduling_policies_in_kube_scheduler.md) inside `PodGroupTemplates`. The [workload](/entity/workload.md) [controller](/pattern/kubernetes_controller_pattern.md) copies the policy from the [template](/entity/podgrouptemplate.md) into each [PodGroup](/definition/podgroup.md) it creates, making the PodGroup self-contained.

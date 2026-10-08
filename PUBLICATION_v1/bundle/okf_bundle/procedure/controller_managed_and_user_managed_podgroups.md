---
type: Procedure
title: Controller-Managed and User-Managed PodGroups
description: How workload controllers create and manage PodGroups.
resource: source://workloads__podgroup-api__lifecycle.md
tags:
- workload
- controller
- podgroup
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- controller-managed
- user-managed
---

In most cases, [workload](/entity/workload.md) [controllers](/pattern/kubernetes_controller_pattern.md) (for example, [Job](/entity/job.md)) create `PodGroups` automatically (controller-managed). The controller determines the `podGroupName` for each Pod at creation time.

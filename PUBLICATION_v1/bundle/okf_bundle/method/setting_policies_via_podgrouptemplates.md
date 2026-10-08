---
type: Method
title: Setting Policies via PodGroupTemplates
description: Set scheduling policies for newly created PodGroups.
resource: source://workloads__workload-api__policies.md
tags:
- kubernetes
- workloads
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- setting policies
- workload api
---

For newly created PodGroups, you set `spec.schedulingPolicy` directly on the [PodGroup](/definition/podgroup.md) itself. Changes to the [Workload](/entity/workload.md)'s templates only affect newly created PodGroups, not existing ones.

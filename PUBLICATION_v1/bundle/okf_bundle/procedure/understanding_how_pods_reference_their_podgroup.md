---
type: Procedure
title: Understanding How Pods Reference Their PodGroup
description: A step-by-step guide to understanding how pods reference their podgroup.
resource: source://workloads__podgroup-api.md
tags:
- kubernetes
- pod-reference-podgroup
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- pod referencing
- scheduling group field
---

[Pods](/definition/kubernetes_cluster_architecture.md) reference their [PodGroup](/definition/podgroup.md) via the `spec.schedulingGroup.podGroupName` field. This allows the scheduler to schedule Pods based on the [scheduling policy](/concept/workload_placement.md) defined in the PodGroup.

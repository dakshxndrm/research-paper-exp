---
type: Concept
title: Scheduling
description: A description of scheduling.
resource: source://containers__runtime-class.md
tags:
- kubernetes
- scheduling
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- pod placement
- node selection
---

By specifying the `[scheduling](/policy/kubernetes_scheduling_overview.md)` field for a [RuntimeClass](/entity/runtimeclass.md), you can set constraints to ensure that Pods running with this RuntimeClass are scheduled to [nodes](/definition/kubernetes_cluster_architecture.md) that support it.

---
type: Feature
title: Gang Scheduling Overview
description: A feature that schedules a group of Pods on an all-or-nothing basis.
resource: source://scheduling-eviction__gang-scheduling.md
tags:
- kubernetes
- scheduling
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- gang scheduling
- all-or-nothing scheduling
---

[Gang scheduling](/procedure/gang_scheduling.md) ensures that a [group of Pods](/definition/podgroup.md) are scheduled on an 'all-or-nothing' basis. If the cluster cannot accommodate the entire group (or a defined minimum number of [Pods](/definition/kubernetes_cluster_architecture.md)), none of the Pods are bound to a [node](/entity/node.md).

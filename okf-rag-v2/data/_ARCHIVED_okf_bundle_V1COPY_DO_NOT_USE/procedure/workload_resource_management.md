---
type: Procedure
title: Workload Resource Management
description: Use workload resources to manage a set of pods.
resource: source://workloads.md
tags:
- kubernetes
- workload
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- workload management
- pod management
---

You can use [workload](/entity/workload.md) resources that manage a set of [pods](/definition/kubernetes_cluster_architecture.md) on your behalf. These resources configure [controllers](/pattern/kubernetes_controller_pattern.md) that make sure the right number of the right kind of pod are running, to match the state you specified.

---
type: Limitation
title: Immutable Minimum Pod Count for Gang Scheduling
description: Minimum number of Pods that must be schedulable for gang scheduling.
resource: source://workloads__podgroup-api__lifecycle.md
tags:
- podgroup
- scheduler
- gang
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- minimum count
- gang scheduling
---

The `spec.schedulingPolicy.gang.[minCount](/metric/mincount.md)` field on a [PodGroup](/definition/podgroup.md) is immutable. Once created, you cannot change the minimum number of [Pods](/definition/kubernetes_cluster_architecture.md) that must be schedulable for the group to be admitted.

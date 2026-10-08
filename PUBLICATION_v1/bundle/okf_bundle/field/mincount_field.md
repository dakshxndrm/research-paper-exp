---
type: Field
title: minCount Field
description: The minimum number of Pods that must be schedulable simultaneously for
  the group to be feasible.
resource: source://workloads__workload-api__policies.md
tags:
- kubernetes
- workloads
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- minimum pod count
- gang policy requirement
---

The `gang` policy requires a `[minCount](/metric/mincount.md)` field, which is the minimum number of [Pods](/definition/kubernetes_cluster_architecture.md) that must be schedulable simultaneously for the group to be feasible:

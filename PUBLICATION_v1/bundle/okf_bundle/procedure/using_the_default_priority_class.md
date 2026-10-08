---
type: Procedure
title: Using the Default Priority Class
description: How to use a default PriorityClass.
resource: source://workloads__workload-api__disruption-and-priority.md
tags:
- kubernetes
- workload-api
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- using default priority class
- default priority class
---

When `priorityClassName` is not set for a [PodGroup](/definition/podgroup.md), [Kubernetes](/policy/garbage_collection_in_kubernetes.md) looks for a default (a [PriorityClass](/entity/priorityclass.md) with `globalDefault` set true)

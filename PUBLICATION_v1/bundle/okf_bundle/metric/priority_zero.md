---
type: Metric
title: Priority Zero
description: The default priority value.
resource: source://workloads__workload-api__disruption-and-priority.md
tags:
- kubernetes
- workload-api
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- zero priority
---

If there is no [PriorityClass](/entity/priorityclass.md) with `globalDefault` set true, a [PodGroup](/definition/podgroup.md) with no `priorityClassName` has priority zero.

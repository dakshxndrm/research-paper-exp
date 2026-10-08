---
type: Procedure
title: Setting Priority for a Pod Group
description: How to set the priority for a PodGroup.
resource: source://workloads__workload-api__disruption-and-priority.md
tags:
- kubernetes
- workload-api
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- setting pod group priority
- pod group priority
---

Once you have created one or more PriorityClasses, you can create a [PodGroup](/definition/podgroup.md) that specifies one of those [PriorityClass](/entity/priorityclass.md) names in its specification.

---
type: Rule
title: Referencing Non-Existent PodGroups
description: Behavior when a Pod references a non-existent PodGroup.
resource: source://workloads__podgroup-api__lifecycle.md
tags:
- podgroup
- pod
- scheduler
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- referencing
- non-existent
---

If a `Pod` references a `[PodGroup](/definition/podgroup.md)` that does not yet exist, the `Pod` remains pending. The scheduler automatically queues the `Pod` for [scheduling](/concept/scheduling.md) once the `PodGroup` is created.

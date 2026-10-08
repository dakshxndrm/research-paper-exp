---
type: Procedure
title: Snapshotting Cluster State
description: The process of taking a single snapshot of the cluster state for the
  duration of the scheduling cycle.
resource: source://scheduling-eviction__podgroup-scheduling.md
tags:
- kubernetes
- scheduling
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- cluster state snapshot
- snapshot
---

When the scheduler begins evaluating a [PodGroup](/definition/podgroup.md), it takes a single snapshot of the cluster state that lasts for the entire duration of the cycle. This ensures the evaluation remains consistent for the whole group and prevents race conditions with other events.

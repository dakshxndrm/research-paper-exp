---
type: Entity
title: PodGroup Conditions
description: Conditions that are updated on the PodGroup's `status.conditions` after
  a scheduling cycle completes.
resource: source://scheduling-eviction__podgroup-scheduling.md
tags:
- kubernetes
- scheduling
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- scheduling conditions
---

After a [PodGroup scheduling cycle](/policy/podgroup_scheduling_cycle.md) completes, the scheduler updates conditions on the [PodGroup](/definition/podgroup.md)'s `status.conditions`: `PodGroupScheduled` and `DisruptionTarget`.

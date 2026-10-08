---
type: Limitation
title: Immutable Scheduling Group Field on Pods
description: Once set, a Pod cannot move to a different PodGroup.
resource: source://workloads__podgroup-api__lifecycle.md
tags:
- podgroup
- pod
- scheduler
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- scheduling group
- immutable field
---

The `spec.schedulingGroup` field on a Pod is immutable. Once set, a Pod cannot move to a different [PodGroup](/definition/podgroup.md).

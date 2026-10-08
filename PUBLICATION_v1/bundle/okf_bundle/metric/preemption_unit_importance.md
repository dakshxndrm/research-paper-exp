---
type: Metric
title: Preemption Unit Importance
description: Importance of preemption units in Kubernetes.
resource: source://scheduling-eviction__workload-aware-preemption.md
tags:
- kubernetes
- preemption
- priority
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- victim importance
---

The scheduler evaluates the importance of [preemption](/procedure/preemption.md) units based on their priority, [workload](/entity/workload.md) type, group size, and start time.

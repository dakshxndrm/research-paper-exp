---
type: Entity
title: PodGroup
description: Defines the PodGroup resource that declares scheduling policies in its
  spec field.
resource: source://workloads__workload-api__policies.md
tags:
- entity
- podgroup
- scheduling
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- PodGroup resource
- standalone PodGroup
---

Every PodGroup must declare a [scheduling](/scheduling/runtimeclass_scheduling_constraints.md) policy in its `[spec.schedulingPolicy](/definition/podgroup_scheduling_policy.md)` field. For standalone PodGroups (created without a Workload), you set `spec.schedulingPolicy` directly on the PodGroup itself.

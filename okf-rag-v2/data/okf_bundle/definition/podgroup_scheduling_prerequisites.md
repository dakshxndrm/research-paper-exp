---
type: Definition
title: PodGroup Scheduling Prerequisites
description: Required feature gates and API groups enabling PodGroup scheduling functionality.
resource: source://scheduling-eviction__podgroup-scheduling.md
tags:
- scheduling
- configuration
- requirements
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- feature gates
- API group
- scheduling prerequisites
---

[PodGroup scheduling](/concept/podgroup_lifecycle_and_controller_relationship.md) depends on the Workload API. The `GenericWorkload` feature gate and the `[scheduling](/scheduling/runtimeclass_scheduling_constraints.md).k8s.io/v1alpha1` API group must be enabled in the cluster for [PodGroup](/entity/podgroup.md) scheduling to function.

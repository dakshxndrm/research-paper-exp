---
type: Definition
title: PodGroup Scheduling Overview
description: PodGroup scheduling evaluates a group of Pods as a single unit to prevent
  resource deadlocks and ensure atomic placement decisions.
resource: source://scheduling-eviction__podgroup-scheduling.md
tags:
- scheduling
- architecture
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- PodGroup scheduling cycle
- group scheduling
- workload scheduling
---

The standard [Kubernetes scheduler](/definition/kube_scheduler.md) evaluates Pods sequentially, which can lead to resource deadlocks when multiple workloads are submitted concurrently. [PodGroup scheduling](/concept/podgroup_lifecycle_and_controller_relationship.md) addresses this by treating a group of Pods as a unified entity, attempting to find placements for all Pods simultaneously. If sufficient resources are not available for the entire group, none of the Pods are bound. This feature depends on the Workload API, requiring the `GenericWorkload` feature gate and `[scheduling](/scheduling/runtimeclass_scheduling_constraints.md).k8s.io/v1alpha1` [API group](/definition/podgroup_scheduling_prerequisites.md) to be enabled in the cluster.

---
type: Dependency
title: Required feature gates and API group
description: The feature depends on Gang Scheduling and the Workload API, requiring
  GenericWorkload and GangScheduling feature gates and the scheduling.k8s.io/v1alpha2
  API group to be enabled.
resource: source://scheduling-eviction__workload-aware-preemption.md
tags:
- dependencies
- feature gates
- api group
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- feature dependencies
- required feature gates
- API group requirements
---

This feature depends on the [Gang Scheduling](/definition/workload_placement_and_podgrouptemplates.md) and the Workload API. Ensure the GenericWorkload and GangScheduling [feature gates](/definition/podgroup_scheduling_prerequisites.md) and the [scheduling.k8s.io/v1alpha2 API](/definition/workload_api_resource.md) group are enabled in the cluster.

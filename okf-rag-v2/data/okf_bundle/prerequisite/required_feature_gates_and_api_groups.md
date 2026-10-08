---
type: Prerequisite
title: Required Feature Gates and API Groups
description: The GenericWorkload feature gate and scheduling.k8s.io/v1alpha2 API group
  must be enabled for gang scheduling to function.
resource: source://scheduling-eviction__gang-scheduling.md
tags:
- configuration
- prerequisite
timestamp: '2026-09-02T17:04:11+00:00'
---

This feature depends on the [PodGroup API](/reference/podgroup_api_and_runtime_policy_carriage.md). Ensure the [GenericWorkload feature gate](/definition/podgroup_api_group_and_feature_gate.md) and the [scheduling.k8s.io/v1alpha2 API](/definition/workload_api_resource.md) group are enabled in the cluster.

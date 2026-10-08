---
type: Definition
title: Gang Scheduling Overview
description: Gang scheduling ensures a group of Pods are scheduled on an all-or-nothing
  basis, binding none if the cluster cannot accommodate the entire group or a defined
  minimum number.
resource: source://scheduling-eviction__gang-scheduling.md
tags:
- scheduling
- kubernetes
timestamp: '2026-09-02T17:04:11+00:00'
---

[Gang scheduling](/definition/workload_placement_and_podgrouptemplates.md) ensures that a group of Pods are scheduled on an "all-or-nothing" basis. If the cluster cannot accommodate the entire group (or a defined minimum number of Pods), none of the Pods are bound to a node. This feature depends on the [PodGroup API](/reference/podgroup_api_and_runtime_policy_carriage.md). Ensure the [GenericWorkload feature gate](/definition/podgroup_api_group_and_feature_gate.md) and the [scheduling.k8s.io/v1alpha2 API](/definition/workload_api_resource.md) group are enabled in the cluster.

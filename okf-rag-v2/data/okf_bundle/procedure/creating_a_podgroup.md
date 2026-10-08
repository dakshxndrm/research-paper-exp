---
type: Procedure
title: Creating a PodGroup
description: The process for creating a PodGroup API resource, requiring the scheduling.k8s.io/v1alpha2
  API group and GenericWorkload feature gate enabled.
resource: source://workloads__podgroup-api.md
tags:
- kubernetes
- procedure
- creation
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- PodGroup creation
- create PodGroup
- API resource creation
---

A [PodGroup API resource](/definition/podgroup_api_resource.md) is part of the [scheduling.k8s.io/v1alpha2 API](/definition/workload_api_resource.md) group. (and your cluster must have that [API group enabled](/definition/workload_api_requirements.md), as well as the [GenericWorkload feature gate](/definition/podgroup_api_group_and_feature_gate.md), before you can use this API). The following manifest creates a [PodGroup](/entity/podgroup.md) with a [gang scheduling policy](/definition/gang_scheduling_policy.md) that requires at least 4 Pods to be schedulable simultaneously: You can inspect PodGroups in your cluster: To see the full status including [scheduling conditions](/definition/podgroup_scheduling_status_conditions.md):

---
type: Definition
title: Workload API requirements
description: The cluster must have the scheduling.k8s.io/v1alpha2 API group enabled
  and the GenericWorkload feature gate activated before using the Workload API.
resource: source://workloads__workload-api.md
tags:
- api requirements
- cluster configuration
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- scheduling.k8s.io/v1alpha2
- API group enabled
- GenericWorkload gate
---

# Workload API requirements

The `Workload` API resource is part of the `[scheduling.k8s.io/v1alpha2](/definition/podgroup_api_group_and_feature_gate.md)` [API group](/definition/podgroup_scheduling_prerequisites.md) and your cluster must have that API group enabled, as well as the `GenericWorkload` feature gate, before you can use this API.

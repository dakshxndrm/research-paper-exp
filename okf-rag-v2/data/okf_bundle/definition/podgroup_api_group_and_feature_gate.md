---
type: Definition
title: PodGroup API group and feature gate
description: The PodGroup API resource is part of the scheduling.k8s.io/v1alpha2 API
  group and requires the GenericWorkload feature gate to be enabled on the cluster
  before use.
resource: source://workloads__podgroup-api.md
tags:
- kubernetes
- api
- feature gate
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- scheduling.k8s.io/v1alpha2
- GenericWorkload feature gate
---

The [PodGroup API resource](/definition/podgroup_api_resource.md) is part of the [scheduling.k8s.io/v1alpha2 API](/definition/workload_api_resource.md) group and your cluster must have that [API group enabled](/definition/workload_api_requirements.md), as well as the GenericWorkload feature gate, before you can use this API.

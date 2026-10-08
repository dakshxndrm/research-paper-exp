---
type: Procedure
title: Enabling Workload-Aware Preemption
description: Enable workload-aware preemption in a Kubernetes cluster.
resource: source://scheduling-eviction__workload-aware-preemption.md
tags:
- kubernetes
- configuration
- preemption
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- workload-aware preemption setup
---

Ensure the `GenericWorkload` and `GangScheduling` feature gates and the `[scheduling.k8s.io/v1alpha2](/entity/api_group.md)` [API group](/definition/api_group_resource_type_namespace_and_name.md) are enabled in the cluster.

---
type: Procedure
title: Creating a Workload
description: Describes the process of creating a workload in Kubernetes.
resource: source://workloads__workload-api.md
tags:
- kubernetes
- procedure
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- workload creation
- scheduling policy
---

To create a `[Workload](/entity/workload.md)`, you must have the `[scheduling.k8s.io/v1alpha2](/entity/api_group.md)` [API group](/definition/api_group_resource_type_namespace_and_name.md) enabled and the `GenericWorkload` feature gate. The entire `Workload` spec is immutable after creation.

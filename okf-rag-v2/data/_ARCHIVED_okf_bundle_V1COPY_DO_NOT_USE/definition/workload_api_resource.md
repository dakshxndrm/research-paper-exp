---
type: Definition
title: Workload API Resource
description: Defines the scheduling requirements and structure of a multi-Pod application.
resource: source://workloads__workload-api.md
tags:
- kubernetes
- api-resource
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- Workload
- scheduling.k8s.io/v1alpha2
---

The `[Workload](/entity/workload.md)` [API resource](/entity/podgroup_api_resource.md) defines the [scheduling](/concept/scheduling.md) requirements and structure of a multi-Pod application. While workload [controllers](/pattern/kubernetes_controller_pattern.md) such as [Job](/entity/job.md) manage the application's [runtime](/entity/container_runtime_1.md) state, the `Workload` specifies how groups of `[Pods](/definition/kubernetes_cluster_architecture.md)` should be scheduled.

---
type: Definition
title: Workload API resource
description: The Workload API resource defines scheduling requirements and structure
  for multi-Pod applications in the scheduling.k8s.io/v1alpha2 API group.
resource: source://workloads__workload-api.md
tags:
- api
- scheduling
- workload
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- scheduling.k8s.io/v1alpha2 API
- GenericWorkload feature gate
---

# Workload API resource

The `Workload` API resource defines the [scheduling](/scheduling/runtimeclass_scheduling_constraints.md) requirements and structure of a multi-Pod application. While workload controllers such as Job manage the application's [runtime](/definition/container_runtime.md) state, the `Workload` specifies how groups of `Pods` should be scheduled. The [Job controller](/procedure/job_controller_workflow.md) is the only built-in controller that creates [PodGroup](/entity/podgroup.md) objects from the `Workload`'s `[PodGroupTemplates](/definition/podgrouptemplates.md)` at runtime.

The Workload API resource is part of the `[scheduling.k8s.io/v1alpha2](/definition/podgroup_api_group_and_feature_gate.md)` [API group](/definition/podgroup_scheduling_prerequisites.md) and your cluster must have that [API group enabled](/definition/workload_api_requirements.md), as well as the `GenericWorkload` feature gate, before you can use this API.

A `Workload` is a static, long-lived policy [template](/entity/podgrouptemplate.md). It defines what [scheduling policies](/configuration/scheduling_policies_configuration.md) should be applied to groups of Pods, but does not track runtime state itself. Runtime scheduling state is maintained by PodGroup objects, which controllers [create](/operations/kubectl_resource_management_operations.md) from the `Workload`'s `PodGroupTemplates`.

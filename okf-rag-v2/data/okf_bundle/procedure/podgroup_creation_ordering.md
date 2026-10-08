---
type: Procedure
title: PodGroup creation ordering
description: Controllers must create Workload, PodGroup, and Pods in sequence; PodGroup
  creation fails if the referenced Workload does not exist, and Pods referencing a
  missing PodGroup remain pending.
resource: source://workloads__podgroup-api__lifecycle.md
tags:
- podgroup
- creation
- scheduling
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- PodGroup creation
- creation ordering
- Workload PodGroup Pod
---

Controllers must [create](/operations/kubectl_resource_management_operations.md) objects in this order: Workload — the [scheduling policy template](/definition/podgrouptemplates.md); [PodGroup](/entity/podgroup.md) — the [runtime](/definition/container_runtime.md) instance; Pods — with [spec.schedulingGroup](/definition/workload_placement_and_podgrouptemplates.md).[podGroupName](/concept/pod_reference_to_podgroup.md) pointing to the PodGroup. If a PodGroup includes a podGroupTemplateRef that points to a Workload that does not exist (or is being deleted), the [API server](/definition/kube_apiserver.md) rejects the [PodGroup creation](/procedure/creating_a_podgroup.md) request. The referenced Workload must exist before the PodGroup can be created. If a Pod references a PodGroup that does not yet exist, the Pod remains pending. The [scheduler](/definition/kube_scheduler.md) automatically queues the Pod for [scheduling](/scheduling/runtimeclass_scheduling_constraints.md) once the PodGroup is created.

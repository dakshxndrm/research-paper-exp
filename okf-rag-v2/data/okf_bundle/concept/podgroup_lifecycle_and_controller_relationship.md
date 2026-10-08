---
type: Concept
title: PodGroup lifecycle and controller relationship
description: The relationship between workload controllers, Workloads, PodGroups,
  and Pods, where the workload controller creates PodGroupTemplates, the controller
  creates PodGroups from templates, and Pods reference their PodGroup via a scheduling
  group field.
resource: source://workloads__podgroup-api.md
tags:
- kubernetes
- lifecycle
- controller
- workload
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- PodGroup lifecycle
- workload controller
- PodGroup scheduling
- scheduling group field
---

The relationship between controllers, Workloads, PodGroups, and Pods follows this pattern: 1. The [workload controller](/definition/workload_controller.md) creates a Workload that defines [PodGroupTemplates](/definition/podgrouptemplates.md) with [scheduling policies](/configuration/scheduling_policies_configuration.md). 2. For each [runtime](/definition/container_runtime.md) instance, the controller creates a [PodGroup](/entity/podgroup.md) from one of the Workload's PodGroupTemplates. 3. The controller creates Pods that reference the PodGroup via the [spec.schedulingGroup](/definition/workload_placement_and_podgrouptemplates.md).[podGroupName](/concept/pod_reference_to_podgroup.md) field. The [Job controller](/procedure/job_controller_workflow.md) is the only built-in workload controller that follows this pattern for now. Custom controllers can implement the same flow for their own workload types. The Workload acts as a long-lived policy definition, while PodGroups handle the transient, per-instance runtime state. This separation means that status updates for individual PodGroups do not contend on the shared Workload object.

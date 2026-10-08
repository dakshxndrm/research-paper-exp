---
type: Definition
title: Pod Group Priority
description: PodGroup uses PriorityClass to assign an integer priority value that
  overrides individual pod priorities during workload-aware preemption events.
resource: source://workloads__workload-api__disruption-and-priority.md
tags:
- priority
- preemption
- admission
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- PodGroup priority
- priorityClassName
- PriorityClass
- high-priority
---

## Pod group priority

[PodGroup](/entity/podgroup.md) uses the same concept of PriorityClass as single Pods. Once you have created one or more [PriorityClasses](/definition/priorityclasses.md), you can [create](/operations/kubectl_resource_management_operations.md) a PodGroup that specifies one of those PriorityClass names in its specification. The priority [admission controller](/control/admission_controller_for_owner_deletion.md) uses the `priorityClassName` field and populates the integer value of the priority. If the priority class is not found, the PodGroup is rejected.

When `priorityClassName` is not set for a PodGroup, Kubernetes looks for a default (a PriorityClass with `globalDefault` set true). If there is no PriorityClass with `globalDefault` set true, a PodGroup with no `priorityClassName` has priority zero.

The priority of the PodGroup is an authoritative priority for all pods in the group during [workload-aware preemption](/feature/workload_aware_preemption_mechanism.md) events, even when priorities of individual pods forming this PodGroup differ.

* Read about Workload-Aware [Preemption](/definition/podgroup_preemption_and_disruption.md) algorithm.
* Learn about the Workload API.

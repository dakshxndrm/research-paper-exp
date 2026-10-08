---
type: Definition
title: Workload Placement and PodGroupTemplates
description: Advanced scheduling policies that group Pods for coordinated placement.
resource: source://workloads.md
tags:
- kubernetes
- scheduling
- workload placement
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- PodGroup
- scheduling group
- gang scheduling
- spec.schedulingGroup
---

While standard [workload resources](/definition/workload_resources.md) (like Deployments and Jobs) manage the lifecycle of Pods, you may have complex [scheduling](/scheduling/runtimeclass_scheduling_constraints.md) requirements where groups of Pods must be treated as a single unit. The Workload API allows you to define [PodGroupTemplates](/definition/podgrouptemplates.md) to group Pods and apply advanced [scheduling policies](/configuration/scheduling_policies_configuration.md) to them, such as gang scheduling. Controllers [create PodGroup](/procedure/creating_a_podgroup.md) objects from these templates at [runtime](/definition/container_runtime.md), and Pods reference their [PodGroup](/entity/podgroup.md) via the spec.schedulingGroup field. This is particularly useful for batch processing and machine learning workloads where all-or-nothing placement is required.

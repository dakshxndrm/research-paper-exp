---
type: Procedure
title: Creating a PodGroup
description: A step-by-step guide to creating a PodGroup.
resource: source://workloads__podgroup-api.md
tags:
- kubernetes
- podgroup-creation
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- creating a scheduling unit
- PodGroup creation
---

To create a [PodGroup](/definition/podgroup.md), you need to have the `[scheduling.k8s.io/v1alpha2](/entity/api_group.md)` [API group](/definition/api_group_resource_type_namespace_and_name.md) enabled and the `GenericWorkload` feature gate. You can then use the following manifest to create a PodGroup with a [gang scheduling policy](/definition/gang_scheduling_policy.md) that requires at least 4 [Pods](/definition/kubernetes_cluster_architecture.md) to be schedulable simultaneously.

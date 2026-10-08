---
type: Procedure
title: Requesting DRA Devices for a PodGroup
description: A step-by-step guide to requesting Dynamic Resource Allocation devices.
resource: source://workloads__podgroup-api.md
tags:
- kubernetes
- dra-devices
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- requesting DRA resources
- DRA device allocation
---

Devices available through Dynamic [Resource Allocation](/entity/resourceclaim.md) (DRA) can be requested by a [PodGroup](/definition/podgroup.md) through its `spec.resourceClaims` field. ResourceClaims associated with PodGroups can be shared by all [Pods](/definition/kubernetes_cluster_architecture.md) belonging to the group.

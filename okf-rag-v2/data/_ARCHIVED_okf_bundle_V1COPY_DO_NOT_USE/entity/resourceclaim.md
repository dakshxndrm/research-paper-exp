---
type: Entity
title: ResourceClaim
description: A resource allocation for a PodGroup.
resource: source://workloads__podgroup-api.md
tags:
- kubernetes
- resourceclaim
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- resource allocation
- DRA claim
---

ResourceClaims associated with PodGroups can be shared by all [Pods](/definition/kubernetes_cluster_architecture.md) belonging to the group. With only a reference to the [PodGroup](/definition/podgroup.md) in the ResourceClaim's `status.reservedFor` instead of each individual Pod, any number of Pods in the same PodGroup can share a ResourceClaim.

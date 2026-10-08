---
type: Definition
title: PodGroup resource claims for DRA devices
description: Devices available through Dynamic Resource Allocation can be requested
  by a PodGroup through its spec.resourceClaims field, allowing shared references
  to ResourceClaims by all Pods in the group.
resource: source://workloads__podgroup-api.md
tags:
- kubernetes
- dra
- resource claims
- scheduling
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- resourceClaims
- DRA devices
- Dynamic Resource Allocation
- status.reservedFor
- ResourceClaimTemplate
---

Devices available through Dynamic Resource Allocation (DRA) can be requested by a [PodGroup](/entity/podgroup.md) through its spec.resourceClaims field. ResourceClaims associated with PodGroups can be shared by all Pods belonging to the group. With only a reference to the PodGroup in the ResourceClaim's status.reservedFor instead of each individual Pod, any number of Pods in the same PodGroup can share a ResourceClaim. ResourceClaims can also be generated from ResourceClaimTemplates for each PodGroup, allowing the devices allocated to each generated ResourceClaim to be shared by the Pods in each PodGroup.

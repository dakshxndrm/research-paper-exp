---
type: Distribution
title: EndpointSlice distribution logic and rebalancing
description: The control plane tries to fill EndpointSlices as full as possible but
  does not actively rebalance them. The distribution logic prioritizes limiting EndpointSlice
  updates over perfect distribution, preferring to create new EndpointSlices rather
  than update multiple existing ones.
resource: source://services-networking__endpoint-slices.md
tags:
- kubernetes
- distribution
- controller logic
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- endpoint slice distribution
- rebalancing logic
- fill EndpointSlices
---

The [control plane](/definition/control_plane_components.md) tries to fill EndpointSlices as full as possible, but does not actively rebalance them. The logic iterates through existing EndpointSlices, removes unwanted endpoints, and updates matching endpoints that have changed. It then fills modified slices with new endpoints. If new endpoints remain, it tries to fit them into previously unchanged slices and/or [create](/operations/kubectl_resource_management_operations.md) new ones, prioritizing limiting updates over perfect distribution.

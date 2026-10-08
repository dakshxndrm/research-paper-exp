---
type: Policy
title: Endpoint Slice Creation and Management
description: The control plane creates and manages EndpointSlice objects.
resource: source://services-networking__endpoint-slices.md
tags:
- kubernetes
- control-plane
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- endpoint slice creation
- endpoint slice management
---

Most often, the [control plane](/definition/kubernetes_cluster_architecture.md) (specifically, the [endpoint slice controller](/entity/endpointslice_controller.md)) creates and manages EndpointSlice objects. There are a variety of other use cases for EndpointSlices, such as [service](/entity/kubernetes_service.md) mesh implementations, that could result in other entities or [controllers](/pattern/kubernetes_controller_pattern.md) managing additional sets of EndpointSlices.

---
type: Entity
title: EndpointSlice Controller
description: The endpoint slice controller creates and manages EndpointSlice objects.
resource: source://services-networking__endpoint-slices.md
tags:
- kubernetes
- control-plane
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- endpoint slice controller
- controller
---

The [endpoint slice](/definition/endpoint_slice.md) [controller](/pattern/kubernetes_controller_pattern.md) sets `endpointslice-controller.k8s.io` as the value for the label `endpointslice.[kubernetes](/policy/garbage_collection_in_kubernetes.md).io/managed-by` on all EndpointSlices it manages.

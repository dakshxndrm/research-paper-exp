---
type: Definition
title: Endpoint Slice
description: A Kubernetes resource that contains references to a set of network endpoints.
resource: source://services-networking__endpoint-slices.md
tags:
- kubernetes
- api
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- network endpoint
---

In [Kubernetes](/policy/garbage_collection_in_kubernetes.md), an EndpointSlice contains references to a set of network endpoints. The [control plane](/definition/kubernetes_cluster_architecture.md) automatically creates EndpointSlices for any [Kubernetes Service](/entity/kubernetes_service.md) that has a selector specified.

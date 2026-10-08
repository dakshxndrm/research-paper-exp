---
type: Duplicate endpoints
title: EndpointSlice duplicate endpoints across slices
description: Due to the nature of EndpointSlice changes, endpoints may be represented
  in more than one EndpointSlice at the same time. Clients must iterate through all
  existing EndpointSlices associated with a Service and build a complete list of unique
  network endpoints, handling deduplication.
resource: source://services-networking__endpoint-slices.md
tags:
- kubernetes
- duplicate endpoints
- kube-proxy
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- duplicate endpoints
- endpoint aggregation
- deduplication
---

Due to the nature of [EndpointSlice](/definition/service_api_and_stable_endpoints.md) changes, endpoints may be represented in more than one EndpointSlice at the same time. This naturally occurs as changes to different EndpointSlice objects can arrive at the Kubernetes client watch / cache at different times. Clients of the EndpointSlice API must iterate through all the existing EndpointSlices associated to a [Service](/component/service_load_balancing.md) and build a complete list of unique network endpoints. It is important to mention that endpoints may be duplicated in different EndpointSlices.

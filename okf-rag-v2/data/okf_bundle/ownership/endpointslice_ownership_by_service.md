---
type: Ownership
title: EndpointSlice ownership by Service
description: EndpointSlices are owned by the Service they track endpoints for, indicated
  by an owner reference on each EndpointSlice and a kubernetes.io/service-name label
  that enables simple lookups of all EndpointSlices belonging to a Service.
resource: source://services-networking__endpoint-slices.md
tags:
- kubernetes
- ownership
- service
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- Service ownership
- kubernetes.io/service-name label
- owner reference
---

In most use cases, EndpointSlices are owned by the [Service](/component/service_load_balancing.md) that the [endpoint slice](/definition/endpointslice_api_resource.md) object tracks endpoints for. This [ownership](/definition/owner_and_dependent_objects.md) is indicated by an [owner reference](/mechanism/owner_references_in_object_specifications.md) on each [EndpointSlice](/definition/service_api_and_stable_endpoints.md) as well as a kubernetes.io/service-name label that enables simple lookups of all EndpointSlices belonging to a Service.

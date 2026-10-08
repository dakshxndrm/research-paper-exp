---
type: Definition
title: EndpointSlice API resource
description: An EndpointSlice contains references to a set of network endpoints for
  a Kubernetes Service with a selector, automatically created by the control plane.
resource: source://services-networking__endpoint-slices.md
tags:
- kubernetes
- networking
- api
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- EndpointSlice object
- endpoint slice
---

# [EndpointSlice](/definition/service_api_and_stable_endpoints.md) API resource

In Kubernetes, an EndpointSlice contains references to a set of network endpoints. The [control plane](/definition/control_plane_components.md) automatically creates EndpointSlices for any Kubernetes [Service](/component/service_load_balancing.md) that has a selector specified. These EndpointSlices include references to all the Pods that match the Service selector. EndpointSlices group network endpoints together by unique combinations of IP family, protocol, port number, and Service name. The name of an EndpointSlice object must be a valid DNS subdomain name.

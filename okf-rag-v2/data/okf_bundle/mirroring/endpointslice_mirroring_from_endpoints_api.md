---
type: Mirroring
title: EndpointSlice mirroring from Endpoints API
description: The EndpointSlice API replaces the older Endpoints API. The control plane
  mirrors most user-created Endpoints resources to corresponding EndpointSlices, unless
  the Endpoints resource has a skip-mirror label, a leader annotation, the Service
  does not exist, or the Service has a selector. Individual Endpoints resources may
  translate into multiple EndpointSlices if they have multiple subsets or include
  endpoints with multiple IP families. A maximum of 1000 addresses per subset will
  be mirrored.
resource: source://services-networking__endpoint-slices.md
tags:
- kubernetes
- mirroring
- endpoints api
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- EndpointSlice mirroring
- Endpoints API mirroring
- skip-mirror label
---

The [EndpointSlice](/definition/service_api_and_stable_endpoints.md) API is a replacement for the older Endpoints API. To preserve compatibility with older controllers and user workloads that expect [kube-proxy](/definition/kube_proxy_optional.md) to route traffic based on Endpoints resources, the cluster's [control plane](/definition/control_plane_components.md) mirrors most user-created Endpoints resources to corresponding EndpointSlices. Individual Endpoints resources may translate into multiple EndpointSlices. This will occur if an Endpoints resource has multiple subsets or includes endpoints with multiple IP families (IPv4 and IPv6). A maximum of 1000 addresses per subset will be mirrored to EndpointSlices.

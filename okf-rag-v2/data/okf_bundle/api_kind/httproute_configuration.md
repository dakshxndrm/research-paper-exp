---
type: API Kind
title: HTTPRoute Configuration
description: Specifies routing behavior of HTTP requests from a Gateway listener to
  backend network endpoints.
resource: source://services-networking__gateway.md
tags:
- api
- kind
- http
- routing
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- httproute
- http route
- http route configuration
---

HTTPRoute specifies [routing](/definition/external_access_mechanisms.md) behavior of [HTTP requests](/api_communication/kubectl_api_request_process.md) from a [Gateway](/api_kind/gateway_resource.md) listener to backend network endpoints. For a [Service](/component/service_load_balancing.md) backend, an implementation may represent the backend as a Service IP or EndpointSlices. An HTTPRoute represents configuration applied to the underlying Gateway implementation, such as configuring additional traffic routes in a cloud load balancer. Traffic is routed based on Host header and request path matching rules.

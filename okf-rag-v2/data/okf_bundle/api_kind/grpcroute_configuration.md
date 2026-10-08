---
type: API Kind
title: GRPCRoute Configuration
description: Specifies routing behavior of gRPC requests from a Gateway listener to
  backend network endpoints.
resource: source://services-networking__gateway.md
tags:
- api
- kind
- grpc
- routing
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- grpcroute
- grpc route
- grpc route configuration
---

GRPCRoute specifies [routing](/definition/external_access_mechanisms.md) behavior of gRPC requests from a [Gateway](/api_kind/gateway_resource.md) listener to backend network endpoints. For a [Service](/component/service_load_balancing.md) backend, an implementation may represent the backend as a Service IP or EndpointSlices. Gateways supporting GRPCRoute are required to support HTTP/2 without an initial upgrade from HTTP/1. GRPCRoute allows matching specific gRPC services, so only requests for a specified method to a service will be forwarded; other RPC methods will not be matched.

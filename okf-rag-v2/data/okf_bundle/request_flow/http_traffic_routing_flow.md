---
type: Request Flow
title: HTTP Traffic Routing Flow
description: Describes the step-by-step process of routing HTTP requests from client
  to backend via Gateway and HTTPRoute.
resource: source://services-networking__gateway.md
tags:
- request flow
- http
- routing
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- http routing flow
- request flow
- traffic routing process
---

Here is a simple example of HTTP traffic being routed to a [Service](/component/service_load_balancing.md) by using a [Gateway](/api_kind/gateway_resource.md) and an [HTTPRoute](/api_kind/httproute_configuration.md). The request flow for a Gateway implemented as a reverse proxy begins with the client preparing an HTTP request for a URL. The client's DNS resolver queries for the destination name and learns a mapping to one or more IP addresses associated with the Gateway. The client sends a request to the Gateway IP address; the reverse proxy receives the HTTP request and uses the Host header to match a configuration derived from the Gateway and attached HTTPRoute. Optionally, the reverse proxy can perform request header and/or path matching based on match rules of the HTTPRoute, and can modify the request by adding or removing headers based on filter rules. Lastly, the reverse proxy forwards the request to one or more backends.

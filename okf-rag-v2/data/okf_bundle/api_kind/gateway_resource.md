---
type: API Kind
title: Gateway Resource
description: Defines an instance of traffic handling infrastructure for processing
  backend network endpoints.
resource: source://services-networking__gateway.md
tags:
- api
- kind
- gateway
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- gateway
---

Gateway describes an instance of traffic handling infrastructure that defines a network endpoint for processing traffic such as filtering, balancing, and splitting for backends such as a [Service](/component/service_load_balancing.md). A Gateway may represent a cloud load balancer or an in-cluster proxy server configured to accept HTTP traffic. By default, a Gateway only accepts Routes from the same namespace; cross-namespace Routes require configuring `allowedRoutes`.

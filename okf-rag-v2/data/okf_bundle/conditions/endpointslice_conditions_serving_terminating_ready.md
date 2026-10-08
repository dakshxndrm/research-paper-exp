---
type: Conditions
title: EndpointSlice conditions serving terminating ready
description: 'The EndpointSlice API stores three conditions: serving, terminating,
  and ready. Serving indicates the endpoint should be used for Service traffic. Terminating
  indicates the endpoint is being shut down. Ready is a shortcut for serving and not
  terminating.'
resource: source://services-networking__endpoint-slices.md
tags:
- kubernetes
- conditions
- endpoint status
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- serving condition
- terminating condition
- ready condition
---

The [EndpointSlice](/definition/service_api_and_stable_endpoints.md) API stores conditions about endpoints that may be useful for consumers. The three conditions are serving, terminating, and ready. The serving condition indicates that the endpoint is currently serving responses and should be used as a target for [Service](/component/service_load_balancing.md) traffic. The terminating condition indicates that the endpoint is terminating. The ready condition is essentially a shortcut for checking serving and not terminating.

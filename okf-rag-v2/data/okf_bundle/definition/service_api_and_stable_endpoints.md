---
type: Definition
title: Service API and Stable Endpoints
description: Explains the Service API for providing stable endpoints to backend pods,
  including EndpointSlice management and service proxying.
resource: source://services-networking.md
tags:
- networking
- services
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- Service API
- stable endpoints
- EndpointSlice
- service proxying
---

# [Service](/component/service_load_balancing.md) API and Stable Endpoints

The Service API lets you provide a stable (long lived) IP address or hostname for a service implemented by one or more backend pods, where the individual pods making up the service can change over time.

* Kubernetes automatically manages EndpointSlice objects to provide information about the pods currently backing a Service.
* A [service proxy](/definition/kube_proxy_optional.md) implementation monitors the set of Service and EndpointSlice objects, and programs the data plane to route service traffic to its backends, by using operating system or cloud provider APIs to intercept or rewrite packets.

---
type: Definition
title: Service Endpoint Management
description: Kubernetes Services dynamically update their endpoint lists to exclude
  failed Pods, ensuring traffic routes only to healthy instances.
resource: source://architecture__self-healing.md
tags:
- kubernetes
- definition
- service
- endpoints
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- Service endpoints
- endpoint management
- traffic routing
---

- **[Load balancing](/component/service_load_balancing.md) for Services:** If a Pod behind a Service fails, Kubernetes automatically removes it from the Service's endpoints to route traffic only to healthy Pods.

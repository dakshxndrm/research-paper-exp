---
type: Component
title: Service Load Balancing
description: Kubernetes Services automatically remove failed Pods from their endpoint
  lists, routing traffic only to healthy Pods.
resource: source://architecture__self-healing.md
tags:
- kubernetes
- component
- service
- networking
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- Service
- load balancing
- Service endpoints
---

- **Load balancing for Services:** If a Pod behind a Service fails, Kubernetes automatically removes it from the Service's endpoints to route traffic only to healthy Pods.

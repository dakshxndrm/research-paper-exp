---
type: Procedure
title: Provision Dual-Stack Load Balancer
description: Procedure to provision dual-stack load balancer for Kubernetes clusters.
resource: source://services-networking__dual-stack.md
tags:
- kubernetes
- networking
- load balancer
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- dual-stack load balancer
---

To provision a [dual-stack](/classification/kubernetes_cluster_networking_types.md) [load balancer](/api/gateway_api.md), set the `.spec.type` field to `LoadBalancer` and the `.spec.ipFamilyPolicy` field to `PreferDualStack` or `RequireDualStack`.

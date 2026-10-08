---
type: Capability
title: Service Load Balancing for Self-Healing
description: Describes how Kubernetes Services automatically remove failed Pods from
  their endpoints to ensure traffic is routed only to healthy Pods.
resource: source://architecture__self-healing.md
tags:
- service
- load-balancing
- pod
- endpoint
- self-healing
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- Load balancing for Services
- Service load balancing
---

If a Pod behind a [Service](/entity/kubernetes_service.md) fails, [Kubernetes](/policy/garbage_collection_in_kubernetes.md) automatically removes it from the Service's endpoints to route traffic only to healthy [Pods](/definition/kubernetes_cluster_architecture.md).

---
type: Overview
title: Kubernetes Networking Problems
description: Describes the four distinct networking challenges addressed by Kubernetes
  and their solutions.
resource: source://cluster-administration__networking.md
tags:
- networking
- problems
- communication
- pods
- services
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- 4 distinct networking problems
- networking problems
---

[Kubernetes](/policy/garbage_collection_in_kubernetes.md) addresses 4 distinct networking problems:

1.  Highly-coupled container-to-container communications: This is solved by [Pods](/definition/kubernetes_cluster_architecture.md) and `localhost` communications.
2.  Pod-to-Pod communications: This is the primary focus of the source document.
3.  Pod-to-[Service](/entity/kubernetes_service.md) communications: This is covered by [Services](/procedure/configuring_load_balancing_and_services.md).
4.  External-to-Service communications: This is also covered by Services.

---
type: Definition
title: kubectl command-line tool
description: The primary interface for creating, inspecting, updating, and deleting
  Kubernetes objects, communicating with the cluster through the Kubernetes API.
resource: source://overview__kubectl.md
tags:
- tool
- command-line
- kubernetes
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- kubectl
- kubectl tool
- Kubernetes CLI
---

The `kubectl` tool communicates with your cluster through the Kubernetes API. It is the primary interface for creating, inspecting, updating, and deleting Kubernetes objects. Whether run from a laptop or from a Pod inside the cluster, it sends requests to the [API server](/definition/kube_apiserver.md). The tool complements [Kubernetes Components](/definition/kubernetes_cluster_architecture_overview.md) that run inside the cluster and the Kubernetes API that those components implement. Other clients, such as client libraries and web dashboards like [Headlamp](/entity/headlamp.md), also communicate through the same API.

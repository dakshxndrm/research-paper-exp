---
type: Implementation
title: Pod Network Implementation (CNI)
description: Manages the pod network.
resource: source://services-networking.md
tags:
- kubernetes
- networking
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- cni plugin
---

The [pod network](/model/kubernetes_network_model.md) implementation is responsible for managing the pod network. On Linux, most container runtimes use the Container Networking Interface (CNI) to interact with the pod network implementation.

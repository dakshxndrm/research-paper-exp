---
type: Procedure
title: Installing a CNI Plugin
description: Steps for installing a CNI plugin.
resource: source://extend-kubernetes__compute-storage-net__network-plugins.md
tags:
- kubernetes
- networking
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- install cni
- cni installation
---

A [Container Runtime](/entity/container_runtime.md), in the networking context, is a daemon on a [node](/entity/node.md) configured to provide CRI [Services](/procedure/configuring_load_balancing_and_services.md) for kubelet. In particular, the [Container Runtime](/definition/kubernetes_node_components_overview.md) must be configured to load the [CNI plugins](/list/kubernetes_networking_add_ons.md) required to [implement the Kubernetes network model](/mechanism/kubernetes_network_model_implementation.md).

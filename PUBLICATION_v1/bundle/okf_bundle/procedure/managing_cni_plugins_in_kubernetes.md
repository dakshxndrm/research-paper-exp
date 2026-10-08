---
type: Procedure
title: Managing CNI Plugins in Kubernetes
description: Steps for managing CNI plugins in Kubernetes.
resource: source://extend-kubernetes__compute-storage-net__network-plugins.md
tags:
- kubernetes
- networking
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- manage cni
- cni management
---

Prior to [Kubernetes](/policy/garbage_collection_in_kubernetes.md) 1.24, the [CNI plugins](/list/kubernetes_networking_add_ons.md) could also be managed by the [kubelet](/definition/kubernetes_node_components_overview.md) using the `cni-bin-dir` and `network-[plugin](/plugin/gangscheduling_plugin.md)` command-line parameters.

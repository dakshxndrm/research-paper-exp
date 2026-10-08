---
type: Configuration
title: Kubernetes IP Address Allocation
description: Details how non-overlapping IP addresses are allocated to Pods, Services,
  and Nodes within a Kubernetes cluster.
resource: source://cluster-administration__networking.md
tags:
- networking
- ip addresses
- configuration
- pods
- services
- nodes
- network plugin
- kube-apiserver
- kubelet
- cloud-controller-manager
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- IP address ranges
- allocate non-overlapping IP addresses
- assign IP addresses to Pods
- assign IP addresses to Services
- assign IP addresses to Nodes
---

[Kubernetes](/policy/garbage_collection_in_kubernetes.md) clusters require the allocation of non-overlapping IP addresses for Pods, [Services](/procedure/configuring_load_balancing_and_services.md), and [Nodes](/definition/kubernetes_cluster_architecture.md). These addresses are drawn from a range of available addresses configured in the following components:

-   The network [plugin](/plugin/gangscheduling_plugin.md) is configured to assign IP addresses to Pods.
-   The kube-apiserver is configured to assign IP addresses to Services.
-   The [kubelet](/definition/kubernetes_node_components_overview.md) or the [cloud-controller-manager](/component/cloud_controller_manager.md) is configured to assign IP addresses to Nodes.

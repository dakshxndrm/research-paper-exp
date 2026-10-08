---
type: Classification
title: Kubernetes Cluster Networking Types
description: Categorizes Kubernetes clusters based on the IP families configured for
  Pods, Services, and Nodes.
resource: source://cluster-administration__networking.md
tags:
- networking
- ip addresses
- cluster
- types
- ipv4
- ipv6
- dual-stack
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- cluster networking types
- IP families
- IPv4 only
- IPv6 only
- IPv4/IPv6 dual-stack
- IPv6/IPv4 dual-stack
- dual-stack
---

[Kubernetes](/policy/garbage_collection_in_kubernetes.md) clusters are categorized into different networking types based on the IP families configured. These types are:

-   **IPv4 only**: The network [plugin](/plugin/gangscheduling_plugin.md), kube-apiserver, and [kubelet](/definition/kubernetes_node_components_overview.md)/[cloud-controller-manager](/component/cloud_controller_manager.md) are configured to assign only IPv4 addresses.
-   **IPv6 only**: The network plugin, kube-apiserver, and kubelet/cloud-[controller](/pattern/kubernetes_controller_pattern.md)-manager are configured to assign only IPv6 addresses.
-   **[IPv4/IPv6](/policy/dual_stack_networking_policy.md) or IPv6/IPv4 dual-stack**: The network plugin, kube-apiserver, and kubelet or cloud-controller-manager are configured to assign both IPv4 and IPv6 addresses. All components must agree on the configured primary [IP family](/definition/address_types.md).

Kubernetes clusters only consider the IP families present on the Pods, [Services](/procedure/configuring_load_balancing_and_services.md), and [Nodes](/definition/kubernetes_cluster_architecture.md) objects, independently of other existing IPs of the represented objects. For example, only the IP addresses in `[node](/entity/node.md).status.addresses` or `pod.status.ips` are considered when implementing the [Kubernetes network model](/model/kubernetes_network_model.md) and defining the cluster type.

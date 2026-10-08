---
type: Mechanism
title: Kubernetes Network Model Implementation
description: Explains how the Kubernetes network model is implemented on each node,
  primarily through Container Network Interface (CNI) plugins.
resource: source://cluster-administration__networking.md
tags:
- networking
- implementation
- cni
- container runtime
- plugins
- nodes
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- implement the Kubernetes network model
- container runtime
- CNI plugins
- Container Network Interface plugins
---

The [Kubernetes network model](/model/kubernetes_network_model.md) is implemented by the [container runtime](/entity/container_runtime.md) on each [node](/entity/node.md). The most common container runtimes use [Container Network Interface](/component/kubernetes_network_plugins.md) (CNI) plugins to manage their network and security capabilities. Many different [CNI plugins](/list/kubernetes_networking_add_ons.md) exist from various vendors. Some of these provide only basic features of adding and removing network interfaces, while others provide more sophisticated solutions, such as integration with other container orchestration systems, running multiple CNI plugins, or advanced [IPAM](/procedure/configuring_ip_address_management_ipam.md) features.

---
type: Component
title: Kubernetes Network Plugins
description: Explains that network plugins implement the Container Network Interface
  (CNI) specification for IP allocation and inter-pod communication.
resource: source://architecture.md
tags:
- kubernetes
- networking
- plugin
- cni
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- Network plugins
- container network interface
- CNI specification
---

Network plugins are software components that implement the container network interface (CNI) specification. They are responsible for allocating IP addresses to [pods](/definition/kubernetes_cluster_architecture.md) and enabling them to communicate with each other within the cluster. Some network plugins provide their own, third-party implementation of proxying, which can mean the [node](/entity/node.md) does not need to run `[kube-proxy](/component/kube_proxy.md)`.

---
type: Definition
title: Kubernetes Node Components Overview
description: Outlines the components that run on every worker node to maintain running
  pods and provide the Kubernetes runtime environment.
resource: source://architecture.md
tags:
- kubernetes
- node
- component
- worker machine
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- Node components
- worker node components
- kubelet
- Container runtime
---

[Node](/entity/node.md) components run on every [node](/entity/worker_node.md), maintaining running [pods](/definition/kubernetes_cluster_architecture.md) and providing the [Kubernetes](/policy/garbage_collection_in_kubernetes.md) [runtime](/entity/container_runtime_1.md) environment. These components include `kubelet`, `[kube-proxy](/component/kube_proxy.md)` (optional), and a `[Container runtime](/entity/container_runtime.md)`. The `kubelet` is an agent that runs on each node in the cluster, ensuring that containers are running in a Pod. The `[Container runtime](/mechanism/kubernetes_network_model_implementation.md)` is the software that is responsible for running containers, such as containerd, CRI-O, or any other implementation of the Kubernetes Container Runtime Interface (CRI).

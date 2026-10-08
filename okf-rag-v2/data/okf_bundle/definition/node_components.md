---
type: Definition
title: Node Components
description: Describes the components that run on every worker node to maintain running
  pods and provide the Kubernetes runtime environment.
resource: source://architecture.md
tags:
- architecture
- kubernetes
- node
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- worker nodes
- Kubernetes node
---

Node components run on every node, maintaining running pods and providing the Kubernetes runtime environment. The [kubelet](/definition/kubelet.md) and [kube-proxy](/definition/kube_proxy_optional.md) are essential node components, along with the [container runtime](/definition/container_runtime.md). The kubelet ensures that containers are running in a pod, and kube-proxy maintains network rules on nodes.

---
type: Entity
title: Node Components
description: Components that run on every node to maintain running pods and provide
  the Kubernetes runtime environment.
resource: source://overview__components.md
tags:
- kubernetes
- architecture
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- worker node components
---

[Node components](/definition/node_components.md) run on every node, maintaining running pods and providing the Kubernetes runtime environment. Key components include [kubelet](/definition/kubelet.md), which ensures that Pods are running including their containers; [kube-proxy](/definition/kube_proxy_optional.md), which maintains network rules on nodes to implement Services (optional); and [Container runtime](/definition/container_runtime.md), the software responsible for running containers. Additionally, systemd may be run on a Linux node to supervise local components.

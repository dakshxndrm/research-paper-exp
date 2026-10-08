---
type: Definition
title: kube-proxy (optional)
description: A network proxy that runs on each node and maintains network rules for
  Service access, optional if a third-party network plugin provides equivalent behavior.
resource: source://architecture.md
tags:
- architecture
- kubernetes
- networking
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- kube-proxy
- network proxy
- Service proxy
---

kube-proxy is a network proxy that runs on each node. It maintains network rules on nodes. These network rules allow network communication to your Pods from network sessions inside or outside of your cluster. If you use a network plugin that implements packet forwarding for Services by itself, and providing equivalent behavior to kube-proxy, then you do not need to run kube-proxy on the nodes in your cluster.

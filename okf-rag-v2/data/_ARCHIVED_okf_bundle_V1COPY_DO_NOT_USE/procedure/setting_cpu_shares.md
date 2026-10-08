---
type: Procedure
title: Setting CPU Shares
description: How Kubernetes sets CPU shares for Pods.
resource: source://scheduling-eviction__pod-overhead.md
tags:
- kubernetes
- kubelet
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- kubelet
---

For CPU, if the Pod is Guaranteed or Burstable QoS, the [kubelet](/definition/kubernetes_node_components_overview.md) will set `cpu.shares` based on the sum of container requests plus the `overhead` defined in the PodSpec.

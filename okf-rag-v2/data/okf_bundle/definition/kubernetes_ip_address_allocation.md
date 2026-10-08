---
type: Definition
title: Kubernetes IP Address Allocation
description: Kubernetes clusters require non-overlapping IP address allocation for
  Pods, Services, and Nodes from configured ranges managed by the network plugin,
  kube-apiserver, and kubelet or cloud-controller-manager respectively.
resource: source://cluster-administration__networking.md
tags:
- ip addresses
- allocation
timestamp: '2026-09-02T17:04:11+00:00'
---

# Kubernetes IP Address Allocation

Kubernetes clusters require to allocate non-overlapping IP addresses for Pods, Services and Nodes, from a range of available addresses configured in the following components:

- The network plugin is configured to assign IP addresses to Pods.
- The [kube-apiserver](/definition/kube_apiserver.md) is configured to assign IP addresses to Services.
- The [kubelet](/definition/kubelet.md) or the [cloud-controller-manager](/definition/cloud_controller_manager.md) is configured to assign IP addresses to Nodes.

---
type: Procedure
title: CNI Plugin Installation Prior to Kubernetes 1.24
description: Before Kubernetes 1.24, CNI plugins could be managed by kubelet using
  command-line parameters cni-bin-dir and network-plugin.
resource: source://extend-kubernetes__compute-storage-net__network-plugins.md
tags:
- installation
- cni
- kubernetes 1.24
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- CNI plugin management before 1.24
- kubelet CNI parameters
- cni-bin-dir and network-plugin
---

Prior to Kubernetes 1.24, the [CNI plugins](/definition/external_components_implementing_kubernetes_networking.md) could also be managed by the [kubelet](/definition/kubelet.md) using the `cni-bin-dir` and `network-plugin` command-line parameters. These command-line parameters were removed in Kubernetes 1.24, with management of the CNI no longer in scope for kubelet.

---
type: Definition
title: Loopback Interface Requirement
description: Kubernetes requires container runtimes to provide a loopback interface
  `lo` for pod sandboxes, implementable via the CNI loopback plugin.
resource: source://extend-kubernetes__compute-storage-net__network-plugins.md
tags:
- networking
- loopback
- sandbox
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- loopback interface
- CNI loopback plugin
- sandbox loopback
---

In addition to the CNI plugin installed on the nodes for implementing the Kubernetes [network model](/definition/kubernetes_network_model_overview.md), Kubernetes also requires the container runtimes to provide a [loopback interface](/definition/container_runtime_cni_responsibilities.md) `lo`, which is used for each sandbox (pod sandboxes, vm sandboxes, ...). Implementing the loopback interface can be accomplished by re-using the CNI loopback plugin or by developing your own code to achieve this (see this example from CRI-O).

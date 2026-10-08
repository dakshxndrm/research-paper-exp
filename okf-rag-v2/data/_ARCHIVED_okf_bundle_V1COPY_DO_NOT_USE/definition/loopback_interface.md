---
type: Definition
title: Loopback Interface
description: A loopback interface is required for each sandbox.
resource: source://extend-kubernetes__compute-storage-net__network-plugins.md
tags:
- kubernetes
- networking
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- loopback
- sandbox
---

In addition to the [CNI plugin](/implementation/pod_network_implementation_cni.md) installed on the [nodes](/definition/kubernetes_cluster_architecture.md) for implementing the [Kubernetes network model](/model/kubernetes_network_model.md), [Kubernetes](/policy/garbage_collection_in_kubernetes.md) also requires the container runtimes to provide a loopback interface `lo`, which is used for each sandbox (pod sandboxes, vm sandboxes, ...).

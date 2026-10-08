---
type: List
title: Kubernetes Infrastructure Add-ons
description: This concept describes add-ons that enhance the underlying infrastructure
  capabilities of Kubernetes, including running virtual machines and detecting node
  problems.
resource: source://cluster-administration__addons.md
tags:
- infrastructure
- virtual machines
- node issues
- kubernetes
- bare-metal
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- infrastructure extensions
- KubeVirt
- node problem detector
---

*   **KubeVirt**: Is an add-on to run virtual machines on [Kubernetes](/policy/garbage_collection_in_kubernetes.md), usually run on bare-metal clusters.
*   **[node](/entity/node.md) problem detector**: Runs on Linux [nodes](/definition/kubernetes_cluster_architecture.md) and reports system issues as either Events or [Node](/entity/worker_node.md) conditions.

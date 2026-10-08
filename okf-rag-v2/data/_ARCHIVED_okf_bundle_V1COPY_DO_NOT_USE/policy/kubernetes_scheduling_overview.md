---
type: Policy
title: Kubernetes Scheduling Overview
description: A brief overview of Kubernetes scheduling principles.
resource: source://scheduling-eviction__kube-scheduler.md
tags:
- kubernetes
- scheduling
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- scheduling
- kube-scheduler
---

In [Kubernetes](/policy/garbage_collection_in_kubernetes.md), _scheduling_ refers to making sure that Pods are matched to [Nodes](/definition/kubernetes_cluster_architecture.md) so that [kubelet](/definition/kubernetes_node_components_overview.md) can run them. A scheduler watches for newly created Pods that have no [Node](/entity/node.md) assigned and finds the best [Node](/entity/worker_node.md) for each Pod to run on.

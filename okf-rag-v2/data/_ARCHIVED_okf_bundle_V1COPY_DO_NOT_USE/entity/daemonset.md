---
type: Entity
title: DaemonSet
description: Define Pods that provide facilities local to nodes.
resource: source://workloads.md
tags:
- kubernetes
- daemonset
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- node daemon
- system daemon
---

DaemonSet defines Pods that provide facilities that are local to nodes. Every time you add a [node](/entity/node.md) to your cluster that matches the specification in a DaemonSet, the [control plane](/definition/kubernetes_cluster_architecture.md) schedules a Pod for that DaemonSet onto the new [node](/entity/worker_node.md).

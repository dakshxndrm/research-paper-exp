---
type: Risk
title: Time skew risk
description: The TTL-after-finished controller's sensitivity to time skew in the cluster.
resource: source://workloads__controllers__ttlafterfinished.md
tags:
- kubernetes
- risk
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- time skew
- clock drift
---

Because the [TTL-after-finished controller](/entity/ttl_after_finished_controller.md) uses timestamps stored in the [Kubernetes](/policy/garbage_collection_in_kubernetes.md) jobs to determine whether the TTL has expired or not, this feature is sensitive to time skew in your cluster, which may cause the [control plane](/definition/kubernetes_cluster_architecture.md) to clean up [Job](/entity/job.md) objects at the wrong time.

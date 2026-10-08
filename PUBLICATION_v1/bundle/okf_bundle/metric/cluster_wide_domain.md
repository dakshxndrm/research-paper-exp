---
type: Metric
title: Cluster-Wide Domain
description: Evaluation of the entire cluster as a single domain in Kubernetes.
resource: source://scheduling-eviction__workload-aware-preemption.md
tags:
- kubernetes
- preemption
- priority
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- domain
---

The scheduler evaluates the entire cluster as a single domain instead of evaluating [preemption](/procedure/preemption.md) [node](/entity/node.md) by [node](/entity/worker_node.md).

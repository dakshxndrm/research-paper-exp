---
type: Policy Type
title: Basic Policy
description: The `basic` policy instructs the scheduler to evaluate all Pods on a
  best-effort basis.
resource: source://workloads__workload-api__policies.md
tags:
- kubernetes
- workloads
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- best effort policy
- non-gang policy
---

The `basic` policy instructs the scheduler to evaluate all [Pods](/definition/kubernetes_cluster_architecture.md) on a best-effort basis. Unlike the `gang` policy, a [PodGroup](/definition/podgroup.md) using the `basic` policy is considered feasible regardless of how many of its Pods are currently schedulable.

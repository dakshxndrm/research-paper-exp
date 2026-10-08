---
type: Policy
title: PodGroup Scheduling Policies
description: Every PodGroup must declare a scheduling policy in its `spec.schedulingPolicy`
  field.
resource: source://workloads__workload-api__policies.md
tags:
- kubernetes
- workloads
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- scheduling policies
- pod group policies
---

Every [PodGroup](/definition/podgroup.md) must declare a [scheduling policy](/concept/workload_placement.md) in its `spec.schedulingPolicy` field. This policy dictates how the scheduler treats the collection of [Pods](/definition/kubernetes_cluster_architecture.md) in the group.

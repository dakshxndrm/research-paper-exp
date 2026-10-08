---
type: Entity
title: Workload
description: A static, long-lived policy template that defines scheduling policies
  for groups of Pods.
resource: source://workloads__workload-api.md
tags:
- kubernetes
- entity
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- static policy
- long-lived policy
---

A `Workload` is a static, long-lived policy [template](/entity/podgrouptemplate.md). It defines what [scheduling policies](/policy/scheduling_policies_in_kube_scheduler.md) should be applied to groups of [Pods](/definition/kubernetes_cluster_architecture.md), but does not track [runtime](/entity/container_runtime_1.md) state itself.

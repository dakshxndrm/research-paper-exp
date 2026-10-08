---
type: Entity
title: StatefulSet
description: Run one or more related Pods that track state.
resource: source://workloads.md
tags:
- kubernetes
- statefulset
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- stateful deployment
- persistent deployment
---

StatefulSet lets you run one or more related [Pods](/definition/kubernetes_cluster_architecture.md) that do track state somehow. For example, if your [workload](/entity/workload.md) records data persistently, you can run a StatefulSet that matches each Pod with a [PersistentVolume](/metric/terminating_status_in_persistentvolumes.md).

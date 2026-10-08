---
type: Configuration
title: Configuring Pod Overhead via RuntimeClass
description: Pod overhead is configured by defining the overhead field in a RuntimeClass
  resource, which the admission controller applies at pod creation time.
resource: source://scheduling-eviction__pod-overhead.md
tags:
- kubernetes
- runtimeclass
- admission
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- RuntimeClass overhead
- overhead field configuration
- kata-fc RuntimeClass
---

You need to make sure a RuntimeClass is utilized which defines the [overhead field](/definition/pod_overhead_in_kubernetes.md). To work with [Pod overhead](/definition/pod_overhead.md), you need a RuntimeClass that defines the overhead field. Workloads which are created which specify the kata-fc [RuntimeClass handler](/definition/runtimeclass_handler.md) will take the memory and cpu overheads into account for resource quota calculations, node [scheduling](/scheduling/runtimeclass_scheduling_constraints.md), as well as Pod [cgroup sizing](/cgroup_sizing/pod_cgroup_sizing_with_overhead.md).

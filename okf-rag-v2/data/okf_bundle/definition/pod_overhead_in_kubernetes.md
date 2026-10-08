---
type: Definition
title: Pod Overhead in Kubernetes
description: Pod Overhead accounts for system resources consumed by Pod infrastructure
  beyond container requests and limits, set at admission time via RuntimeClass.
resource: source://scheduling-eviction__pod-overhead.md
tags:
- kubernetes
- scheduling
- runtimeclass
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- pod overhead
- overhead field
---

When you run a Pod on a Node, the Pod itself takes an amount of system resources that are additional to the resources needed to run the container(s) inside the Pod. In Kubernetes, [Pod Overhead](/definition/pod_overhead.md) is a way to account for the resources consumed by the Pod infrastructure on top of the container requests & limits. A pod's overhead is considered in addition to the sum of container resource requests when [scheduling](/scheduling/runtimeclass_scheduling_constraints.md) a Pod. Similarly, the [kubelet](/definition/kubelet.md) will include the [Pod overhead](/feature/runtimeclass_pod_overhead.md) when sizing the Pod cgroup, and when carrying out Pod eviction ranking.

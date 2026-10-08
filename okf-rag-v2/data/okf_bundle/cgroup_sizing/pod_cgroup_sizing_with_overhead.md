---
type: Cgroup Sizing
title: Pod cgroup Sizing with Overhead
description: The kubelet sets cgroup limits based on container limits plus the defined
  Pod overhead for CPU and memory.
resource: source://scheduling-eviction__pod-overhead.md
tags:
- kubernetes
- cgroup
- kubelet
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- cgroup sizing
- cpu.cfs_quota_us
- memory.limit_in_bytes
- Pod cgroup limits
---

If the resource has a limit defined for each container (Guaranteed QoS or Burstable QoS with limits defined), the [kubelet](/definition/kubelet.md) will set an upper limit for the pod cgroup associated with that resource (cpu.cfs_quota_us for CPU and memory.limit_in_bytes memory). This upper limit is based on the sum of the container limits plus the overhead defined in the PodSpec. For CPU, if the Pod is Guaranteed or Burstable QoS, the kubelet will set cpu.shares based on the sum of container requests plus the overhead defined in the PodSpec.

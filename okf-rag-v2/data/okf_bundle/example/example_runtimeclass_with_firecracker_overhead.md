---
type: Example
title: Example RuntimeClass with Firecracker overhead
description: A RuntimeClass example using Kata Containers and Firecracker that defines
  approximately 120MiB per Pod for the virtual machine and guest OS.
resource: source://scheduling-eviction__pod-overhead.md
tags:
- kubernetes
- example
- virtualization
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- kata-fc RuntimeClass
- Firecracker overhead example
- 120MiB overhead
---

You could use the following RuntimeClass definition with a virtualization [container runtime](/definition/container_runtime.md) (in this example, Kata Containers combined with the Firecracker virtual machine monitor) that uses around 120MiB per Pod for the virtual machine and the guest OS: Workloads which are created which specify the kata-fc [RuntimeClass handler](/definition/runtimeclass_handler.md) will take the memory and cpu overheads into account for resource quota calculations, node [scheduling](/scheduling/runtimeclass_scheduling_constraints.md), as well as Pod [cgroup sizing](/cgroup_sizing/pod_cgroup_sizing_with_overhead.md).

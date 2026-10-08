---
type: Scheduling
title: Pod Scheduling with Overhead
description: The scheduler considers Pod overhead plus container requests when finding
  a node with sufficient available resources.
resource: source://scheduling-eviction__pod-overhead.md
tags:
- kubernetes
- scheduler
- resource allocation
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- scheduler overhead consideration
- node scheduling with overhead
- 2.25 CPU and 320 MiB
---

When the [kube-scheduler](/definition/kube_scheduler.md) is deciding which node should run a new Pod, the scheduler considers that Pod's overhead as well as the sum of container requests for that Pod. For this example, the scheduler adds the requests and the overhead, then looks for a node that has 2.25 CPU and 320 MiB of memory available.

---
type: Definition
title: Pod Overhead
description: Mechanism to account for resources consumed by Pod infrastructure beyond
  container requests and limits.
resource: source://workloads__pods__advanced-pod-config.md
tags:
- resources
- computation
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- infrastructure resources
---

[Pod overhead](/feature/runtimeclass_pod_overhead.md) allows you to account for the resources consumed by the Pod infrastructure on top of the container requests and limits. This is configured using a RuntimeClass with the `overhead` field, specifying fixed memory and CPU values that are added to the Pod's total resource consumption beyond what individual containers request or limit.

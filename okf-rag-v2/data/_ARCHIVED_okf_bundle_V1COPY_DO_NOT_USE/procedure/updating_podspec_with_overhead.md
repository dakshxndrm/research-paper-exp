---
type: Procedure
title: Updating PodSpec with Overhead
description: How the RuntimeClass admission controller updates the PodSpec.
resource: source://scheduling-eviction__pod-overhead.md
tags:
- kubernetes
- runtime class
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- updating pod spec
- runtime class admission
---

At admission time, the [RuntimeClass](/entity/runtimeclass.md) [admission controller](/policy/priority_admission_controller.md) updates the [workload](/entity/workload.md)'s PodSpec to include the `overhead` as described in the RuntimeClass.

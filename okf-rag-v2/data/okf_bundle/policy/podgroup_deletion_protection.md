---
type: Policy
title: PodGroup deletion protection
description: A dedicated finalizer blocks PodGroup deletion until all referencing
  Pods reach a terminal phase (Succeeded or Failed).
resource: source://workloads__podgroup-api__lifecycle.md
tags:
- podgroup
- deletion
- finalizer
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- finalizer
- deletion blocking
---

A [PodGroup](/entity/podgroup.md) cannot be fully deleted while any of its Pods are still running. A dedicated [finalizer](/definition/what_are_finalizers.md) ensures that deletion is blocked until all Pods referencing the PodGroup have reached a terminal phase (Succeeded or Failed).

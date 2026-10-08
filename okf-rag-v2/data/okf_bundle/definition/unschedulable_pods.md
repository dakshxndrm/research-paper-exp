---
type: Definition
title: Unschedulable Pods
description: Pods that remain unassigned when no feasible nodes are available for
  scheduling.
resource: source://scheduling-eviction__kube-scheduler.md
tags:
- scheduling
- unschedulable
- pods
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- unscheduled pods
- Pod placement failure
---

# Unschedulable Pods

If none of the nodes are suitable, the pod remains unscheduled until the [scheduler](/definition/kube_scheduler.md) is able to place it.

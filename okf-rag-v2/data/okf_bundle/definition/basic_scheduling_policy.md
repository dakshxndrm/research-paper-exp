---
type: Definition
title: Basic Scheduling Policy
description: Defines the basic scheduling policy behavior for PodGroups, evaluating
  Pods individually without requiring simultaneous placement.
resource: source://workloads__workload-api__policies.md
tags:
- scheduling
- policy
- basic
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- basic policy
- best-effort scheduling
---

The `basic` policy instructs the [scheduler](/definition/kube_scheduler.md) to evaluate all Pods on a best-effort basis. Unlike the `gang` policy, a [PodGroup](/entity/podgroup.md) using the `basic` policy is considered feasible regardless of how many of its Pods are currently schedulable. This policy is suited for groups that do not require simultaneous startup but logically belong together, or to open the way for group-level constraints that do not imply "all-or-nothing" placement.

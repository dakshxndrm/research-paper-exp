---
type: Definition
title: Feasible Nodes
description: Nodes that meet the scheduling requirements for a Pod; if no nodes are
  suitable, the Pod remains unscheduled.
resource: source://scheduling-eviction__kube-scheduler.md
tags:
- scheduling
- feasible nodes
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- suitable nodes
- schedulable nodes
---

# Feasible Nodes

In a cluster, Nodes that meet the [scheduling](/scheduling/runtimeclass_scheduling_constraints.md) requirements for a Pod are called _feasible_ nodes. If none of the nodes are suitable, the pod remains unscheduled until the [scheduler](/definition/kube_scheduler.md) is able to place it.

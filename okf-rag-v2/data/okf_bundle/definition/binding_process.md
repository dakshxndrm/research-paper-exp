---
type: Definition
title: Binding Process
description: The scheduler notifies the API server about the scheduling decision,
  completing the Pod placement process.
resource: source://scheduling-eviction__kube-scheduler.md
tags:
- scheduling
- binding
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- binding
- Pod binding
- scheduling decision
---

# Binding Process

The [scheduler](/definition/kube_scheduler.md) finds [feasible Nodes](/definition/feasible_nodes.md) for a Pod and then runs a set of functions to score the feasible Nodes and picks a Node with the highest score among the feasible ones to run the Pod. The scheduler then notifies the [API server](/definition/kube_apiserver.md) about this decision in a process called _binding_.

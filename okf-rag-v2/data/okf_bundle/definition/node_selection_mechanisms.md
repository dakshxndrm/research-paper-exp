---
type: Definition
title: Node Selection Mechanisms
description: Methods to control Pod scheduling onto specific nodes using labels, affinity
  rules, and tolerations.
resource: source://workloads__pods__advanced-pod-config.md
tags:
- scheduling
- nodes
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- node selection
- scheduling rules
- affinity rules
---

Kubernetes provides several mechanisms to control which nodes your Pods are scheduled on. Node selectors are the simplest form of [node selection](/scheduling/runtimeclass_scheduling_constraints.md) constraint, requiring a node to have matching labels. Node affinity allows you to specify rules that constrain which nodes your Pod can be scheduled on, with required rules that must be satisfied and preferred rules that influence scheduling. Pod affinity and anti-affinity allow you to constrain which nodes a Pod can be scheduled on based on the labels of other Pods already running on nodes. Tolerations allow Pods to be scheduled on nodes with matching taints by specifying the key, operator, value, and effect.

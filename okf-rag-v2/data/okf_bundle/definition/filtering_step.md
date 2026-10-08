---
type: Definition
title: Filtering Step
description: The first step of node selection where the scheduler finds feasible Nodes
  that meet a Pod's scheduling requirements, such as resource availability.
resource: source://scheduling-eviction__kube-scheduler.md
tags:
- scheduling
- filtering
- node selection
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- filtering operation
- PodFitsResources
---

# Filtering Step

The _filtering_ step finds the set of Nodes where it's feasible to schedule the Pod. For example, the PodFitsResources filter checks whether a candidate Node has enough available resources to meet a Pod's specific resource requests. After this step, the node list contains any [suitable Nodes](/definition/feasible_nodes.md); often, there will be more than one. If the list is empty, that Pod isn't (yet) schedulable.

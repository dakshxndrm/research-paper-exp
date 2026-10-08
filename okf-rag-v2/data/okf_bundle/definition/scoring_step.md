---
type: Definition
title: Scoring Step
description: The second step of node selection where the scheduler ranks remaining
  feasible Nodes and selects the highest-scoring Node for Pod placement.
resource: source://scheduling-eviction__kube-scheduler.md
tags:
- scheduling
- scoring
- node selection
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- scoring operation
- Node ranking
---

# Scoring Step

In the _scoring_ step, the scheduler ranks the remaining nodes to choose the most suitable [Pod placement](/procedure/node_selection_process_in_kube_scheduler.md). The scheduler assigns a score to each Node that survived filtering, basing this score on the active scoring rules. Finally, [kube-scheduler](/definition/kube_scheduler.md) assigns the Pod to the Node with the highest ranking. If there is more than one node with equal scores, kube-scheduler selects one of these at random.

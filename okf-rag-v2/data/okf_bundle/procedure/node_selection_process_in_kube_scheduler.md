---
type: Procedure
title: Node Selection Process in kube-scheduler
description: 'kube-scheduler selects a node for a Pod in two steps: filtering to find
  feasible nodes, then scoring to rank remaining nodes and select the highest-scoring
  one.'
resource: source://scheduling-eviction__kube-scheduler.md
tags:
- scheduling
- procedure
- node selection
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- node selection
- scheduling process
- Pod placement
---

# [Node Selection](/scheduling/runtimeclass_scheduling_constraints.md) Process

[kube-scheduler](/definition/kube_scheduler.md) selects a node for the pod in a 2-step operation:

1. **Filtering**: The filtering step finds the set of Nodes where it's feasible to schedule the Pod. For example, the [PodFitsResources](/definition/filtering_step.md) filter checks whether a candidate Node has enough available resources to meet a Pod's specific resource requests. After this step, the node list contains any [suitable Nodes](/definition/feasible_nodes.md); often, there will be more than one. If the list is empty, that Pod isn't (yet) schedulable.

1. **Scoring**: In the [scoring step](/definition/scoring_step.md), the scheduler ranks the remaining nodes to choose the most suitable [Pod placement](/procedure/basic_scheduling_policy_with_tas.md). The scheduler assigns a score to each Node that survived filtering, basing this score on the active scoring rules. Finally, kube-scheduler assigns the Pod to the Node with the highest ranking. If there is more than one node with equal scores, kube-scheduler selects one of these at random.

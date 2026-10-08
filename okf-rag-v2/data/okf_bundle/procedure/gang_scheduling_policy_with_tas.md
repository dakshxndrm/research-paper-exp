---
type: Procedure
title: Gang Scheduling Policy with TAS
description: When applied to PodGroups with gang scheduling policy, TAS simulates
  the potential assignment of the full group of pods at once and guarantees that at
  least the specified minCount pods can fit together into the same topology domain
  before committing resources; if no feasible placement is found, the entire PodGroup
  becomes unschedulable.
resource: source://workloads__workload-api__topology-aware-scheduling.md
tags:
- scheduling
- gang
- policy
- topology
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- gang scheduling
- minCount
- placement feasibility
- PodGroup scheduling
---

When applied to PodGroups with `gang` [scheduling policy](/definition/podgroup_scheduling_policy.md), TAS simulates the potential assignment (*placement*) of the full group of pods at once. It guarantees that at least the specified `[minCount](/definition/gang_scheduling_constraints.md)` pods can fit together into the same [topology domain](/definition/topology_constraint_definition.md) before committing resources. If no feasible placement is found, the entire [PodGroup](/entity/podgroup.md) becomes unschedulable. This is the recommended approach for workloads like distributed AI and ML training that strictly require proximity to minimize inter-[pod communication](/definition/pod_network_communication.md) latency. If new pods are added to the PodGroup where some pods are already scheduled (for example, if pods are recreated), the [scheduler](/definition/kube_scheduler.md) will force all new incoming pods to land on the exact same topology domain where the existing pods currently reside. If that specific domain lacks sufficient capacity for the new pods, the pods will remain pending - even if it means that less than `minCount` pods are scheduled at this point. As of v1.36 [Topology-Aware Scheduling](/definition/topology_aware_scheduling_overview.md) does not trigger workload or pod [preemption](/definition/podgroup_preemption_and_disruption.md). If no feasible placement can be found without triggering preemption, the PodGroup becomes unschedulable.

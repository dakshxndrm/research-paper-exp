---
type: Feature
title: Topology-Aware Scheduling Overview
description: TAS is a Workload API feature that optimizes pod placement within a cluster
  by co-locating pods in a PodGroup into a specific topology domain to minimize inter-pod
  communication latency and prevent infrastructure fragmentation.
resource: source://workloads__workload-api__topology-aware-scheduling.md
tags:
- scheduling
- topology
- workload
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- Topology-Aware Scheduling
- workload scheduling
---

[Topology-Aware Scheduling](/definition/topology_aware_scheduling_overview.md) (TAS) is a feature of the Workload API that optimizes the placement of pods within the cluster. TAS ensures that all pods within a [PodGroup](/entity/podgroup.md) are co-located into a specific [topology domain](/definition/topology_constraint_definition.md), such as a single server rack or [zone](/topology/endpointslice_topology_information_nodename_and_zone.md). This minimizes inter-[pod communication](/definition/pod_network_communication.md) latency and prevents workload fragmentation across the cluster infrastructure.

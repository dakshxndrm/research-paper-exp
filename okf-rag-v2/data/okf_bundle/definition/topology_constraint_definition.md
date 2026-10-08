---
type: Definition
title: Topology Constraint Definition
description: A topology constraint defines a key corresponding to a Kubernetes node
  label representing the target topology domain; the scheduler enforces that all pods
  within the PodGroup are placed onto nodes sharing the exact same value for this
  specified label.
resource: source://workloads__workload-api__topology-aware-scheduling.md
tags:
- definition
- topology
- constraint
- label
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- topology constraint
- node label
- topology domain
- rack
- zone
---

To define a topology constraint for a [PodGroup](/entity/podgroup.md) you need to set a `key`, which corresponds to a [Kubernetes node](/definition/node_components.md) label, representing the target topology domain (for example, a rack or a [zone](/topology/endpointslice_topology_information_nodename_and_zone.md)). The [scheduler](/definition/kube_scheduler.md) strictly enforces that all pods within the PodGroup are placed onto nodes that share the exact same value for this specified label.

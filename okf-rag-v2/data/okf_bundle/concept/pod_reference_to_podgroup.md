---
type: Concept
title: Pod reference to PodGroup
description: Pods reference their PodGroup via the spec.schedulingGroup.podGroupName
  field; if the PodGroup does not exist, the Pod remains pending until the PodGroup
  is created.
resource: source://workloads__podgroup-api__lifecycle.md
tags:
- podgroup
- pod reference
- scheduling
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- Pod scheduling group
- podGroupName
- Pod reference PodGroup
---

Pods reference their [PodGroup](/entity/podgroup.md) via the [spec.schedulingGroup](/definition/workload_placement_and_podgrouptemplates.md).podGroupName field. If a Pod references a PodGroup that does not yet exist, the Pod remains pending. The [scheduler](/definition/kube_scheduler.md) automatically queues the Pod for [scheduling](/scheduling/runtimeclass_scheduling_constraints.md) once the PodGroup is created.

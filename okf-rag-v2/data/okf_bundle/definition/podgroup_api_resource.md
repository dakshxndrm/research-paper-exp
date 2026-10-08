---
type: Definition
title: PodGroup API resource
description: A runtime object representing a group of Pods scheduled together as a
  single unit, carrying both scheduling policy and scheduling status for a specific
  instance.
resource: source://workloads__podgroup-api.md
tags:
- kubernetes
- scheduling
- workload
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- PodGroup
- scheduling.k8s.io/v1alpha2 API resource
---

A [PodGroup](/entity/podgroup.md) is a [runtime](/definition/container_runtime.md) object that represents a group of Pods scheduled together as a single unit. While the Workload API defines [scheduling policy](/definition/podgroup_scheduling_policy.md) templates, PodGroups are the runtime counterparts that carry both the policy and the [scheduling status](/definition/podgroup_scheduling_status_conditions.md) for a specific instance of that group.

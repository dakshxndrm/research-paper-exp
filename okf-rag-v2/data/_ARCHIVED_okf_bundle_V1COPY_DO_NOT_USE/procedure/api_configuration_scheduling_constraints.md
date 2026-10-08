---
type: Procedure
title: 'API Configuration: Scheduling Constraints'
description: Declares scheduling constraints for a PodGroup.
resource: source://workloads__workload-api__topology-aware-scheduling.md
tags:
- workload-api
- scheduling
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- scheduling constraints
- placement-based scheduling
---

Every [PodGroup](/definition/podgroup.md) (or [PodGroupTemplate](/entity/podgrouptemplate.md)) may optionally declare the `schedulingConstraints` field, which is interpreted by the placement-based PodGroup [scheduling algorithm](/procedure/understanding_the_gang_scheduling_algorithm.md).

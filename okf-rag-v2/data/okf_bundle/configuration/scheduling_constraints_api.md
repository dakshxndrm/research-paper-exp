---
type: Configuration
title: Scheduling Constraints API
description: Every PodGroup or PodGroupTemplate may optionally declare a schedulingConstraints
  field, interpreted by the placement-based PodGroup scheduling algorithm; if defined
  in PodGroupTemplate, constraints are copied to referencing PodGroups.
resource: source://workloads__workload-api__topology-aware-scheduling.md
tags:
- configuration
- api
- scheduling
- constraints
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- schedulingConstraints
- PodGroupTemplate
- API configuration
- placement algorithm
---

Every [PodGroup](/entity/podgroup.md) (or [PodGroupTemplate](/entity/podgrouptemplate.md)) may optionally declare the `schedulingConstraints` field, which is interpreted by the placement-based [PodGroup scheduling algorithm](/algorithm/podgroup_scheduling_algorithm.md). If constraints are defined in PodGroupTemplate, they will be copied to referencing PodGroups. As of Kubernetes v1.36, the API supports topology constraints. As of Kubernetes v1.36, you can specify only a single [topology constraint](/definition/topology_constraint_definition.md) in each PodGroup.

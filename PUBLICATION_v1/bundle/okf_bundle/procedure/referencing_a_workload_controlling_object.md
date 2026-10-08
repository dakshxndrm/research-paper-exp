---
type: Procedure
title: Referencing a Workload Controlling Object
description: Describes how to link a workload back to the specific high-level object
  defining the application.
resource: source://workloads__workload-api.md
tags:
- kubernetes
- procedure
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- controller reference
- workload linking
---

The `controllerRef` field links the [Workload](/entity/workload.md) back to the specific high-level object defining the application, such as a [Job](/entity/job.md) or a custom CRD.

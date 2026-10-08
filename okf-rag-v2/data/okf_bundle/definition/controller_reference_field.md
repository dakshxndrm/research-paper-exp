---
type: Definition
title: Controller reference field
description: The controllerRef field links the Workload back to the specific high-level
  object defining the application, such as a Job or a custom CRD, for observability
  and tooling purposes.
resource: source://workloads__workload-api.md
tags:
- api
- reference field
- tooling
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- Workload controllerRef
- application reference
- high-level object link
---

# Controller reference field

The `controllerRef` field links the Workload back to the specific high-level object defining the application, such as a Job or a custom CRD. This is useful for observability and tooling. This data is not used to schedule or manage the Workload.

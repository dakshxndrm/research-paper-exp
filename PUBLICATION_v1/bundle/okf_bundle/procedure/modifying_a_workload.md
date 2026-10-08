---
type: Procedure
title: Modifying a Workload
description: Describes what happens when you modify an existing workload.
resource: source://workloads__workload-api.md
tags:
- kubernetes
- procedure
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- workload modification
- template update
---

The entire `[Workload](/entity/workload.md)` spec is immutable after creation: you cannot modify existing templates, add new templates, or remove templates from `[podGroupTemplates](/template/podgrouptemplates.md)`.

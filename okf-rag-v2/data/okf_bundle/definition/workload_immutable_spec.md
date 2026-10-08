---
type: Definition
title: Workload immutable spec
description: The entire Workload spec is immutable after creation; existing templates
  cannot be modified, new templates added, or templates removed from podGroupTemplates.
resource: source://workloads__workload-api.md
tags:
- api
- immutability
- workload policy
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- immutable API spec
- Workload creation
- static workload definition
---

# Workload immutable spec

The entire `Workload` spec is immutable after creation: you cannot modify existing templates, add new templates, or remove templates from `[podGroupTemplates](/definition/podgrouptemplates.md)`.

A `Workload` consists of two fields: a list of `PodGroupTemplates` and an optional controller reference. The entire `Workload` spec is immutable after creation.

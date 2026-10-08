---
type: Entity
title: Workload API
description: An API that provides PodGroupTemplates.
resource: source://workloads__podgroup-api.md
tags:
- kubernetes
- workload-api
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- API for workloads
- workload object
---

The [Workload API](/entity/workload_api.md) is an API that provides [PodGroupTemplates](/template/podgrouptemplates.md). It acts as a [long-lived policy](/entity/workload.md) definition, while PodGroups handle the transient, per-instance [runtime](/entity/container_runtime_1.md) state.

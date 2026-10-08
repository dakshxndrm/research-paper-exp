---
type: Policy
title: Priority Admission Controller
description: How the priority admission controller checks and sets priorities.
resource: source://workloads__workload-api__disruption-and-priority.md
tags:
- kubernetes
- workload-api
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- priority admission
- admission controller
---

The priority admission [controller](/pattern/kubernetes_controller_pattern.md) uses the `priorityClassName` field and populates the integer value of the priority. If the [priority class](/entity/priorityclass.md) is not found, the [PodGroup](/definition/podgroup.md) is rejected.

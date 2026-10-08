---
type: Procedure
title: Using Gang Scheduling with Jobs
description: Describes how to use gang scheduling with jobs in Kubernetes.
resource: source://workloads__workload-api.md
tags:
- kubernetes
- procedure
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- gang policy
- parallel indexed jobs
---

You do not need to create [Workload](/entity/workload.md) or [PodGroup](/definition/podgroup.md) objects yourself as the [Job controller](/component/kube_controller_manager.md) handles it automatically.

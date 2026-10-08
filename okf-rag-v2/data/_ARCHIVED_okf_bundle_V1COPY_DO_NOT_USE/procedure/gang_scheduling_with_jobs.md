---
type: Procedure
title: Gang Scheduling with Jobs
description: Describes how gang scheduling works with Jobs in Kubernetes.
resource: source://workloads__workload-api.md
tags:
- kubernetes
- procedure
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- gang policy
- parallel indexed jobs
---

When the `WorkloadWithJob` feature gate is enabled, the [Job controller](/component/kube_controller_manager.md) automatically creates [Workload](/entity/workload.md) and [PodGroup](/definition/podgroup.md) objects for parallel indexed Jobs.

---
type: Definition
title: Job completion status
description: The status conditions indicating a Job has finished execution.
resource: source://workloads__controllers__ttlafterfinished.md
tags:
- job status
- completion
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- Job finished
- Job Complete
- Job Failed
- Job status condition
---

The [TTL-after-finished controller](/definition/ttl_after_finished_controller.md) considers a Job eligible for cleanup once its status condition shows that the Job is either `Complete` or `Failed`. These are the two [status conditions](/definition/podgroup_conditions.md) that indicate a Job has finished execution.

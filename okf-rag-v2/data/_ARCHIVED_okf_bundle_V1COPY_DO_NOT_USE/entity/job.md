---
type: Entity
title: Job
description: A Kubernetes object that can be cleaned up by the TTL-after-finished
  controller.
resource: source://workloads__controllers__ttlafterfinished.md
tags:
- kubernetes
- entity
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- Kubernetes job
- finished Job
---

The [TTL-after-finished controller](/entity/ttl_after_finished_controller.md) is only supported for Jobs. You can use this mechanism to clean up finished Jobs (either `Complete` or `Failed`) automatically by specifying the `.spec.ttlSecondsAfterFinished` field of a Job, as in this example.

---
type: Entity
title: TTL-after-finished controller
description: A Kubernetes component responsible for cleaning up finished Jobs.
resource: source://workloads__controllers__ttlafterfinished.md
tags:
- kubernetes
- entity
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- controller
- cleanup mechanism
---

The [TTL-after-finished](/policy/ttl_after_finished_controller_policy.md) [controller](/pattern/kubernetes_controller_pattern.md) is only supported for Jobs. You can use this mechanism to clean up finished Jobs (either `Complete` or `Failed`) automatically by specifying the `.spec.ttlSecondsAfterFinished` field of a [Job](/entity/job.md), as in this example.

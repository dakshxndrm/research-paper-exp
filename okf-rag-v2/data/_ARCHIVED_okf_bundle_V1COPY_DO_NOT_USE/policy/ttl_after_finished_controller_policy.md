---
type: Policy
title: TTL-after-finished controller policy
description: A Kubernetes feature to limit Job lifetime after completion.
resource: source://workloads__controllers__ttlafterfinished.md
tags:
- kubernetes
- policy
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- TTL-after-finished
- time-to-live
---

[Kubernetes](/policy/garbage_collection_in_kubernetes.md)' [TTL-after-finished controller](/entity/ttl_after_finished_controller.md) provides a [time to live](/metric/ttl_seconds.md) mechanism to limit the lifetime of [Job](/entity/job.md) objects that have finished execution.

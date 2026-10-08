---
type: Metric
title: TTL seconds
description: The time-to-live period for finished Jobs.
resource: source://workloads__controllers__ttlafterfinished.md
tags:
- kubernetes
- metric
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- time to live
- cleanup period
---

You can set the TTL seconds at any time. Here are some examples for setting the `.spec.ttlSecondsAfterFinished` field of a [Job](/entity/job.md): * Specify this field in the Job manifest, so that a Job can be cleaned up automatically some time after it finishes.

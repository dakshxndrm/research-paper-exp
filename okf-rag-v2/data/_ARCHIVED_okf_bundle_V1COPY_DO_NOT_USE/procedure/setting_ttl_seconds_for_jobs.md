---
type: Procedure
title: Setting TTL seconds for Jobs
description: Specify the `.spec.ttlSecondsAfterFinished` field in a Job manifest or
  update an existing Job.
resource: source://workloads__controllers__ttlafterfinished.md
tags:
- kubernetes
- procedure
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- setting TTL
- TTL configuration
---

You can set the [TTL seconds](/metric/ttl_seconds.md) at any time. Here are some examples for setting the `.spec.ttlSecondsAfterFinished` field of a [Job](/entity/job.md): * Specify this field in the Job manifest, so that a Job can be cleaned up automatically some time after it finishes.

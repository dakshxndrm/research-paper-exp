---
type: Procedure
title: Updating TTL for finished Jobs
description: Modify the TTL period after a Job has finished.
resource: source://workloads__controllers__ttlafterfinished.md
tags:
- kubernetes
- procedure
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- updating TTL
- TTL modification
---

You can modify the TTL period, e.g. `.spec.ttlSecondsAfterFinished` field of Jobs, after the [job](/entity/job.md) is created or has finished.

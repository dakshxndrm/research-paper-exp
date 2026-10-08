---
type: Procedure
title: Detecting job status changes
description: Use a mutating admission webhook to detect changes to the `.status` of
  a Job and set a TTL accordingly.
resource: source://workloads__controllers__ttlafterfinished.md
tags:
- kubernetes
- procedure
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- job status detection
- TTL configuration
---

You can use a mutating admission webhook to set this field dynamically after the [Job](/entity/job.md) has finished, and choose different TTL values based on [job status](/resource/status_field.md), [labels](/concept/owner_references_and_labels.md).

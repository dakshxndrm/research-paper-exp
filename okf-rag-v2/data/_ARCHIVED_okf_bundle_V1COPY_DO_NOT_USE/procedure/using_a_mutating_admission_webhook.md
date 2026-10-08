---
type: Procedure
title: Using a mutating admission webhook
description: Set the TTL seconds dynamically at Job creation or completion using a
  mutating admission webhook.
resource: source://workloads__controllers__ttlafterfinished.md
tags:
- kubernetes
- procedure
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- mutating webhook
- TTL configuration
---

You can use a mutating admission webhook to set this field dynamically at [Job](/entity/job.md) creation time. Cluster administrators can use this to enforce a TTL policy for finished jobs.

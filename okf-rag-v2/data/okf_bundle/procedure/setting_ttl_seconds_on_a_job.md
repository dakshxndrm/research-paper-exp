---
type: Procedure
title: Setting TTL seconds on a Job
description: Methods to configure the ttlSecondsAfterFinished field on Jobs for automatic
  cleanup.
resource: source://workloads__controllers__ttlafterfinished.md
tags:
- configuration
- job spec
- cleanup policy
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- setting TTL
- configure TTL
- Job TTL configuration
- spec.ttlSecondsAfterFinished
---

The `.spec.ttlSecondsAfterFinished` field of a Job can be set using several methods. It can be specified in the Job manifest so the Job is cleaned up automatically after it finishes. For existing finished Jobs, the field can be manually set to make them eligible for cleanup. Cluster administrators can use a mutating admission webhook to set this field dynamically at Job creation time to enforce a TTL policy. The webhook can also set the field dynamically after the Job has finished, choosing different TTL values based on job status or labels; in this case, the webhook must detect changes to the `.status` of the Job and only set a TTL when the Job is marked as completed. Alternatively, users can write their own controller to manage the cleanup TTL for Jobs matching a particular selector.

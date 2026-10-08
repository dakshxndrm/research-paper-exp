---
type: Resource
title: .status field
description: A Kubernetes field used to store the status of a Job.
resource: source://workloads__controllers__ttlafterfinished.md
tags:
- kubernetes
- resource
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- job status
- TTL configuration
---

You can use a mutating admission webhook to set this field dynamically after the [Job](/entity/job.md) has finished, and choose different TTL values based on job status, [labels](/concept/owner_references_and_labels.md).

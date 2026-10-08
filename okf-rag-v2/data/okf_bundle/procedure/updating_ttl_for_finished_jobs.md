---
type: Procedure
title: Updating TTL for finished Jobs
description: How to modify the TTL period on existing finished Jobs.
resource: source://workloads__controllers__ttlafterfinished.md
tags:
- configuration
- job spec modification
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- modify TTL
- update TTL period
- extend TTL
- TTL adjustment
---

The TTL period, such as the `.[spec.ttlSecondsAfterFinished](/procedure/setting_ttl_seconds_on_a_job.md)` field of Jobs, can be modified after the Job is created or has finished. However, if the TTL period is extended after the existing `ttlSecondsAfterFinished` period has already expired, Kubernetes does not guarantee to retain that Job, even if the [update](/operations/kubectl_resource_management_operations.md) returns a successful API response.

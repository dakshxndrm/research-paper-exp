---
type: Definition
title: TTL-after-finished controller
description: A Kubernetes controller that automatically cleans up finished Job objects
  after a configurable time-to-live period.
resource: source://workloads__controllers__ttlafterfinished.md
tags:
- controller
- cleanup
- job lifecycle
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- TTL controller
- TTL-after-finished
- job cleanup controller
- finished job cleanup
---

The TTL-after-finished controller provides a [time-to-live](/definition/supporting_concepts_time_to_live_controller.md) mechanism to limit the lifetime of Job objects that have finished execution. It is only supported for Jobs and can clean up finished Jobs, either Complete or Failed, automatically by specifying the `.[spec.ttlSecondsAfterFinished](/procedure/setting_ttl_seconds_on_a_job.md)` field. The controller assumes a Job is eligible for cleanup TTL seconds after the [Job status condition](/definition/job_completion_status.md) changes to show the Job is either Complete or Failed. When the TTL expires, the Job becomes eligible for cascading removal, which deletes its [dependent objects](/definition/owner_and_dependent_objects.md) together with it. The controller honors Kubernetes object lifecycle guarantees, such as waiting for [finalizers](/definition/what_are_finalizers.md).

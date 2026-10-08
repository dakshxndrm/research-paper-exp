---
type: Concept
title: Cascading removal of Jobs
description: How the TTL-after-finished controller deletes Jobs and their dependent
  objects.
resource: source://workloads__controllers__ttlafterfinished.md
tags:
- cleanup
- object deletion
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- cascading deletion
- dependent object deletion
- Job cascading removal
---

When the [TTL-after-finished controller](/definition/ttl_after_finished_controller.md) cleans up a Job, it deletes the Job cascadingly, meaning it deletes its [dependent objects](/definition/owner_and_dependent_objects.md) together with the Job. This ensures that all resources created by the Job are also removed when the Job's TTL expires.

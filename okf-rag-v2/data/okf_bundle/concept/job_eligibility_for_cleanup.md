---
type: Concept
title: Job eligibility for cleanup
description: The conditions that make a Job eligible for TTL-based cleanup.
resource: source://workloads__controllers__ttlafterfinished.md
tags:
- job status
- cleanup criteria
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- eligible Job
- cleanup eligibility
- Job completion status
---

A Job becomes eligible for cleanup TTL seconds after its status condition changes to show that the Job is either Complete or Failed. The timer starts once the Job status indicates completion, and the Job is only eligible for removal after the specified time period has elapsed.

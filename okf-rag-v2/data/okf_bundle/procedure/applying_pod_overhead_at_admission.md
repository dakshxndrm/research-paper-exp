---
type: Procedure
title: Applying Pod Overhead at Admission
description: The RuntimeClass admission controller mutates the PodSpec to include
  the overhead field; if already present, the Pod is rejected.
resource: source://scheduling-eviction__pod-overhead.md
tags:
- kubernetes
- admission
- workflow
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- admission controller mutation
- overhead field mutation
- PodSpec overhead
---

At admission time the RuntimeClass [admission controller](/control/admission_controller_for_owner_deletion.md) updates the workload's PodSpec to include the overhead as described in the RuntimeClass. If the PodSpec already has this field defined, the Pod will be rejected. In the given example, since only the RuntimeClass name is specified, the admission controller mutates the Pod to include an overhead.

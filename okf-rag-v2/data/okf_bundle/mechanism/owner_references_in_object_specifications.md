---
type: Mechanism
title: Owner References in Object Specifications
description: Dependent objects have a metadata.ownerReferences field that references
  their owner object using the object name and UID within the same namespace; Kubernetes
  sets this field automatically for objects like ReplicaSets, DaemonSets, Deployments,
  Jobs, and CronJobs, but it can also be configured manually.
resource: source://overview__working-with-objects__owners-dependents.md
tags:
- kubernetes
- ownerreferences
- metadata
- namespace
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- owner reference
- ownerReferences
- owner UID
- dependent owner reference
---

[Dependent objects](/definition/owner_and_dependent_objects.md) have a metadata.ownerReferences field that references their owner object. A valid owner reference consists of the object name and a UID within the same namespace as the dependent object. Kubernetes sets the value of this field automatically for objects that are dependents of other objects like ReplicaSets, DaemonSets, Deployments, Jobs and CronJobs, and ReplicationControllers. You can also configure these relationships manually by changing the value of this field. However, you usually don't need to and can allow Kubernetes to automatically manage the relationships.

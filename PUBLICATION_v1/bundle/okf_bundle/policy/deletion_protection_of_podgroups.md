---
type: Policy
title: Deletion Protection of PodGroups
description: Protection against deleting a PodGroup while its Pods are running.
resource: source://workloads__podgroup-api__lifecycle.md
tags:
- podgroup
- pod
- deletion
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- deletion protection
- finalizer
---

A `[PodGroup](/definition/podgroup.md)` cannot be fully deleted while any of its [Pods](/definition/kubernetes_cluster_architecture.md) are still running. A dedicated [finalizer](/procedure/using_finalizers_in_kubernetes.md) ensures that deletion is blocked until all `Pods` [referencing](/rule/referencing_non_existent_podgroups.md) the `PodGroup` have reached a terminal phase (`Succeeded` or `Failed`).

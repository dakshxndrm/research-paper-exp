---
type: Definition
title: PriorityClasses
description: Cluster-scoped API objects that map priority class names to integer values,
  where higher numbers indicate higher priority, used by the kube-scheduler to preempt
  lower-priority Pods when resources are insufficient.
resource: source://workloads__pods__advanced-pod-config.md
tags:
- scheduling
- priority
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- priority class
- Pod priority
- preemption
---

PriorityClasses allow you to set the importance of Pods relative to other Pods. If you assign a priority class to a Pod, Kubernetes sets the `.spec.priority` field for that Pod based on the [PriorityClass](/definition/pod_group_priority.md) you specified (you cannot set `.spec.priority` directly). If or when a Pod cannot be scheduled, and the problem is due to a lack of resources, the [kube-scheduler](/definition/kube_scheduler.md) tries to preempt lower priority Pods, in order to make [scheduling](/scheduling/runtimeclass_scheduling_constraints.md) of the higher priority Pod possible. A PriorityClass is a cluster-scoped API object that maps a priority class name to an integer priority value. Higher numbers indicate higher priority. Kubernetes provides two built-in PriorityClasses: `system-cluster-critical` for system components that are critical to the cluster, and `system-node-critical` for system components that are critical to individual nodes, which is the highest priority that Pods can have in Kubernetes.

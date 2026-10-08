---
type: Definition
title: Kubernetes Scheduling Overview
description: Scheduling ensures Pods are matched to Nodes so kubelet can run them,
  with the scheduler discovering unscheduled Pods and determining optimal placement.
resource: source://scheduling-eviction__kube-scheduler.md
tags:
- scheduling
- overview
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- scheduling
- Pod scheduling
- Node selection
---

# [Scheduling](/scheduling/runtimeclass_scheduling_constraints.md) Overview

In Kubernetes, _scheduling_ refers to making sure that Pods are matched to Nodes so that [kubelet](/definition/kubelet.md) can run them. A [scheduler](/definition/kube_scheduler.md) watches for newly created Pods that have no Node assigned. For every Pod that the scheduler discovers, the scheduler becomes responsible for finding the best Node for that Pod to run on. The scheduler reaches this placement decision taking into account the [scheduling principles](/definition/scheduling_principles.md) described below.

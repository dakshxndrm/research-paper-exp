---
type: Feature
title: RuntimeClass Pod Overhead
description: How to specify overhead resources associated with running a Pod using
  a RuntimeClass, allowing the cluster to account for it in scheduling decisions.
resource: source://containers__runtime-class.md
tags:
- overhead
- resources
- scheduling
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- pod overhead
- overhead resources
- resource accounting
---

## [Pod Overhead](/definition/pod_overhead.md)

You can specify _overhead_ resources that are associated with running a Pod. Declaring overhead allows the cluster (including the [scheduler](/definition/kube_scheduler.md)) to account for it when making decisions about Pods and resources. Pod overhead is defined in RuntimeClass through the `overhead` field. Through the use of this field, you can specify the overhead of running pods utilizing this RuntimeClass and ensure these overheads are accounted for in Kubernetes.

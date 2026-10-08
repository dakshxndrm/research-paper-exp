---
type: Procedure
title: Resource Quota Calculation
description: How Kubernetes calculates resource quotas for Pods.
resource: source://scheduling-eviction__pod-overhead.md
tags:
- kubernetes
- scheduler
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- kube-scheduler
---

If a ResourceQuota is defined, the sum of container requests as well as the `overhead` field are counted.

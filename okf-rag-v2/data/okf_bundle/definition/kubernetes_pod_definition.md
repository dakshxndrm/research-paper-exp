---
type: Definition
title: Kubernetes Pod Definition
description: A Pod represents a set of one or more running containers on a Kubernetes
  cluster.
resource: source://workloads.md
tags:
- kubernetes
- container
- workload
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- container group
- Kubernetes pod
---

In Kubernetes, a Pod represents a set of one or more running containers on your cluster. Kubernetes pods have a defined lifecycle. For example, once a pod is running in your cluster then a critical fault on the node where that pod is running means that all the pods on that node fail. Kubernetes treats that level of failure as final: you would need to [create](/operations/kubectl_resource_management_operations.md) a new Pod to recover, even if the node later becomes healthy.

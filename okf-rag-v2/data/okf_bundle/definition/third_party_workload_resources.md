---
type: Definition
title: Third-Party Workload Resources
description: Custom workload resources that provide additional behaviors not part
  of Kubernetes core.
resource: source://workloads.md
tags:
- kubernetes
- custom resource
- workload
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- custom resource definition
- third-party workload
- extension
---

In the wider Kubernetes ecosystem, you can find third-party [workload resources](/definition/workload_resources.md) that provide additional behaviors. Using a custom resource definition, you can add in a third-party workload resource if you want a specific behavior that's not part of Kubernetes' core. For example, if you wanted to run a group of Pods for your application but stop work unless all the Pods are available (perhaps for some high-throughput distributed task), then you can implement or install an extension that does provide that feature.

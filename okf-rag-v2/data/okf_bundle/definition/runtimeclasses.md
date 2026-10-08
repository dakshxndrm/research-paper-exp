---
type: Definition
title: RuntimeClasses
description: Cluster-scoped objects that represent available container runtimes, allowing
  specification of different runtime configurations for Pods requiring different isolation
  levels or features.
resource: source://workloads__pods__advanced-pod-config.md
tags:
- runtime
- container
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- runtime class
- container runtime
---

A RuntimeClass allows you to specify the low-level [container runtime](/definition/container_runtime.md) for a Pod. It is useful when you want to specify different container runtimes for different kinds of Pod, such as when you need different isolation levels or runtime features. A RuntimeClass is a cluster-scoped object that represents a container runtime that is available on some or all of your nodes. The cluster administrator installs and configures the concrete runtimes backing the RuntimeClass. They might set up that special [container runtime configuration](/definition/container_runtime_cni_responsibilities.md) on all nodes, or perhaps just on some of them. An example Pod using a RuntimeClass specifies the `[runtimeClassName](/usage/runtimeclass_pod_usage.md)` field in the Pod spec.

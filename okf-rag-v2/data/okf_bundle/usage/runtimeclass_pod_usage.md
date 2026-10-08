---
type: Usage
title: RuntimeClass Pod Usage
description: How to specify a RuntimeClass in a Pod spec to use a specific container
  runtime configuration.
resource: source://containers__runtime-class.md
tags:
- usage
- pod
- runtime
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- runtimeClassName
- Pod spec
- runtime selection
---

## Usage

Once [RuntimeClasses](/definition/runtimeclasses.md) are configured for the cluster, you can specify a `runtimeClassName` in the Pod spec to use it. This will instruct the [kubelet](/definition/kubelet.md) to use the named RuntimeClass to run this pod. If the named RuntimeClass does not exist, or the CRI cannot run the corresponding handler, the pod will enter the `Failed` terminal phase. If no `runtimeClassName` is specified, the default RuntimeHandler will be used, which is equivalent to the behavior when the RuntimeClass feature is disabled.

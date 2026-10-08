---
type: Motivation
title: RuntimeClass Performance vs Security Trade-off
description: The rationale for using different RuntimeClasses to balance performance
  and security for different Pods.
resource: source://containers__runtime-class.md
tags:
- motivation
- security
- performance
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- performance security
- runtime selection
- workload isolation
---

## Motivation

You can set a different RuntimeClass between different Pods to provide a balance of performance versus security. For example, if part of your workload deserves a high level of information security assurance, you might choose to schedule those Pods so that they run in a [container runtime](/definition/container_runtime.md) that uses hardware virtualization. You'd then benefit from the extra isolation of the alternative runtime, at the expense of some additional overhead. You can also use RuntimeClass to run different Pods with the same [container runtime](/definition/runtimeclasses.md) but with different settings.

---
type: Definition
title: RuntimeClass Resource
description: A Kubernetes resource that defines container runtime configuration for
  selecting how Pod containers are run.
resource: source://containers__runtime-class.md
tags:
- runtime
- container
- kubernetes
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- runtime class
- RuntimeClass object
- runtime configuration resource
---

## RuntimeClass Resource

This page describes the RuntimeClass resource and [runtime selection](/usage/runtimeclass_pod_usage.md) mechanism. RuntimeClass is a feature for selecting the [container runtime configuration](/definition/container_runtime_cni_responsibilities.md). The [container runtime](/definition/container_runtime.md) configuration is used to run a Pod's containers. The RuntimeClass resource currently only has 2 significant fields: the RuntimeClass name (metadata.name) and the handler. The object definition looks like this: [object definition]. The name of a RuntimeClass object must be a valid DNS subdomain name.

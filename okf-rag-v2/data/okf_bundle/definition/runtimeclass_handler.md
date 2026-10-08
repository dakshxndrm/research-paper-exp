---
type: Definition
title: RuntimeClass Handler
description: A valid DNS label name that identifies a specific container runtime configuration
  configured on nodes.
resource: source://containers__runtime-class.md
tags:
- runtime
- container
- configuration
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- handler name
- runtime handler
- CRI configuration identifier
---

## RuntimeClass Handler

The configurations available through RuntimeClass are [Container Runtime](/definition/container_runtime.md) Interface (CRI) implementation dependent. The handler must be a valid DNS label name. Configurations have a corresponding handler name, referenced by the RuntimeClass. For containerd, [runtime handlers](/criconfiguration/container_runtime_interface_configuration.md) are configured through containerd's configuration at `/etc/containerd/config.toml`. For CRI-O, runtime handlers are configured through CRI-O's configuration at `/etc/crio/crio.conf`.

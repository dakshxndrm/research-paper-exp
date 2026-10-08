---
type: Procedure
title: RuntimeClass Setup Process
description: Steps to configure RuntimeClass including CRI configuration and creating
  RuntimeClass resources.
resource: source://containers__runtime-class.md
tags:
- setup
- configuration
- procedure
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- setup process
- configuration steps
- runtime class creation
---

## Setup

### 1. Configure the CRI implementation on nodes

The configurations available through RuntimeClass are [Container Runtime](/definition/container_runtime.md) Interface (CRI) implementation dependent. See the corresponding documentation for your CRI implementation for how to configure. RuntimeClass assumes a homogeneous node configuration across the cluster by default (which means that all nodes are configured the same way with respect to container runtimes). To support heterogeneous node configurations, see [Scheduling](/scheduling/runtimeclass_scheduling_constraints.md) below. The configurations have a corresponding [handler name](/definition/runtimeclass_handler.md), referenced by the RuntimeClass. The handler must be a valid DNS label name.

### 2. [Create](/operations/kubectl_resource_management_operations.md) the corresponding RuntimeClass resources

The configurations setup in step 1 should each have an associated handler name, which identifies the configuration. For each handler, create a corresponding [RuntimeClass object](/definition/runtimeclass_resource.md). It is recommended that RuntimeClass write operations (create/update/patch/delete) be restricted to the cluster administrator.

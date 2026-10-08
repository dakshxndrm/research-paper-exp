---
type: Lifecycle Phase
title: Runtime Lifecycle Phase
description: Comprises access, compute, and storage protection for running containerized
  workloads.
resource: source://security__cloud-native-security.md
tags:
- security
- lifecycle
- runtime
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- runtime phase
- runtime protection
- container runtime security
---

The [Runtime](/definition/container_runtime.md) lifecycle phase comprises three critical areas: access, compute, and storage. Runtime protection of access focuses on securing the Kubernetes API through [authentication](/authentication/kubectl_authentication_methods.md), authorization, and TLS protection. Runtime protection of compute involves balancing [container isolation](/definition/workload_protection.md) and aggregation through [Pod Security Standards](/concept/runtime_protection_compute.md), specialized operating systems, resource quotas, workload partitioning, and Linux security modules. Runtime protection of storage involves integrating external storage [plugins](/extensibility/kubectl_plugins.md), enabling [API object encryption](/concept/runtime_protection_storage.md), using backups for durability, authenticating network storage connections, and implementing application-level data encryption.

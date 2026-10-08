---
type: Concept
title: 'Runtime Protection: Compute'
description: Guides container runtime security through privilege management and node
  isolation.
resource: source://security__cloud-native-security.md
tags:
- runtime
- compute
- container security
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- container compute security
- Pod Security Standards
- node isolation
---

Containers provide isolation between applications and a mechanism to combine isolated applications on the same host, meaning runtime security involves identifying trade-offs and finding appropriate balance. Kubernetes relies on a [container runtime](/definition/container_runtime.md) to set up and run containers. To protect compute at runtime, practices include enforcing [Pod Security](/definition/workload_protection.md) Standards to ensure applications run with only necessary privileges, running a specialized operating system on nodes designed for containerized workloads typically based on read-only immutable images, defining ResourceQuotas to fairly allocate shared resources, partitioning workloads across different nodes to improve isolation, using container runtimes that provide security restrictions, and on Linux nodes using Linux security modules such as AppArmor or seccomp.

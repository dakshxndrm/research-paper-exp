---
type: Operations
title: kubectl resource management operations
description: kubectl supports create, update, and delete operations for Kubernetes
  objects, with declarative management using apply recommended for production.
resource: source://overview__kubectl.md
tags:
- operations
- resource management
- declarative
- imperative
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- resource management
- create
- update
- delete
- kubectl apply
- declarative management
- imperative commands
---

The `[kubectl](/definition/kubectl_command_line_tool.md)` tool supports many operations, which fall into these broad categories: Manage resources – Create, update, and delete objects such as Pods, Deployments, and Services. Use `kubectl apply` for declarative management from configuration files. Imperative commands (such as `kubectl create` or `kubectl run`) are useful for development and experimentation, but are harder to reproduce and audit.

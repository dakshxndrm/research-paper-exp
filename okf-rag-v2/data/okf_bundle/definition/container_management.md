---
type: Definition
title: Container Management
description: Kubernetes manages containers in production environments, handling scaling,
  failover, and deployment patterns to ensure application availability.
resource: source://overview.md
tags:
- management
- deployment
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- container orchestration
- application deployment
---

Containers are a good way to bundle and run your applications. In a production environment, you need to manage the containers that run the applications and ensure that there is no downtime. For example, if a container goes down, another container needs to start. That's how Kubernetes comes to the rescue! Kubernetes provides you with a framework to run distributed systems resiliently. It takes care of scaling and failover for your application, provides [deployment](/definition/workload_resources.md) patterns, and more. For example: Kubernetes can easily manage a canary deployment for your system.

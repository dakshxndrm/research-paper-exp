---
type: Definition
title: Kubernetes API Access Overview
description: Explains how users and service accounts access the Kubernetes API through
  various methods and the security stages requests pass through.
resource: source://security__controlling-access.md
tags:
- access
- api
- security
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- API access
- Kubernetes API access
- API server access
---

Users access the Kubernetes API using `[kubectl](/definition/kubectl_command_line_tool.md)`, client libraries, or by making REST requests. Both human users and Kubernetes [service](/component/service_load_balancing.md) accounts can be authorized for API access. When a request reaches the API, it goes through several stages: transport security, [authentication](/authentication/kubectl_authentication_methods.md), authorization, admission control, and [auditing](/definition/auditing.md).

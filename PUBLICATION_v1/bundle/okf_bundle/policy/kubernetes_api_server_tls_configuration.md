---
type: Policy
title: Kubernetes API Server TLS Configuration
description: The Kubernetes API server's Transport Layer Security (TLS) configuration.
resource: source://security__controlling-access.md
tags:
- security
- tls
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- API server TLS
- Transport security
---

By default, the [Kubernetes API](/entity/kubernetes_api.md) server listens on port 6443 on the first non-localhost network interface, protected by TLS. In a typical production [Kubernetes cluster](/definition/kubernetes_cluster_architecture.md), the API serves on port 443.

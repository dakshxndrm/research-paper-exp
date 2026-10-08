---
type: Definition
title: API Server Port and Binding Configuration
description: Details the configurable port and IP address settings for the Kubernetes
  API server.
resource: source://security__controlling-access.md
tags:
- configuration
- port
- network
- api server
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- API server port
- secure-port
- bind-address
- port 6443
- port 443
---

By default, the [Kubernetes API server](/definition/kube_apiserver.md) listens on [port 6443](/definition/transport_security_in_kubernetes.md) on the first non-localhost network interface, protected by TLS. In a typical production Kubernetes cluster, the API serves on port 443. The port can be changed with the `--secure-port`, and the listening IP address with the `--bind-address` flag.

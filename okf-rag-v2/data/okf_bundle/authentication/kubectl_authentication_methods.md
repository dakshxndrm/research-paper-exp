---
type: Authentication
title: kubectl authentication methods
description: kubectl authenticates using kubeconfig cluster, user, and context definitions,
  with support for in-cluster authentication via ServiceAccount tokens.
resource: source://overview__kubectl.md
tags:
- authentication
- security
- kubeconfig
- serviceaccount
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- authentication
- cluster authentication
- user authentication
- context authentication
- ServiceAccount token
- in-cluster authentication
---

The `[kubectl](/definition/kubectl_command_line_tool.md)` tool connects to the [API server](/definition/kube_apiserver.md) and authenticates using the cluster, user, and context defined in your [kubeconfig file](/configuration/kubeconfig_file_location_and_environment.md). When running from outside a cluster, it uses the kubeconfig file to find the API server address and credentials. When running inside a Pod, it can use in-cluster authentication based on the ServiceAccount token mounted in the Pod.

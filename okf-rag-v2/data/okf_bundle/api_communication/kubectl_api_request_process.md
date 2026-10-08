---
type: API communication
title: kubectl API request process
description: kubectl translates commands into HTTP requests to the Kubernetes API,
  which validates, applies, and returns results for all operations.
resource: source://overview__kubectl.md
tags:
- api
- communication
- http
- validation
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- API request
- HTTP requests
- API server validation
- etcd storage
- API-driven path
---

When you run a command, `[kubectl](/definition/kubectl_command_line_tool.md)` translates your intent into one or more HTTP requests to the Kubernetes API. The [API server](/definition/kube_apiserver.md) validates each request, applies it to the [cluster state](/concept/desired_versus_current_state.md) stored in [etcd](/definition/etcd.md), and returns the result. This means every `kubectl` action, whether creating a [Deployment](/definition/workload_resources.md) or reading logs, follows the same API-driven path.

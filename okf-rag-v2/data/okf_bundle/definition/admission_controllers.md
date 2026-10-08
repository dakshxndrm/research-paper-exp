---
type: Definition
title: Admission Controllers
description: Plugins that intercept Kubernetes API requests to validate or mutate
  based on specific fields.
resource: source://security.md
tags:
- security
- api
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- admission plugins
- API request validation
- mutating controllers
---

[Admission controllers](/section/securing_a_kubernetes_cluster.md) are [plugins](/extensibility/kubectl_plugins.md) that intercept Kubernetes API requests and can validate or mutate the requests based on specific fields in the request. Thoughtfully designing these controllers helps to avoid unintended disruptions as Kubernetes APIs change across version updates.

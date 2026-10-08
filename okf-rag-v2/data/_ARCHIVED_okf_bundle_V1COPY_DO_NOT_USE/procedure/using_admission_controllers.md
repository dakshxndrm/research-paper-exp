---
type: Procedure
title: Using Admission Controllers
description: Intercept Kubernetes API requests and validate or mutate the requests
  based on specific fields in the request.
resource: source://security.md
tags:
- kubernetes
- security
- admission
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- admission controllers
- api validation
---

[Admission controllers](/guide/kubernetes_admission_control.md) are plugins that intercept [Kubernetes API](/entity/kubernetes_api.md) requests and can validate or mutate the requests based on specific fields in the request.

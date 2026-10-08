---
type: Guide
title: Kubernetes Admission Control
description: Explains admission controllers as plug-ins intercepting API server requests
  and provides good practices for designing admission webhooks.
resource: source://cluster-administration.md
tags:
- kubernetes
- admission controller
- webhook
- api server
- security
- plugin
- best practices
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- Using Admission Controllers
- Admission Webhook Good Practices
- admission controllers
- mutating admission webhooks
- validating admission webhooks
---

[Using Admission Controllers](/procedure/using_admission_controllers.md) explains plug-ins which intercepts requests to the [Kubernetes API](/entity/kubernetes_api.md) server after [authentication](/authentication/authentication_with_kubeconfig_file.md) and [authorization](/definition/kubernetes_authentication_and_authorization.md). Admission Webhook Good Practices provides good practices and considerations when designing mutating admission webhooks and validating admission webhooks.

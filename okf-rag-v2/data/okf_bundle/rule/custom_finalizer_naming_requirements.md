---
type: Rule
title: Custom finalizer naming requirements
description: Custom finalizer names must be publicly qualified, such as example.com/finalizer-name,
  and the API server rejects non-qualified names.
resource: source://overview__working-with-objects__finalizers.md
tags:
- naming-convention
- api-requirement
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- qualified finalizer name
- finalizer naming format
- API server rejection of unqualified finalizers
---

Custom [finalizer](/definition/what_are_finalizers.md) names must be publicly qualified finalizer names, such as `example.com/finalizer-name`. Kubernetes enforces this format; the [API server](/definition/kube_apiserver.md) rejects writes to objects where the change does not use qualified finalizer names for any custom finalizer.

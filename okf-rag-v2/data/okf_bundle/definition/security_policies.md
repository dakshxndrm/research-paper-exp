---
type: Definition
title: Security Policies
description: Kubernetes-native and ecosystem mechanisms for declarative restrictions
  on cluster changes and network filtering.
resource: source://security.md
tags:
- security
- policy
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- NetworkPolicy
- ValidatingAdmissionPolicy
- policy enforcement
---

You can define security policies using Kubernetes-native mechanisms, such as [NetworkPolicy](/definition/network_policies.md) (declarative control over network packet filtering) or ValidatingAdmissionPolicy (declarative restrictions on what changes someone can make using the Kubernetes API). Ecosystem implementations extend policy controls to source code review, container image approval, and [API access](/definition/kubernetes_api_access_overview.md) controls.

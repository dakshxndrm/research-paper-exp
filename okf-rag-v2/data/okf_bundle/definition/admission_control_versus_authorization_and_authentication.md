---
type: Definition
title: Admission Control Versus Authorization and Authentication
description: Clarifies the distinction between Admission Control modules and the earlier
  pipeline stages, including their scope and rejection behavior.
resource: source://security__controlling-access.md
tags:
- admission control
- pipeline
- security
- api request
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- Admission Control modules
- step 3
- request rejection
- object validation
- complex defaults
---

Unlike [Authentication](/authentication/kubectl_authentication_methods.md) and Authorization modules, if any [admission controller](/control/admission_controller_for_owner_deletion.md) module rejects, then the request is immediately rejected. In addition to rejecting objects, [admission controllers](/definition/admission_controllers.md) can also set complex defaults for fields. [Admission controllers](/section/securing_a_kubernetes_cluster.md) act on requests that [create](/operations/kubectl_resource_management_operations.md), modify, delete, or connect to (proxy) an object. Admission controllers do not act on requests that merely [read objects](/definition/authorization_policy_example_and_rules.md). When multiple admission controllers are configured, they are called in order.

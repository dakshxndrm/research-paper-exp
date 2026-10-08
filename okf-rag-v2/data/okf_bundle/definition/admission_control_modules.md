---
type: Definition
title: Admission Control Modules
description: Describes the function and operation of Admission Control modules in
  the request processing pipeline.
resource: source://security__controlling-access.md
tags:
- admission control
- security
- api request
- pipeline
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- Admission Controllers
- step 3
- request modification
- object creation
- object modification
---

[Admission Control modules](/definition/admission_control_versus_authorization_and_authentication.md) are software modules that can modify or reject requests. In addition to the attributes available to Authorization modules, Admission Control modules can access the contents of the object that is being created or modified. [Admission controllers](/definition/admission_controllers.md) act on requests that [create](/operations/kubectl_resource_management_operations.md), modify, delete, or connect to (proxy) an object. [Admission controllers](/section/securing_a_kubernetes_cluster.md) do not act on requests that merely [read objects](/definition/authorization_policy_example_and_rules.md). When multiple admission controllers are configured, they are called in order. This is shown as step 3 in the diagram. Unlike [Authentication](/authentication/kubectl_authentication_methods.md) and Authorization modules, if any [admission controller](/control/admission_controller_for_owner_deletion.md) module rejects, then the request is immediately rejected. In addition to rejecting objects, admission controllers can also set complex defaults for fields. The available Admission Control modules are described in Admission Controllers. Once a request passes all admission controllers, it is validated using the validation routines for the corresponding API object, and then written to the object store (shown as step 4).

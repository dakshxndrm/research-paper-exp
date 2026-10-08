---
type: Definition
title: Authorization Policy Example and Rules
description: Provides an example of a policy declaration and the rules governing read
  and write permissions for namespaced objects.
resource: source://security__controlling-access.md
tags:
- authorization
- policy
- permissions
- namespaced objects
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- policy declaration
- Bob's policy
- namespace permissions
- read objects
- write objects
- projectCaribou
- projectFish
---

For example, if Bob has the policy below, then he can read pods only in the namespace `projectCaribou`. If Bob makes the following request, the request is authorized because he is allowed to read objects in the `projectCaribou` namespace: If Bob makes a request to write (`[create](/operations/kubectl_resource_management_operations.md)` or `update`) to the objects in the `projectCaribou` namespace, his authorization is denied. If Bob makes a request to read (`get`) objects in a different namespace such as `projectFish`, then his authorization is denied.

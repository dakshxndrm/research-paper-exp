---
type: Definition
title: Authorization Process for API Requests
description: Describes how requests are authorized after authentication, the required
  attributes, and the supported authorization modules.
resource: source://security__controlling-access.md
tags:
- authorization
- access control
- security
- api request
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- authorization process
- access control
- ABAC mode
- RBAC Mode
- Webhook mode
- 403 status code
- policy declaration
---

After the request is authenticated as coming from a specific user, the request must be authorized. This is shown as step 2 in the diagram. A request must include the username of the requester, the requested action, and the object affected by the action. The request is authorized if an existing policy declares that the user has permissions to complete the requested action. Kubernetes authorization requires that you use common REST attributes to interact with existing organization-wide or cloud-provider-wide access control systems. It is important to use REST formatting because these control systems might interact with other APIs besides the Kubernetes API. Kubernetes supports multiple authorization modules, such as ABAC mode, RBAC Mode, and Webhook mode. When an administrator creates a cluster, they configure the authorization modules that should be used in the [API server](/definition/kube_apiserver.md). If more than one authorization modules are configured, Kubernetes checks each module, and if any module authorizes the request, then the request can proceed. If all of the modules deny the request, then the request is denied (HTTP status code 403).

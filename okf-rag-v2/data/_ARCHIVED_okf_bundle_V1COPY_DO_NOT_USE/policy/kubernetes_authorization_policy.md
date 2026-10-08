---
type: Policy
title: Kubernetes Authorization Policy
description: The policy governing authorization decisions for the Kubernetes API server.
resource: source://security__controlling-access.md
tags:
- security
- api access control
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- authorization policy
- access control
---

A request must include the username of the requester, the requested action, and the object affected by the action. The request is authorized if an existing policy declares that the user has permissions to complete the requested action.

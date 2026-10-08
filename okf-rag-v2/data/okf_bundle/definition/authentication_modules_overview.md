---
type: Definition
title: Authentication Modules Overview
description: Lists the various authentication modules supported by Kubernetes and
  their characteristics.
resource: source://security__controlling-access.md
tags:
- authentication
- modules
- security
- api request
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- authenticator modules
- client certificates
- password authentication
- plain tokens
- bootstrap tokens
- JSON Web Tokens
---

[Authentication modules](/definition/authentication_step_in_api_request.md) include client certificates, password, and plain tokens, bootstrap tokens, and JSON Web Tokens (used for [service](/component/service_load_balancing.md) accounts). Multiple [authentication](/authentication/kubectl_authentication_methods.md) modules can be specified, in which case each one is tried in sequence, until one of them succeeds.

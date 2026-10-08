---
type: Procedure
title: Configuring Authentication Modules
description: How to configure authentication modules for the Kubernetes API server.
resource: source://security__controlling-access.md
tags:
- security
- api access control
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- authenticators
- authentication configuration
---

Multiple [authentication](/authentication/authentication_with_kubeconfig_file.md) modules can be specified, in which case each one is tried in sequence, until one of them succeeds.

---
type: Definition
title: Control Plane Protection
description: Mechanism to control access to the Kubernetes API server using TLS encryption
  and authentication.
resource: source://security.md
tags:
- security
- access control
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- API server protection
- control plane security
- TLS encryption
---

A key security mechanism for any Kubernetes cluster is to control access to the Kubernetes API. Kubernetes expects you to configure and use TLS to provide [data encryption in transit](/definition/data_encryption_in_transit.md) within the [control plane](/definition/control_plane_components.md), and between the control plane and its clients.

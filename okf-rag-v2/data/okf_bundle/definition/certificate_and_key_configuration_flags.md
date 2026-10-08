---
type: Definition
title: Certificate and Key Configuration Flags
description: Describes the command-line flags used to set the TLS certificate and
  private key for the API server.
resource: source://security__controlling-access.md
tags:
- tls
- certificate
- key configuration
- api server flags
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- TLS certificate
- tls-cert-file
- tls-private-key-file
- private key configuration
---

The [API server](/definition/kube_apiserver.md) presents a certificate. This certificate may be signed using a private certificate authority (CA), or based on a public key infrastructure linked to a generally recognized CA. The certificate and corresponding private key can be set by using the `--tls-cert-file` and `--tls-private-key-file` flags.

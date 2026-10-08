---
type: Definition
title: Transport Security in Kubernetes
description: Describes the default TLS configuration for the Kubernetes API server
  and how certificates are managed for secure connections.
resource: source://security__controlling-access.md
tags:
- security
- tls
- transport
- certificate
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- TLS security
- API server TLS
- secure connection
- port 6443
- port 443
---

By default, the [Kubernetes API server](/definition/kube_apiserver.md) listens on port 6443 on the first non-localhost network interface, protected by TLS. In a typical production Kubernetes cluster, the API serves on port 443. The port can be changed with the `--secure-port`, and the listening IP address with the `--[bind-address](/definition/api_server_port_and_binding_configuration.md)` flag. The API server presents a certificate signed using a private certificate authority (CA) or based on a public key infrastructure linked to a generally recognized CA. The certificate and corresponding private key can be set by using the `--tls-cert-file` and `--[tls-private-key-file](/definition/certificate_and_key_configuration_flags.md)` flags. If your cluster uses a private certificate authority, you need a copy of that [CA certificate](/definition/client_certificate_trust_configuration.md) configured into your `~/.kube/config` on the client, so that you can trust the connection and be confident it was not intercepted. Your client can present a TLS client certificate at this stage.

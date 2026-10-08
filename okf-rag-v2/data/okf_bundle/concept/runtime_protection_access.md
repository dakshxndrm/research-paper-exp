---
type: Concept
title: 'Runtime Protection: Access'
description: Details Kubernetes API security through authentication, authorization,
  and TLS implementation.
resource: source://security__cloud-native-security.md
tags:
- runtime
- access
- api security
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- API access security
- cluster access control
- ServiceAccount management
---

The Kubernetes API is what makes the cluster work, and protecting this API is key to providing effective [cluster security](/section/securing_a_kubernetes_cluster.md). Beyond basic security checks, securing the cluster means implementing effective [authentication](/authentication/kubectl_authentication_methods.md) and authorization for [API access](/definition/kubernetes_api_access_overview.md). ServiceAccounts provide and manage security identities for workloads and [cluster components](/definition/kubernetes_cluster_architecture_overview.md). Kubernetes uses TLS to protect API traffic, and clusters should be deployed using TLS including for traffic between nodes and the [control plane](/definition/control_plane_components.md). Encryption keys must be protected, and if using Kubernetes' CertificateSigningRequests API, special attention must be paid to restricting misuse.

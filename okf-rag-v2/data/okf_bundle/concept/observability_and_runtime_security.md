---
type: Concept
title: Observability and Runtime Security
description: Guides extension of clusters with monitoring tools and cryptographic
  protection of logs and audit records.
resource: source://security__cloud-native-security.md
tags:
- observability
- runtime
- security
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- cluster observability
- runtime monitoring
- security dashboard
---

Kubernetes lets clusters be extended with extra tooling for monitoring and troubleshooting applications and clusters. Code running in containers can generate logs, publish metrics, or provide other observability data. When setting up a metrics dashboard, the entire chain of components that populate data into that dashboard must be reviewed and designed with enough resilience and integrity protection to rely on it even during incidents. Where appropriate, security measures below the Kubernetes layer such as cryptographically measured boot or authenticated distribution of time should be deployed to ensure fidelity of logs and audit records. For high-assurance environments, cryptographic protections should ensure logs are both tamper-proof and confidential.

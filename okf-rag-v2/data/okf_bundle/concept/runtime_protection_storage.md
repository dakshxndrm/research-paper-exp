---
type: Concept
title: 'Runtime Protection: Storage'
description: Details storage security through encryption, backups, and hardware-based
  key protection.
resource: source://security__cloud-native-security.md
tags:
- runtime
- storage
- encryption
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- storage security
- API object encryption
- hardware security module
---

To protect storage for the cluster and running applications, practices include integrating with external storage [plugins](/extensibility/kubectl_plugins.md) that provide [encryption at rest](/definition/data_encryption_at_rest.md) for volumes, enabling encryption at rest for API objects, protecting data durability using backups and verifying restorability, authenticating connections between cluster nodes and network storage, and implementing data encryption within applications. For encryption keys, generating these within specialized hardware provides the best protection against disclosure risks, and a hardware security module can let perform cryptographic operations without allowing the security key to be copied elsewhere.

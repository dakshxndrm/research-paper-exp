---
type: Definition
title: Kubernetes Network Model vs. Older Container Systems
description: Contrasts Kubernetes networking model with older container systems that
  required explicit container links or port mapping for cross-host communication.
resource: source://services-networking.md
tags:
- networking
- architecture
- history
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- network model comparison
- older container systems
- container links
- port mapping
---

# Kubernetes [Network Model](/definition/kubernetes_network_model_overview.md) vs. Older Container Systems

In older container systems, there was no automatic connectivity between containers on different hosts, and so it was often necessary to explicitly [create](/operations/kubectl_resource_management_operations.md) links between containers, or to map container ports to host ports to make them reachable by containers on other hosts. This is not needed in Kubernetes; Kubernetes's model is that pods can be treated much like VMs or physical hosts from the perspectives of port allocation, naming, service discovery, [load balancing](/component/service_load_balancing.md), application configuration, and migration.

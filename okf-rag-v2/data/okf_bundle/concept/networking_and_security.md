---
type: Concept
title: Networking and Security
description: Describes network security measures including NetworkPolicy, service
  mesh, and network plugin selection.
resource: source://security__cloud-native-security.md
tags:
- networking
- security
- cluster
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- network security
- NetworkPolicy
- service mesh security
---

Network security measures should include [NetworkPolicy](/definition/network_policies.md) or a [service](/component/service_load_balancing.md) mesh. Some network [plugins](/extensibility/kubectl_plugins.md) for Kubernetes provide encryption for the [cluster network](/definition/pod_network_communication.md) using technologies such as a virtual private network (VPN) overlay. By design, Kubernetes lets you use your own [networking](/definition/application_exposure_service_and_ingress.md) plugin for the cluster. The network plugin chosen and the way it is integrated can have a strong impact on the security of information in transit.

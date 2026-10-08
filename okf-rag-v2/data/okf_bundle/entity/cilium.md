---
type: Entity
title: Cilium
description: Networking, observability, and security solution with an eBPF-based data
  plane that can span multiple clusters and enforce L3-L7 policies.
resource: source://cluster-administration__addons.md
tags:
- addon
- networking
- observability
- security
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- Cilium networking
- Cilium eBPF
- Cilium security
---

Cilium is a [networking](/definition/application_exposure_service_and_ingress.md), observability, and security solution with an eBPF-based data plane. It provides a simple flat Layer 3 network with the ability to span [multiple clusters](/cluster_management/kubectl_context_switching.md) in either a native [routing](/definition/external_access_mechanisms.md) or overlay/encapsulation mode, and can enforce [network policies](/definition/network_policies.md) on L3-L7 using an identity-based security model decoupled from network addressing. Cilium can act as a replacement for [kube-proxy](/definition/kube_proxy_optional.md) and offers additional, opt-in observability and security features. Cilium is a CNCF project at the Graduated level.

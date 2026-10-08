---
type: SecurityWarning
title: SSH Tunnels Deprecation Notice
description: SSH tunnels for securing control plane to node communication are deprecated
  in favor of the Konnectivity service and should only be used with full understanding
  of the risks.
resource: source://architecture__control-plane-node-communication.md
tags:
- deprecated
- ssh
- security
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- deprecated SSH
- SSH tunnel warning
---

SSH tunnels are currently deprecated, so you shouldn't opt to use them unless you know what you are doing. The [Konnectivity](/procedure/konnectivity_service_for_control_plane_to_node_communication.md) [service](/component/service_load_balancing.md) is a replacement for this communication channel.

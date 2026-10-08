---
type: Definition
title: Windows Pod and Service Network Flows
description: Describes the supported network flows for TCP/UDP traffic involving Pods,
  Services, and Nodes on Windows.
resource: source://services-networking__windows-networking.md
tags:
- windows
- network flows
- tcp/udp
- pod
- service
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- Windows network flows
- pod-to-pod flow
- pod-to-service flow
- node-to-pod flow
---

For Node, Pod, and [Service](/component/service_load_balancing.md) objects, the following network flows are supported for TCP/UDP traffic: Pod → Pod (IP), Pod → Pod (Name), Pod → Service (Cluster IP), Pod → Service (PQDN, but only if there are no '.'), Pod → Service (FQDN), Pod → external (IP), Pod → external (DNS), Node → Pod, Pod → Node.

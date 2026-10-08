---
type: Definition
title: Control Plane Components
description: Explains the core components of the Kubernetes control plane that make
  global decisions and respond to cluster events.
resource: source://architecture.md
tags:
- architecture
- kubernetes
- control plane
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- control plane
- master components
- cluster management
---

The control plane's components make global decisions about the cluster (for example, [scheduling](/scheduling/runtimeclass_scheduling_constraints.md)), as well as detecting and responding to cluster events (for example, starting up a new pod when a [Deployment](/definition/workload_resources.md)'s replicas field is unsatisfied). Control plane components can be run on any machine in the cluster. However, for simplicity, setup scripts typically start all control plane components on the same machine, and do not run user containers on this machine.

---
type: Definition
title: cloud-controller-manager
description: Runs controllers that are specific to your cloud provider, integrating
  cloud infrastructure with the Kubernetes cluster.
resource: source://architecture.md
tags:
- architecture
- kubernetes
- cloud provider
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- cloud controller
- cloud integration
---

The cloud-controller-manager only runs controllers that are specific to your cloud provider. If you are running Kubernetes on your own premises, or in a learning environment inside your own PC, the cluster does not have a [cloud controller manager](/definition/cloud_controller_manager_overview.md). It combines several logically independent control loops into a single binary that you run as a single process.

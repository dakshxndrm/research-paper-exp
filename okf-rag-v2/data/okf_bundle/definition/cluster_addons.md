---
type: Definition
title: Cluster Addons
description: Optional cluster-level features implemented using Kubernetes resources,
  including DNS, Dashboard, monitoring, and logging.
resource: source://architecture.md
tags:
- architecture
- kubernetes
- addons
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- addons
- cluster features
---

[Addons](/entity/addons.md) use Kubernetes resources ([daemonset](/component/replicaset_and_deployment_controllers.md), [deployment](/definition/workload_resources.md), etc) to implement cluster features. Because these are providing cluster-level features, namespaced resources for addons belong within the kube-system namespace. Selected addons include DNS, which serves DNS records for Kubernetes services; Web UI (Dashboard), a general purpose web-based UI for managing clusters; Container Resource Monitoring, which records generic time-series metrics; and Cluster-level Logging, which saves [container logs](/operations/kubectl_debugging_operations.md) to a central log store.

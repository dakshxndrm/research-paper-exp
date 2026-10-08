---
type: Definition
title: kube-controller-manager
description: Runs multiple controller loops that regulate the state of the cluster.
resource: source://architecture.md
tags:
- architecture
- kubernetes
- controller
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- controller manager
- Kubernetes controller manager
---

kube-controller-manager runs multiple controller loops that regulate the state of the cluster. There are many different types of controllers, including the Node controller, [Job controller](/procedure/job_controller_workflow.md), [EndpointSlice](/definition/service_api_and_stable_endpoints.md) controller, and ServiceAccount controller. The [cloud-controller-manager](/definition/cloud_controller_manager.md) runs controllers specific to your cloud provider.

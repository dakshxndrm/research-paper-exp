---
type: Definition
title: Owner and Dependent Objects
description: In Kubernetes, some objects act as owners of other objects, where the
  owned objects are called dependents; for example, a ReplicaSet owns a set of Pods.
resource: source://overview__working-with-objects__owners-dependents.md
tags:
- kubernetes
- objects
- ownership
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- ownership
- dependent objects
- owned objects
---

In Kubernetes, some objects are owners of other objects. For example, a [ReplicaSet](/component/replicaset_and_deployment_controllers.md) is the owner of a set of Pods. These owned objects are dependents of their owner. Ownership is different from the labels and selectors mechanism that some resources also use. For example, consider a [Service](/component/service_load_balancing.md) that creates [EndpointSlice](/definition/service_api_and_stable_endpoints.md) objects. The Service uses labels to allow the [control plane](/definition/control_plane_components.md) to determine which EndpointSlice objects are used for that Service. In addition to the labels, each EndpointSlice that is managed on behalf of a Service has an [owner reference](/mechanism/owner_references_in_object_specifications.md). [Owner references](/definition/owner_references_and_dependents.md) help different parts of Kubernetes avoid interfering with objects they don't control.

---
type: Definition
title: Owner References and Dependents
description: Owner references link objects together, enabling the control plane to
  clean up dependent resources before deleting an object, with automatic management
  by Kubernetes in most cases.
resource: source://architecture__garbage-collection.md
tags:
- owner-references
- dependents
- namespace
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- owner references
- owner-dependent relationships
---

# Owners and dependents

Many objects in Kubernetes link to each other through *owner references*. Owner references tell the [control plane](/definition/control_plane_components.md) which objects are dependent on others. Kubernetes uses owner references to give the control plane, and other API clients, the opportunity to clean up related resources before deleting an object. In most cases, Kubernetes manages owner references automatically.

[Ownership](/definition/owner_and_dependent_objects.md) is different from the labels and selectors mechanism that some resources also use. For example, consider a [Service](/component/service_load_balancing.md) that creates [EndpointSlice](/definition/service_api_and_stable_endpoints.md) objects. The Service uses labels to allow the control plane to determine which EndpointSlice objects are used for that Service. In addition to the labels, each EndpointSlice that is managed on behalf of a Service has an [owner reference](/mechanism/owner_references_in_object_specifications.md). Owner references help different parts of Kubernetes avoid interfering with objects they don't control.

Cross-namespace owner references are disallowed by design. Namespaced dependents can specify cluster-scoped or namespaced owners. A namespaced owner must exist in the same namespace as the dependent. If it does not, the owner reference is treated as absent, and the dependent is subject to deletion once all owners are verified absent.

Cluster-scoped dependents can only specify cluster-scoped owners. In v1.20+, if a cluster-scoped dependent specifies a namespaced kind as an owner, it is treated as having an unresolvable owner reference, and is not able to be garbage collected.

In v1.20+, if the garbage collector detects an invalid cross-namespace ownerReference, or a cluster-scoped dependent with an ownerReference referencing a namespaced kind, a warning Event with a reason of [OwnerRefInvalidNamespace](/event/ownerrefinvalidnamespace_event.md) and an involvedObject of the invalid dependent is reported. You can check for that kind of Event by running [kubectl](/definition/kubectl_command_line_tool.md) get events -A --field-selector=reason=OwnerRefInvalidNamespace.

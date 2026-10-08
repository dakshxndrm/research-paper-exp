---
type: Definition
title: Orphaned Dependents
description: Orphaned dependents are objects left behind when an owner is deleted;
  by default Kubernetes deletes them, but behavior can be overridden to retain them
  as orphans.
resource: source://architecture__garbage-collection.md
tags:
- orphaned-dependents
- definition
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- orphan dependents
- orphaned objects
---

# Orphaned dependents

When Kubernetes deletes an owner object, the dependents left behind are called orphan objects. By default, Kubernetes deletes [dependent objects](/definition/owner_and_dependent_objects.md). To learn how to override this behaviour, see [Delete](/operations/kubectl_resource_management_operations.md) owner objects and orphan dependents.

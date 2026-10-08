---
type: Procedure
title: Configuring Garbage Collection Options
description: Administrators can tune garbage collection for specific Kubernetes controllers
  using dedicated configuration pages for cascading deletion, finished Jobs cleanup,
  and finalizers.
resource: source://architecture__garbage-collection.md
tags:
- gc-configuration
- procedure
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- gc configuration
- tuning garbage collection
---

# Configuring [garbage collection](/definition/supporting_concepts_garbage_collection.md)

You can tune garbage collection of resources by configuring options specific to the controllers managing those resources. The following pages show you how to configure garbage collection:

* Configuring [cascading deletion](/procedure/cascading_deletion_types.md) of Kubernetes objects
* Configuring cleanup of finished Jobs

* Learn more about [ownership](/definition/owner_and_dependent_objects.md) of Kubernetes objects.
* Learn more about Kubernetes [finalizers](/definition/what_are_finalizers.md).
* Learn about the [TTL controller](/definition/supporting_concepts_time_to_live_controller.md) that cleans up finished Jobs.

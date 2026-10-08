---
type: Configuration
title: Scheduling Profiles
description: Configuration method that allows Plugins to implement different scheduling
  stages including QueueSort, Filter, Score, Bind, Reserve, Permit, and others.
resource: source://scheduling-eviction__kube-scheduler.md
tags:
- scheduling
- profiles
- plugins
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- scheduling plugins
- plugin configuration
---

# [Scheduling](/scheduling/runtimeclass_scheduling_constraints.md) Profiles

There are two supported ways to configure the filtering and scoring behavior of the scheduler:

1. **[Scheduling Policies](/configuration/scheduling_policies_configuration.md)**: Allow you to configure _Predicates_ for filtering and _Priorities_ for scoring.

2. **Scheduling Profiles**: Allow you to configure [Plugins](/extensibility/kubectl_plugins.md) that implement different scheduling stages, including: `QueueSort`, `Filter`, `Score`, `Bind`, `Reserve`, `Permit`, and others. You can also configure the [kube-scheduler](/definition/kube_scheduler.md) to run different profiles.

---
type: Configuration
title: Scheduling Policies Configuration
description: 'Two ways to configure filtering and scoring behavior: Scheduling Policies
  use Predicates for filtering and Priorities for scoring, while Scheduling Profiles
  configure Plugins for different scheduling stages.'
resource: source://scheduling-eviction__kube-scheduler.md
tags:
- scheduling
- configuration
- policies
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- scheduling policies
- predicates and priorities
- scheduling configuration
---

# [Scheduling](/scheduling/runtimeclass_scheduling_constraints.md) Policies Configuration

There are two supported ways to configure the filtering and scoring behavior of the scheduler:

1. **Scheduling Policies**: Allow you to configure _Predicates_ for filtering and _Priorities_ for scoring.

1. **[Scheduling Profiles](/configuration/scheduling_profiles.md)**: Allow you to configure [Plugins](/extensibility/kubectl_plugins.md) that implement different scheduling stages, including: `QueueSort`, `Filter`, `Score`, `Bind`, `Reserve`, `Permit`, and others. You can also configure the [kube-scheduler](/definition/kube_scheduler.md) to run different profiles.

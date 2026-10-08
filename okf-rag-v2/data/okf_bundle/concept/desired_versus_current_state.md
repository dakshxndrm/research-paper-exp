---
type: Concept
title: Desired versus Current State
description: Kubernetes treats cluster state as potentially never stable, with controllers
  continuously working to align current state with desired state defined in resource
  specs.
resource: source://architecture__controller.md
tags:
- kubernetes
- cluster management
- state
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- cluster state
- desired state
- current state
---

Kubernetes takes a cloud-native view of systems, and is able to handle constant change. Your cluster could be changing at any point as work happens and control loops automatically fix failures. This means that, potentially, your cluster never reaches a stable state. As long as the controllers for your cluster are running and able to make useful changes, it doesn't matter if the overall state is stable or not.

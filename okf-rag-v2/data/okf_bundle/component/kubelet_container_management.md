---
type: Component
title: kubelet Container Management
description: The kubelet ensures that containers are running and restarts those that
  fail based on the configured restartPolicy.
resource: source://architecture__self-healing.md
tags:
- kubernetes
- component
- kubelet
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- kubelet
- container restart
- node agent
---

- **Container-level restarts:** If a container inside a Pod fails, Kubernetes restarts it based on the `[restartPolicy](/definition/container_level_restart_policy.md)`.

- **[kubelet](/definition/kubelet.md):** Ensures that containers are running, and restarts those that fail.

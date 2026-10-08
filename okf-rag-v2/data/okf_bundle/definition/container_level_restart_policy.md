---
type: Definition
title: Container-Level Restart Policy
description: The restartPolicy determines how Kubernetes handles container restarts,
  specifying behavior for failed or terminated containers.
resource: source://architecture__self-healing.md
tags:
- kubernetes
- definition
- restart
- policy
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- restartPolicy
- container restart policy
---

- **Container-level restarts:** If a container inside a Pod fails, Kubernetes restarts it based on the `restartPolicy`.

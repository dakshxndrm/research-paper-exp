---
type: Metric
title: Node Scores
description: The scores assigned to each Node during the scoring step.
resource: source://scheduling-eviction__kube-scheduler.md
tags:
- kubernetes
- scheduling
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- node ranking
- pod placement score
---

The scheduler assigns a score to each [Node](/entity/node.md) that survived filtering, basing this score on the active scoring rules.

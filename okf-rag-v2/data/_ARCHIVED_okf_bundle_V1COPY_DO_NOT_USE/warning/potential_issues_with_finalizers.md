---
type: Warning
title: Potential Issues with Finalizers
description: Potential issues that can arise from finalizers.
resource: source://overview__working-with-objects__finalizers.md
tags:
- kubernetes
- finalizers
- deletion issues
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- finalizer issues
- deletion issues
---

In some situations, finalizers can block the deletion of dependent objects, which can cause the targeted owner object to remain for longer than expected without being fully deleted.

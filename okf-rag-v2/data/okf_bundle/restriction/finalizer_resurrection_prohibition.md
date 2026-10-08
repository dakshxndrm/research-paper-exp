---
type: Restriction
title: Finalizer resurrection prohibition
description: After deletion is requested, the object cannot be resurrected; the only
  way is to delete it and make a new similar object.
resource: source://overview__working-with-objects__finalizers.md
tags:
- deletion-prohibition
- api-behavior
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- cannot resurrect deleted object
- object resurrection impossible after deletion
- must re-create object after failed deletion
---

After the deletion is requested, you cannot resurrect this object. The only way is to [delete](/operations/kubectl_resource_management_operations.md) it and make a new similar object.

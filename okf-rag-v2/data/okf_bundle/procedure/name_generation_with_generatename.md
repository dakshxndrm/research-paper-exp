---
type: Procedure
title: Name Generation with generateName
description: When `generateName` is provided instead of `name` in a resource create
  request, the server uses the provided value as a name prefix and appends a generated
  suffix; name conflicts may occur resulting in HTTP 409, but Kubernetes v1.31 and
  later attempt up to 8 times to generate a unique name before failing.
resource: source://overview__working-with-objects__names.md
tags:
- kubernetes
- naming-conventions
- resource-creation
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- generateName
- auto name generation
- name prefix generation
---

The server may generate a name when `generateName` is provided instead of `name` in a resource [create](/operations/kubectl_resource_management_operations.md) request. When `generateName` is used, the provided value is used as a name prefix, which server appends a generated suffix to. Even though the name is generated, it may conflict with existing names resulting in an HTTP 409 response. This became far less likely to happen in Kubernetes v1.31 and later, since the server will make up to 8 attempts to generate a [unique name](/definition/podgrouptemplate_unique_name.md) before returning an HTTP 409 response.

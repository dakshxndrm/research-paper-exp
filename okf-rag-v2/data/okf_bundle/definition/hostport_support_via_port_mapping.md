---
type: Definition
title: hostPort Support via Port Mapping
description: The CNI networking plugin supports hostPort functionality, which must
  be configured via the portMappings capability in the cni-conf-dir.
resource: source://extend-kubernetes__compute-storage-net__network-plugins.md
tags:
- networking
- hostport
- portmapping
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- hostPort support
- portMappings capability
- port mapping configuration
---

The CNI [networking](/definition/application_exposure_service_and_ingress.md) plugin supports hostPort. You can use the official portmap plugin offered by the CNI plugin team or use your own plugin with [portMapping](/definition/network_plugin_support_for_hostport.md) functionality. If you want to enable hostPort support, you must specify portMappings capability in your cni-conf-dir.

---
type: Definition
title: Pod Security Context
description: Configuration options that provide granular control over security settings
  for Pods and containers, including user IDs, capabilities, and seccomp profiles.
resource: source://workloads__pods__advanced-pod-config.md
tags:
- security
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- security context
- Pod security
- container security
---

The Security context field in the Pod specification provides granular control over security settings for Pods and containers. Pod-wide securityContext applies to the entire Pod, while container-level securityContext applies only to specific containers. User and Group IDs control which user/group the container runs as. Capabilities can be added or dropped, Seccomp Profiles set security computing profiles, and SELinux Options configure SELinux context. AppArmor profiles provide additional [access control](/definition/authorization_process_for_api_requests.md). Windows Options configure Windows-specific security settings. Privileged mode overrides many other security settings and should be avoided unless necessary. Windows containers can be run in privileged mode by setting the `windowsOptions.hostProcess` flag on the Pod-level security context.

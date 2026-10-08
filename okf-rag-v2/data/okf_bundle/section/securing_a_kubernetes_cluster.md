---
type: Section
title: Securing a Kubernetes Cluster
description: Documents security procedures including certificate generation, API access
  control, authentication, authorization, admission controllers, sysctl usage, and
  audit logging in Kubernetes.
resource: source://cluster-administration.md
tags:
- kubernetes
- security
- cluster hardening
- api access
- authentication
- authorization
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- Kubernetes security
- cluster security
- Kubernetes API security
- kubelet security
- admission controllers
- Kubernetes auditing
---

# Securing a Kubernetes Cluster

* Generate Certificates describes the steps to generate certificates using different tool chains.

* Kubernetes Container Environment describes the environment for [Kubelet](/definition/kubelet.md) managed containers on a [Kubernetes node](/definition/node_components.md).

* Controlling Access to the Kubernetes API describes how Kubernetes implements [access control](/definition/authorization_process_for_api_requests.md) for its own API.

* Authenticating explains [authentication](/authentication/kubectl_authentication_methods.md) in Kubernetes, including the various authentication options.

* Authorization is separate from authentication, and controls how HTTP calls are handled.

* Using [Admission Controllers](/definition/admission_controllers.md) explains plug-ins which intercepts requests to the [Kubernetes API server](/definition/kube_apiserver.md) after authentication and authorization.

* Admission Webhook Good Practices provides good practices and considerations when designing mutating admission webhooks and validating admission webhooks.

* Using Sysctls in a Kubernetes Cluster describes to an administrator how to use the `sysctl` command-line tool to set kernel parameters.

* [Auditing](/definition/auditing.md) describes how to interact with Kubernetes' audit logs.

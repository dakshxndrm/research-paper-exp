---
type: Definition
title: Authentication Step in API Request
description: Describes the authentication process that occurs after TLS establishment,
  including the modules used and the outcome of successful or failed authentication.
resource: source://security__controlling-access.md
tags:
- authentication
- security
- api request
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- authentication step
- Authenticator modules
- authentication modules
- 401 status code
- username availability
---

Once TLS is established, the HTTP request moves to the [Authentication](/authentication/kubectl_authentication_methods.md) step. This is shown as step 1 in the diagram. The cluster creation [script](/automation/kubectl_script_and_automate_output_formatting.md) or cluster admin configures the [API server](/definition/kube_apiserver.md) to run one or more [Authenticator modules](/definition/authentication_modules_overview.md). Authenticators are described in more detail in Authentication. The input to the authentication step is the entire HTTP request; however, it typically examines the headers and/or client certificate. Authentication modules include client certificates, password, and plain tokens, bootstrap tokens, and JSON Web Tokens (used for [service](/component/service_load_balancing.md) accounts). Multiple authentication modules can be specified, in which case each one is tried in sequence, until one of them succeeds. If the request cannot be authenticated, it is rejected with HTTP status code 401. Otherwise, the user is authenticated as a specific username, and the user name is available to subsequent steps to use in their decisions. Some authenticators also provide the group memberships of the user, while other authenticators do not. While Kubernetes uses usernames for [access control](/definition/authorization_process_for_api_requests.md) decisions and in request logging, it does not have a User object nor does it store usernames or other information about users in its API.

---
type: Mechanism
title: API Server Control
description: Kubernetes built-in controllers, such as the Job controller, manage cluster
  state by interacting with the API server to create, remove, or update resources
  like Pods and Job objects.
resource: source://architecture__controller.md
tags:
- kubernetes
- api server
- built-in
- job controller
- state management
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- control via API server
- built-in controllers
- Job controller
---

The [job controller](/component/kube_controller_manager.md) is an example of a [Kubernetes](/policy/garbage_collection_in_kubernetes.md) built-in controller. Built-in [controllers](/pattern/kubernetes_controller_pattern.md) manage state by interacting with the cluster [API server](/policy/api_server_behavior_in_kubernetes.md). When the [Job](/entity/job.md) controller sees a new task it makes sure that, somewhere in your cluster, the kubelets on a set of Nodes are running the right number of Pods to get the work done. The Job controller does not run any Pods or containers itself. Instead, the Job controller tells the API server to create or remove Pods. Other components in the [control plane](/definition/kubernetes_cluster_architecture.md) act on the new information (there are new Pods to schedule and run), and eventually the work is done. After you create a new Job, the [desired state](/philosophy/kubernetes_state_management.md) is for that Job to be completed. The Job controller makes the current state for that Job be nearer to your desired state: creating Pods that do the work you wanted for that Job, so that the Job is closer to completion. Controllers also update the objects that configure them. For example: once the work is done for a Job, the Job controller updates that [Job object](/entity/kubernetes_job_resource.md) to mark it `Finished`. (This is a bit like how some thermostats turn a light off to indicate that your room is now at the temperature you set).

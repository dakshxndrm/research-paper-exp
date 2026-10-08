---
type: Procedure
title: Job Controller Workflow
description: The Job controller monitors for new tasks and ensures the correct number
  of Pods are running to complete the work, then updates the Job object to mark it
  Finished.
resource: source://architecture__controller.md
tags:
- kubernetes
- job
- controller
- workload
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- Job controller
- job scheduling
- Pod creation by Job
---

The Job controller is an example of a Kubernetes built-in controller. [Built-in controllers](/category/built_in_controllers.md) manage state by interacting with the cluster [API server](/definition/kube_apiserver.md). Job is a Kubernetes resource that runs a pod, or perhaps several Pods, to carry out a task and then stop. When the Job controller sees a new task it makes sure that, somewhere in your cluster, the kubelets on a set of Nodes are running the right number of Pods to get the work done. The Job controller does not run any Pods or containers itself. Instead, the Job controller tells the API server to [create](/operations/kubectl_resource_management_operations.md) or remove Pods. Other components in the [control plane](/definition/control_plane_components.md) act on the new information, and eventually the work is done. After you create a new Job, the [desired state](/concept/desired_versus_current_state.md) is for that Job to be completed. The Job controller makes the current state for that Job be nearer to your desired state: creating Pods that do the work you wanted for that Job, so that the Job is closer to completion. Controllers also update the objects that configure them. For example: once the work is done for a Job, the Job controller updates that Job object to mark it Finished.

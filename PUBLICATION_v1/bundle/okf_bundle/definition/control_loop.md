---
type: Definition
title: Control Loop
description: A control loop is a non-terminating process that continuously regulates
  the state of a system by comparing a desired state to a current state.
resource: source://architecture__controller.md
tags:
- robotics
- automation
- system regulation
- definition
timestamp: '2026-07-27T19:53:46+00:00'
---

In robotics and automation, a _control loop_ is a non-[terminating](/metric/terminating_status_in_persistentvolumes.md) loop that regulates the state of a system. Here is one example of a control loop: a thermostat in a room. When you set the temperature, that's telling the thermostat about your *[desired state](/philosophy/kubernetes_state_management.md)*. The actual room temperature is the *current state*. The thermostat acts to bring the current state closer to the desired state, by turning equipment on or off.

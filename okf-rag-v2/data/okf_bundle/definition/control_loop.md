---
type: Definition
title: Control Loop
description: A non-terminating loop that regulates the state of a system by comparing
  desired and current states and taking corrective action.
resource: source://architecture__controller.md
tags:
- robotics
- automation
- systems
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- thermostat loop
---

In robotics and automation, a control loop is a non-terminating loop that regulates the state of a system. When you set the temperature, that's telling the thermostat about your [desired state](/concept/desired_versus_current_state.md). The actual room temperature is the current state. The thermostat acts to bring the current state closer to the desired state, by turning equipment on or off.

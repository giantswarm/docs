---
linkTitle: P1 Incident Process
title: P1 incident process
description: The process used by the Giant Swarm support team when a priority one incident is called.
weight: 100
menu:
  main:
    parent: overview
    weight: 20
user_questions:
  - What process does Giant Swarm follow in case of critical incidents?
owner:
  - https://github.com/orgs/giantswarm/teams/teddyfriends
last_review_date: 2023-05-02
---

After years of handling critical enterprise workloads in production, we have hardened our incident process based on our learnings. In this document we focus on critical incidents, called `Priority 1` (P1) incidents, though some of the steps could be part of regular incidents too. Giant Swarm classify incidents in a simple manner, critical incidents when a production system is impaired or regular incidents which have a straightforward process.

## Separation of Responsibilities

It’s important to make sure that everybody involved in an incident knows their role, what is expected from them and that it doesn’t conflict with others' responsibilities. Somewhat counterintuitively, a clear separation of responsibilities allows individuals more autonomy, as they do not need to ask all the time and coordinate actions.

### Roles

At Giant Swarm we have two defined roles: Incident Coordinators and Operations Engineers.

### Incident Coordinator

The Incident Coordinator (IC) holds the high-level state about the incident. They structure the incident response, assigning responsibilities according to need and priority. De facto, the IC holds all positions/responsibilities that they have not delegated. If appropriate, they can remove roadblocks that prevent Operations Engineers from working most effectively.

The IC is the public face of our incident response. It is within the ICs duty to issue periodic updates to the team involved - both customer teams and within Giant Swarm - to act as the bridge between the customer and the team. The IC will need to be in the war rooms of our customers.

If there is a dedicated IC, the IC isn’t debugging systems and keeps the focus on coordinating the team to do so, while managing our customers.

### Operations Engineer

The Operations Engineer (OE) works with the incident coordinator to respond to the incident and is the only one debugging and applying changes to a system.

## P1 Incident Process

The process starts from the well-known [Incident Command System](https://en.wikipedia.org/wiki/Incident_Command_System) used by US firefighters to manage emergency situations. Obviously we have adapted to manage developer platforms. 

Our main tenet is to have a simple process integrated with our incident tooling ([Incident.io](https://incident.io/)) to simplify the life of our engineers. Once a critical incident is declared none wants to read a process but be driving by it. 

The process can be broken down in these steps:

1. [Identify](#identify)
2. [Investigate](#investigate)
3. [Fixing](#fixing)
4. [Monitoring](#monitoring)
5. [Closing up](#closing-up)

### Identify

First step is to identify the incident and understand its impact and severity. In our case, there are three possible sources:

- Alert received pointing to an impacted production system
- Customer sent us an urgent email
- Customer reached out via Slack

Once our engineer acknowledge the message we need to confirm the severity to trigger the P1 process. In case the customer paged us, the Giant Swarm engineer joins the call or thread to verify the severity. In case an alert paged us, the engineer connects to the platform and measure the impact.

Once the criticality is confirmed we continue the workflow by [declaring an Incident](https://help.incident.io/en/articles/5947915-declaring-incidents), which creates a Slack incident channel and triggers a custom [workflow](https://help.incident.io/en/articles/6971329-getting-started-with-workflows) that drives the engineer through the next steps. 

When the incident is created there is some data that the engineer must fill in (short summary, severity and customer impacted). When severity is `Critical` (P1 incident) the first thing to do is building the team. Most of the times the engineer creating the channel is not part of the [Incident Coordinators Group](https://giantswarm.app.opsgenie.com/teams/dashboard/f02504a3-83d4-4ea8-b55c-8c67756f9b2e/main) so he needs to escalate it to get someone from that team. For that reason, when you create an incident channel, incident.io show you a button to escalate. In the end, we need at least two person team to manage a critical incident (communications and operations).

![Incident.io Escalate Screenshot](escalate_screenshot.png)

### Investigate

Once the team is built the person assigned to the Operations Engineer role will carry on with the investigation. The Incident Coordinator will be in contact with the customer, via messaging or in a call, and will provide information to the Operator to help with the investigation.

We leave space to the Operations Engineers to focus on the investigation but we establish 20 minutes periods to get back and inform the customer on the state. Most of the time the OEs will share the findings in the channel and the IC can pin those messages to help tracking the actions performed.

In case the Incident Coordinator needs to increase the number of responders, they can always escalate to more members of the large team using incident.io.

### Fixing

After we have found the root cause of the problem we implement a solution to avoid any more downtime for the customer service. Most of the time, the solution is temporary and will be replaced once the actual fix is rolled out to the platform. 

### Monitoring

Once the fix or workaround has been implemented, we communicate with the customer and move to a monitoring phase, where we stay in stand-by keeping an eye on the metrics and communication channel to confirm there is no regression. We leave the incident in this state for some time, which could be a day or two, till we agree with the customer there is no regression.  

### Closing up

When we close the incident the work is not yet finished. We write down a [PostMortem](https://docs.giantswarm.io/support/overview/#postmortem-process) document to detail all information collected through the incident and share with the customer. We usually create follow ups that convert in tickets to our product teams so we can improve our service and avoid same mistake twice.

## More info

- This process takes inspiration from [Incident Coordinator role](https://en.wikipedia.org/wiki/Incident_commander).
- Incident.io [shortcut cheatsheet](https://help.incident.io/en/articles/5948163-shortcuts-cheatsheet)

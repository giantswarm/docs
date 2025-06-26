---
title: Friendly display of annotations
linkTitle: Annotations
description: You can customize which annotations get displayed in the developer portal, and how they appear in the portal user interface.
weight: 40
menu:
  principal:
    parent: overview-developer-portal-customizing
    identifier: overview-developer-portal-customizing-annotations
last_review_date: 2025-06-24
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
user_questions:
  - How can I configure and customize the display of annotations in the developer portal?
---

The use of [labels]({{< relref "/overview/developer-portal/customizing/labels" >}}) and annotations on Kubernetes resources like Cluster API clusters is highly individual. With the Giant Swarm developer portal, you can configure which annotations get displayed by default as _friendly annotations_, and how they get displayed. You can customize:

- Order of annotations displayed
- Text displayed for the annotation key

The configuration works mostly like the configuration for [friendly labels]({{< relref "/overview/developer-portal/customizing/labels" >}}), with the difference that you cannot configure the color of annotations.

You customize annotations via the Backstage app configuration. Giant Swarm staff will assist you with the implementation.

## Example {#example1}

Let's start with an example. The following YAML snippet shows a valid configuration block a Giant Swarm customer may use.

```yaml
gs:
  friendlyAnnotations:
    - selector: giantswarm.io/last-known-cluster-upgrade-timestamp
      key: Last cluster upgrade
    - selector: giantswarm.io/cluster-upgrading:true
      key: Cluster is upgrading
      valueMap:
        true: "Yes"
```

The result of this configuration would be:

- If the `giantswarm.io/last-known-cluster-upgrade-timestamp` annotation is present, it will be displayed first as "Last cluster upgrade" with the timestamp value.
- If the `giantswarm.io/cluster-upgrading` annotation is present with the value `true`, it will be displayed as "Cluster is upgrading" with the value "Yes".

## Order

The `gs.friendlyAnnotations` configuration item is an array. The order of annotations displayed depends on the order of the according annotation's configuration. To have a certain annotation displayed first, bring its configuration to the top of the array.

## Label key and value matching

The `selector` directive specifies the annotation to apply to. The [example](#example1) shows how the configuration matches an exact annotation key. You can make the matching more general by using wildcards or make it more specific by including certain annotation values.

### Wildcards

Using the asterisk `*` as a wildcard, the `selector` directive supports matching a group of annotations. Here we provide an example that would result in displaying all annotations that start with `giantswarm.io/`:

```yaml
gs:
  friendlyAnnotations:
    - selector: giantswarm.io/*
```

You can use the wildcard several times within one `selector` directive. It matches any character, even an empty string. For example, the pattern `*kubernetes.io/*` would also match a label key `kubernetes.io/foo`.

### Value matching

To apply a display configuration to an annotation with a specific value, use the `selector` directive with a combination of key and value. Use the colon `:` sign as a separator.

**Note:** You cannot combine value matching with wildcard use.

## Text displayed

You can customize both the annotation's key and the value that appears in the user interface. In our [example](#example1), we already show how to configure the annotaition's display name using the `key` directive.

To specify the annotation name shown, use the `key` directive. For specifying the values to display, use the `valueMap` directive. You can use each independently. However, here is an example combining both:

```yaml
gs:
  friendlyLabels:
    - selector: 'foo.io/network-policy'
      key: Network policy
      valueMap:
        private-sstrict: Private-strict (no egress nor ingress)
        private: Private (no ingress)
        public: Public (public ingress)
```

For an annotation like `foo.io/network-policy: private`, the user interface will display the following:

- **Network policy**: Private (no ingress)

## Related

- [Friendly display of labels]({{< relref "/overview/developer-portal/customizing/labels" >}})

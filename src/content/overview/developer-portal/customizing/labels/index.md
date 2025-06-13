---
title: Friendly display of labels
linkTitle: Labels
description: The developer portal allows to customize which labels get displayed as friendly labels, and how they are displayed.
weight: 30
menu:
  principal:
    parent: overview-developer-portal-customizing
    identifier: overview-developer-portal-customizing-labels
last_review_date: 2025-06-12
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
user_questions:
  - How can I configure and customize the display of labels in the developer portal?
---

The use of labels on Kubernetes resources like Cluster API clusters is highly individual. With the developer portal, Giant Swarm allows to configure which labels get displayed by default as _friendly labels_, and how they get displayed. You can customize:

- Order of labels displayed
- Text displayed for the key and for values
- Color, either independent of the value, or depending on the value

Currently, the display of labels is limited to clusters only. In the future, this will be expanded to other resource types.

All customization applies as long as the user has the _friendly labels_ toggle set to active. Once this is deactivated, all labels are displayed without any customization.

The customization is done in the Backstage app configuration. Giant Swarm staff will assist you with the implementation.

## Example {#example1}

Let's start with an example. The following YAML snippet shows a valid configuration block a Giant Swarm customer may use.

```yaml
gs:
  friendlyLabels:
    - label: app.kubernetes.io/version
      key: App version
      variant: blue
    - label: app.kubernetes.io/name
      key: App name
      variant: blue
```

In the user interface, in the context of a cluster, the labels may appear like this:

![Screenshot shows two labels with a blue background, one "App version" and one "App name"](./screenshot_ex1.png)

## Order

The `gs.friendlyLabels` configuration item is an array. The order of labels displayed depends on the order of the according label's configuration. In order to have a certain label displayed first, bring it's configuration to the top of the array.

In the [example](#example1) above, the order of the two configuration items reverses the order that would otherwise be alphabetical.

## Label key and value matching

The `label` directive specifies the label to apply to. The [example](#example1) above shows how the configuration matches an exact label key. However, the matching can also be made more general, by the use of wildcards. And it can be made even more specific, by including certain label values.

### Wildcards

Using the asterisk `*` as a wildcard, the `label` directive supports matching a group of labels. Here we provide an example that would result in coloring pink all labels that contain `kubernetes.io/` in the key:

```yaml
gs:
  friendlyLabels:
    - label: '*kubernetes.io/*'
      variant: pink
```

The wildcard can be used several times. It matches any character, even an empty string. For example, the pattern `*kubernetes.io/*` would also match a label key `kubernetes.io/foo`.

### Value matching

To apply a display configuration to a label only in case it bears a certain value, the `label` directive must be used with a combination of key and value, separated by the colon `:` sign. Example:

```yaml
gs:
  friendlyLabels:
    - label: 'giantswarm.io/service-priority:highest'
      variant: red
    - label: 'giantswarm.io/service-priority:medium'
      variant: orange
```

The above configuration will color the `giantswarm.io/service-priority` label red if the value is `highest` and orange if the value is `medium`.

**Note:** Value matching cannot be combined with wildcard use.

## Text displayed

Both the label's key and the value displayed can be customized. In the [example](#example1) above, the label's display key is configured using the `key` directive.

To specify the label name shown, use the `key` directive. For specifying the values to display, the `valueMap` directive is used. Here is an example combining both:

```yaml
gs:
  friendlyLabels:
    - label: 'foo.io/env'
      key: Environment
      valueMap:
        DEV: Development
        PROD: Production
        STG: Staging
```

For a label like `foo.io/env=PROD`, the following would be displayed:

![Screenshot shows a label where display name and value have been overwritten](./screenshot_valuemap.png)

## Color

Labels can be highlighted in one of nine colors, to make it easier to spot them among others. The directive to use here is `variant`. The available color values are:

- `blue`
- `brown`
- `green`
- `orange`
- `pink`
- `purple`
- `red`
- `teal`
- `yellow`

The actual color value displayed depends on the theme (light or dark) selected and is optimized for contrast in comparison to the displayed text.

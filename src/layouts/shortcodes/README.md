# Shortcodes

These shortcodes allow the use of a string in any number of places in the docs,
while maintaining it only in one place.

The goal here is to give users accurate, complete and up-to-date information.

## Usage

A shortcode can only be placed in *Markdown* text. The file name (without
`.html` suffix) is used as a placeholder, wrapped in a certain way, like
`{{% placeholder %}}`.

For example, to place the shortcode from `first_aws_autoscaling_version.html`,
the content would look like this

```markdown
... since version {{% first_aws_autoscaling_version %}} and ...
```

and would get rendered like

```nohighlight
... since version 6.3.0 ...
```

## List of shortcodes and explanation

- `autoscaler_utilization_threshold`: Utilization threshold for the kubernetes
autoscaler, including percent unit, as we configure it by default. Below this
utilization, the autoscaler will consider a node underused and will scale down.

- `default_aws_instance_type`: The AWS EC2 instance type we use by default for
worker nodes.

- `default_cluster_size_worker_nodes`: The default number of worker nodes we
use when a cluster is created without specifying a number.

- `first_aws_autoscaling_version`: The release version that introduced
autoscaling for AWS.

- `minimal_supported_cluster_size_worker_nodes`: The minimum number of worker
nodes a cluster must have in order to be supported by Giant Swarm.

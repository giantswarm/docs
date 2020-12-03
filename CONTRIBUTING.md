# Giant Swarm docs contribution guidelines

**We welcome any contributions on content to this repository in the form of pull requests!**

Please review these contribution guidelines to ease getting your changes into this repository.

## Style

Some general guidelines to know about when editing or reviewing content.

### Acronyms and abbreviations

**Guideline:** avoid acronyms and abbreviations where possible.

Use them only where the acronym is easier to understand than the long form.

Example: `SSH` is very common, `secure shell` is not widely understood and ambiguous.

**Guideline:** When using an acronym/abbreviation, please use the long form first and then the acronym form in parantheses, to introduce the acronym.

Example:

> The Ingress Controller (IC) manages incoming traffic to your services.

After that, you can use the acronym without the long form and without parantheses.

### Headline title case

We use [Title Case](https://titlecase.com/) only for the main article headline, but not for lower level headlines.

### Code blocks and syntax highlighting

**Guideline:** For code blocks, we give language hints to ensure proper syntax highlighting.

A YAML block, for example, is opened with triple back-ticks followed by `yaml`:

    ```yaml
    foo: bar
    ```

**Guideline:** shell commands and their output get the fake hint `nohighlight` to prevent any funky syntax highlighting.

Shell commands in code blocks are prepended with a `$ ` (dollar sign and one blank character).

Example:

    ```nohighlight
    $ gsctl --version
    Version:      0.26.0 - https://github.com/giantswarm/gsctl/releases/tag/0.26.0
    Build date:   2020-11-18T08:48:37Z
    Commit hash:  5c7820239fc68fc9552eb2751ca3c3ceda47001c - https://github.com...
    ```

### CLI commands

**Guideline:** Were a CLI provides both long and short form flags, we use the long form for clarity.

**Guideline:** We avoid the equal sign between flag name and value where possible.

Good example:

```nohighlight
gsctl create cluster --owner acme
```

Bad examples:

```nohighlight
gsctl create cluster --owner=acme
gsctl create cluster -o=acme
gsctl create cluster -o acme
```

**Guideline:** We break a command into multiple lines once it becomes longer than ~ 60 characters,
using the backslash character. This makes it easier to read.

Example:

```nohighlight
gsctl create cluster \
  --owner acme \
  --create-default-nodepool false
```

### Linting and validation

Many style rules are checked automatically in CI. You can also execute the check locally
before pushing commits using the `make lint` command.

For a reference of all rules please check the [DavidAnson/markdownlint documentation](https://github.com/DavidAnson/markdownlint/blob/master/doc/Rules.md).

There is a project specific configuration in place via the `.markdownlint.yaml` file.

To check locally whether all internal links are correct, use `make linkcheck`.

To check both internal and external links, use `make linkcheck-external`.

## Solutions for specific problems

### Kubernetes API versions

Keep an eye on API versions of Kubernetes resources.

**Guideline:** Examples and references should cover all possible API versions of Kubernetes versions we provide to our customers.

**Guideline:** If possible, use the latest API version supported by Kubernetes.

**Guideline:** If different Kubernetes versions require different API versions, we offer multiple examples and explain which Kubernetes version requires which API version.

An example for this would be the deprecation of the API version of Ingress resources from `networking.k8s.io/v1beta1` to `networking.k8s.io/v1` in Kubernetes 1.19.

## Editing content

Edit existing content in the `src/content` folder.

### Front matter

Each documentation page consists of a Markdown file that starts with some metadata called [front matter](https://gohugo.io/content-management/front-matter/). Some hints:

- Please look at the other pages to get an idea of what the front matter is good for.
- Please double-check whether the `description` is still up-to-date or could be improved. It will often show up Google search results.

Special front matter fields we use:

- `last_review_date`: Date of the last time somebody checked the entire page for validity.
- `user_questions`: List of questions this article answers. Written from a user's perspective. E. g. _How do I ..._.

### Hyperlinks

In order to link to other docs pages, please use this format only:

```markdown
... see the [gsctl reference](/reference/gsctl/) for details. ...
```

Note that

- Hyperlinks URLs must start with `/`
- Must usually end with `/`
- Must not contain `https://` or the host name `docs.giantswarm.io`.

This is important to support automation when links have to change, or when checking links.

### Table of contents and headline anchors

The rendered documentation pages will have a table of contents on the left hand side and an anchor for every intermediate headline. This anchor is normally generated from the headline's content. For example, a headline

```markdown
### Another section with more content
```

will result in a headline

```html
<h3 id="another-section-with-more-content">Another section with more content</h3>
```

This means that anchors and URLs can become quite long. It also means that when the headline text changes, all links to this headline also have to be updated.

To control this behavior, the anchor ID can be edited as a suffix to the markdown headline, like in the following example:

```markdown
### Another section with more content {#more}
```

will result in a headline

```html
<h3 id="more">Another section with more content</h3>
```

### Shortcodes

Shortcodes allow the use of a string in any number of places in the docs,
while maintaining it only in one place. We use these to place, for example,
configuration details.

The goal here is to give users accurate, complete and up-to-date information.

Shortcodes exist as one file each in the folder [src/layouts/shortcodes](https://github.com/giantswarm/docs/tree/master/src/layouts/shortcodes).

#### Usage

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

#### List of shortcodes with explanation

- `autoscaler_utilization_threshold`: Utilization threshold for the kubernetes
autoscaler, including percent unit, as we configure it by default. Below this
utilization, the autoscaler will consider a node underused and will scale down.

- `default_aws_instance_type`: The AWS EC2 instance type we use by default for
worker nodes.

- `default_cluster_size_worker_nodes`: The default number of worker nodes we
use when a cluster is created without specifying a number.

- `first_aws_autoscaling_version`: The tenant cluster release version that introduced
autoscaling for AWS.

- `first_aws_nodepools_version`: The tenant cluster release version that introduced
nodepools for AWS.

- `first_azure_nodepools_version`: The tenant cluster release version that introduced nodepools for Azure.

- `first_spotinstances_version`: The tenant cluster release version that introduced
spotinstances for AWS.

- `minimal_supported_cluster_size_worker_nodes`: The minimum number of worker
nodes a cluster must have in order to be supported by Giant Swarm.

### Iterating on content locally

If you want to iterate quickly on some content you can use the `make dev`
command.

You can access the server at http://localhost:1313/. The server can be stopped by hitting `Ctrl + C`.

It will not include content from the external repositories.

### Previewing changes {#previewing}

You can bring up the final site using the following commands:

```nohighlight
make docker-build
docker-compose up
```

You can access the server at http://localhost:8080/. The server can be stopped by hitting `Ctrl + C`.

### Content from external sources

The build process of this repo (see the `build` target in the `Makefile`) ties in content from several sources:

- Changes and Releases (see scritps/aggregate-changelogs)
- Guides or recipes from external repositories
- Custom Resource Definitions from [apiextensions](https://github.com/giantswarm/apiextensions)

To trigger the build and fetching external content locally, run `make`.

## Contributing

This repository is public to facilitate content quality and encourage contributions. We appreciate all contributions, including corrections and suggestions for improvement.

The best way to contribute changes are pull requests. Please note the following regarding pull requests:

- Please make one pull request per topic/issue. Avoid putting several non-related issues in a single pull request!

- When creating a pull request, please remember you accept that your contribution will be published under the Creative Commons referenced below. Giant Swarm will be able to use your content without restriction.   Giant Swarm is not obliged to list you as the author of your contribution, but will attempt to do so where possible.

# Giant Swarm User Documentation

This is the main documentation repository for the documentation available at https://docs.giantswarm.io.

## Repository overview

This repository named `docs` holds the main **content** of our documentation. The documentation
site is created using the static site generator [HUGO](http://gohugo.io/) based on Markdown files
in the `src/content/` directory. Images are in the `src/static/img/` directory.

Additional content repositories are tied in through the file `src/external-repositories.txt`.

**We welcome any contributions on content to this repository in the form of pull requests!**

The `src/` directory also contains HTML templates and the HUGO site configuration.

The build process here in the `Makefile` and the `Dockerfile` pull together the content
from this and the external repositories, and create a Docker container serving a the
documentation website.

There are several additional repositories which provide additional functionality:

- [docs-proxy](https://github.com/giantswarm/docs-proxy/): nginx proxy server which integrates the search engine and the API spec (see below) into the documentation site, and provides some additional configuration, e. g. regarding HTTP headers.

- [api-spec](https://github.com/giantswarm/api-spec/): Specification (in Swagger/OpenAPI) format for the Giant Swarm API. Available in the docs site under https://docs.giantswarm.io/api/.

- [sitesearch](https://github.com/giantswarm/sitesearch/): Search engine for the documentation site.

- [indexer](https://github.com/giantswarm/docs-indexer/): Indexing tool that pushes new content to the `sitesearch` index periodically, to keep the search engine up-to-date.

## Editing content

Edit existing content in the `src/content` folder or in the external repositories (see `src/external-repositories.txt`).

### Front matter

Each documentation page consists of a Markdown file that starts with some metadata called [front matter](https://gohugo.io/content-management/front-matter/). Some hints:

- Please look at the other pages to get an idea of what the front matter is good for.

- Please always update the last modification date of the page when you change content.

- Please double-check whether the page description is still up-to-date or could be improved.

### Code blocks

We support fenced code blocks wrapped by the triple backtick operator. It is recommended to
also declare the language a code snippet uses, to prevent faulty guessing. Example:

    ```json
    {"message": "this is JSON"}
    ```

Shell snippets (commands and their output) should in generall prevent highlighting like this:

    ```nohighlight
    $ ls
    bar    foo
    ```

### Table of contents and headline anchors

The rendered documentation pages will have a table of contents on the top left and an achor for every intermediate headline. This anchor is normally generated from the headline's content. For example, a headline

    ### Another section with more content

will result in a headline

    <h3 id="another-section-with-more-content">Another section with more content</h3>

This means that anchors and URLs can become quite long. It also means that when the healine text changes, all links to this headline also have to be updated.

To control this behaviour, the anchor ID can be edited as a suffix to the markdown headline, like in the following example:

    ### Another section with more content {#more}

will result in a headline

    <h3 id="more">Another section with more content</h3>

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

- `first_aws_autoscaling_version`: The release version that introduced
autoscaling for AWS.

- `minimal_supported_cluster_size_worker_nodes`: The minimum number of worker
nodes a cluster must have in order to be supported by Giant Swarm.


### Previewing changes

You can bring up the site using the following commands:

```nohighlight
make docker-build
make docker-run
```

You can access the server at http://localhost:8080/. The server can be stopped by hitting `Ctrl + C`.

To run the site locally together with search (sitesearch) and API docs (api-spec), you can use the docker-compose setup provided in the file `docker-compose.yaml`.

## Contributing

This repository is public to facilitate content quality and encourage contributions. We appreciate all contributions, including corrections and suggestions for improvement.

The best way to contribute changes are pull requests. Please note the following regarding pull requests:

- Please make one pull request per topic/issue. Avoid putting several non-related issues in a single pull request!

- When creating a pull request, please remember you accept that your contribution will be published under the Creative Commons referenced below. Giant Swarm will be able to use your content without restriction.   Giant Swarm is not obliged to list you as the author of your contribution, but will attempt to do so where possible.

## Style

### Using acronyms

Please avoid acronyms and abbreviations where possible, use them only where the acronym is easier to understand than the long form (example: `SSH` is self-explanatory, `secure shell` is not widely understood).

When you want to use an acronym, please use the long form and the aronym form together at the first use on a page. Example:

> The Ingress Controller (IC) manages incoming traffic to your services.

After that, you can use the acronym without the long form.

### Headline title case

We use [Title Case](https://titlecase.com/) for the main article headline, but not for lower level headlines.

### Code blocks and syntax highlighting

For **code blocks**, we give language hints to ensure proper syntax highlighting. A YAML block, for example, is opened with triple backticks followed by `yaml`.

However, shell commands and their output get the fake hint `nohighlight` to prevent any funky syntax highlighting.

Shell commands in code blocks are prepended with a `$ ` (dollar sign and one blank character).

### CLI commands

We use long-form CLI flags and avoid the possible equal sign between flag name and value, for best readability.

Right:

```nohighlight
$ gsctl create cluster --owner acme
```

Wrong:

```nohighlight
$ gsctl create cluster --owner=acme
$ gsctl create cluster -o=acme
$ gsctl create cluster -o acme
```

## License

The content in this repository is licensed under the [Creative Commons Attribution ShareAlike](http://creativecommons.org/licenses/by-sa/4.0/) license.

For attribution, please use either:

- Giant Swarm
- giantswarm.io

and link, if possible, to https://giantswarm.io

## Deploying

With every push to `master`, the latest content is automatically published. See `.circleci/config.yml` and `helm/` for details.


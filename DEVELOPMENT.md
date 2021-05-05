# Developing on the docs

## Repository overview

This repository named `docs` holds the main **content** of our documentation. The documentation
site is created using the static site generator [HUGO](http://gohugo.io/) based on Markdown files
in the `src/content/` directory.

Additional content is tied in through the scripts

- `scripts/aggregate-changelogs`: Aggregates changelog entries into the `src/content/changes` destination.
- `scripts/update-crd-reference`: Generates reference pages for our custom resource definitions in the `src/content/reference/management-api` destination.
- `scripts/update-external-repos`: Tutorials that need their own code repository. They must have a `docs` subfolder with the Markdown content and optionally some images. Configuration is found in `scripts/update-external-repos/repositories.txt`.

To update these external content types, the `Makefile` provides specific targets:

- `make changes`
- `make update-external-repos`
- `make update-crd-reference`

## Related repositories and components

There are several additional repositories which provide additional functionality:

- [docs-proxy](https://github.com/giantswarm/docs-proxy/): nginx proxy server which integrates the search engine and the API spec (see below) into the documentation site, and provides some additional configuration, e. g. regarding HTTP headers.

- [api-spec](https://github.com/giantswarm/api-spec/): Specification (in Swagger/OpenAPI) format for the Giant Swarm REST API. Available in the docs site under https://docs.giantswarm.io/api/.

- [sitesearch](https://github.com/giantswarm/sitesearch/): Search engine for the documentation site.

- [indexer](https://github.com/giantswarm/docs-indexer/): Indexing tool that pushes new content to the `sitesearch` index periodically, to keep the search engine up-to-date.

## Iterating on content locally

TODO: Probably won't work currently. Use `brew install hugo` and `hugo server -s src` instead.

If you want to iterate quickly on some content you can use the `make dev`
command.

You can access the server at http://localhost:1313/. The server can be stopped by hitting `Ctrl + C`.

It will not include content from the external repositories.

### Previewing changes

You can bring up the final site using the following commands:

```nohighlight
make docker-build
docker-compose up
```

You can access the server at http://localhost:8080/. The server can be stopped by hitting `Ctrl + C`.

## Shortcodes

Shortcodes allow the use of a string in any number of places in the docs,
while maintaining it only in one place. We use these to place, for example,
configuration details.

The goal here is to give users accurate, complete and up-to-date information.

Shortcodes exist as one file each in the folder [src/layouts/shortcodes](https://github.com/giantswarm/docs/tree/master/src/layouts/shortcodes).

### Usage

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

### List of shortcodes with explanation

- `platform_support_table`: A table that displays information regarding which
providers support a feature described in the context. Look for examples in the
code base too, to understand how it is configured. The shortcode offers three
parameters `aws`, `azure`, and `kvm`. Each one functions the same way:

    - Multiple key-value-pairs can be set, separated by comma. Example: `alpha=v10.0.0,beta=v11.0.0,ga=v12.0.0`.

    - Key-value-pairs use the `=` character to separate key and value.

    - The key must be either `alpha`, `beta`, `ga`, or `roadmap`, with a meaning as follows.

        - `alpha`: Version that made the feature available in an Alpha stage. If no value/version is given, it means that the feature is currently in the Alpha stage.

        - `beta`: Version that made the feature available in a beta stage. If no value/version is given, it means that the feature is currently in the Beta stage.

        - `ga`: Version that made the feature GA (general availability). If no value/version is given, it means that the feature is currently in the GA stage.

        - `roadmap`: The feature is on our roadmap for the given provider. The value muest be the roadmap issue URL.

    - For the keys `alpha`, `beta`, and `ga` the (optional) value is expected to be a semver version number of the workload cluster release. For example, `beta=v10.0.0` indicates that the feature was published in Beta in release v10.0.0. If only the key is present, but no value, this indicates that the version number is unknown.

    - For the `roadmap` key, a value must be given, and the value must be the `https://github.com/giantswarm/roadmap` issue URL about the feature.

- `autoscaler_utilization_threshold`: Utilization threshold for the kubernetes
autoscaler, including percent unit, as we configure it by default. Below this
utilization, the autoscaler will consider a node underused and will scale down.

- `default_aws_instance_type`: The AWS EC2 instance type we use by default for
worker nodes.

- `default_cluster_size_worker_nodes`: The default number of worker nodes we
use when a cluster is created without specifying a number.

- `first_aws_autoscaling_version`: The workload cluster release version that introduced
autoscaling for AWS.

- `first_aws_nodepools_version`: The workload cluster release version that introduced
nodepools for AWS.

- `first_azure_nodepools_version`: The workload cluster release version that introduced nodepools for Azure.

- `first_spotinstances_version`: The workload cluster release version that introduced
spotinstances for AWS.

- `minimal_supported_cluster_size_worker_nodes`: The minimum number of worker
nodes a cluster must have in order to be supported by Giant Swarm.

## About the Header and Footer

The header and footer are to be kept in sync with www.giantswarm.io
In order to do this we copy the HTML and CSS specific to those parts of the page.

Fully automating this is a goal, but for now check out the Makefile target
called `grab-main-site-header-footer` for one idea of how to grab the header and
footer using curl.

Copying just the CSS styles that apply to the header and footer is a bit trickier.
Oliver Ponder has some loosely arranged scripts that can be used to help automate this
in the future.

Files starting with `gs_` are involved in making the header and footer appear
and behave correctly.

`partials/gs_header.html` - The unedited html of the header at www.giantswarm.io

`partials/gs_mobile_menu.html` - The unedited html of the mobile navigation menu at www.giantswarm.io

`partials/gs_footer.html` - The unedited html of the footer at www.giantswarm.io

`partials/gs_styles.html` - Automatically extracted styles which apply to
                            elements found in the header and footer, as well
                            as hand written override styles to make it play nicely
                            with CSS already present in docs.

`scripts/gs_menu.js`      - Hand written javascript that recreates the interactive
                            functionality of the navigation menus.


## Deploying

To publish the content in this repository, a release is needed. Releases are created automatically for every push to the `master` branch, so normally whenever a pull request gets merged. [app-updater](https://github.com/giantswarm/app-updater) then updates the `docs-app` app CR in the `c68pn` namespace.

You can also publish manually with this command:

```nohighlight
kubectl --context giantswarm-gollum -n c68pn patch app docs-app --type merge -p '{"spec": {"version": "X.Y.Z"}}'
```

Here, `giantswarm-gollum` is the kubeconfig context created by `opsctl create kubeconfig -i gollum`. `X.Y.Z` is to be replaced by the new version number of the app, without `v` prefix.

Latest content should be visible after a short period. When checking, make sure to circumvent any browser cache. For example, do this by keeping the Shift key pressed while hitting the reload button of your browser.

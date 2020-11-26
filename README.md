# Giant Swarm User Documentation

This is the main documentation repository for the documentation available at https://docs.giantswarm.io.

## Repository overview

This repository named `docs` holds the main **content** of our documentation. The documentation
site is created using the static site generator [HUGO](http://gohugo.io/) based on Markdown files
in the `src/content/` directory. Images are in the `src/static/img/` directory.

Additional content repositories are tied in through the file `src/external-repositories.txt`.

The `src/` directory also contains HTML templates and the HUGO site configuration.

The build process here in the `Makefile` and the `Dockerfile` pull together the content
from this and the external repositories, and create a Docker container serving a the
documentation website.

There are several additional repositories which provide additional functionality:

- [docs-proxy](https://github.com/giantswarm/docs-proxy/): nginx proxy server which integrates the search engine and the API spec (see below) into the documentation site, and provides some additional configuration, e. g. regarding HTTP headers.

- [api-spec](https://github.com/giantswarm/api-spec/): Specification (in Swagger/OpenAPI) format for the Giant Swarm API. Available in the docs site under https://docs.giantswarm.io/api/.

- [sitesearch](https://github.com/giantswarm/sitesearch/): Search engine for the documentation site.

- [indexer](https://github.com/giantswarm/docs-indexer/): Indexing tool that pushes new content to the `sitesearch` index periodically, to keep the search engine up-to-date.


**We welcome any contributions on content to this repository in the form of pull requests!**

Please review the [Contribution guidelines](CONTRIBUTING.md) to ease getting your changes into this repository.

## License

The content in this repository is licensed under the [Creative Commons Attribution ShareAlike](http://creativecommons.org/licenses/by-sa/4.0/) license.

For attribution, please use either:

- Giant Swarm
- giantswarm.io

and link, if possible, to https://giantswarm.io

## Deploying

To publish the content in this repository:

1. Create a new [release](https://github.com/giantswarm/docs/releases). When in doubt, bump the patch version. This will trigger the creation of a new version of the `docs-app` via CI.
2. Watch the appearance of the new release of `docs-app` in the [giantswarm-operations-platform-catalog](https://github.com/giantswarm/giantswarm-operations-platform-catalog/commits/master) catalog.
3. Update the version of App `docs-app` in `gollum` in namespace `c68pn`. You can use this command:

```nohighlight
kubectl --context giantswarm-gollum -n c68pn patch app docs-app --type merge -p '{"spec": {"version": "X.Y.Z"}}'
```

Here, `giantswarm-gollum` is the kubeconfig context created by `opsctl create kubeconfig -i gollum`. `X.Y.Z` is to be replaced by the new version number of the app, without `v` prefix.

Latest content should be visible after a short period. When checking, make sure to circumvent any browser cache. For example, do this by keeping the Shift key pressed while hitting the reload button of your browser.

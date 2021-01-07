# Giant Swarm User Documentation

This is the main documentation repository for the documentation available at https://docs.giantswarm.io.

## Repository overview

This repository named `docs` holds the main **content** of our documentation. The documentation
site is created using the static site generator [HUGO](http://gohugo.io/) based on Markdown files
in the `src/content/` directory. Images are in the `src/static/img/` directory.

Additional content is tied in through the scripts

- `scripts/aggregate-changelogs`: Aggregates changelog entries into the `src/content/changes` destination.
- `scripts/update-crd-reference`: Generates reference pages for our custom resource definitions in the `src/content/reference/management-cluster-api` destination.
- `scripts/update-external-repos`: Tutorials that need their own code repository. They must have a `docs` subfolder with the Markdown content and optionally some images. Configuration is found in `scripts/update-external-repos/repositories.txt`.

To update these external content types, the `Makefile` provides specific targets:

- `make changes`
- `make update-external-repos`
- `make update-crd-reference`

## Related repositories and components

There are several additional repositories which provide additional functionality:

- [docs-proxy](https://github.com/giantswarm/docs-proxy/): nginx proxy server which integrates the search engine and the API spec (see below) into the documentation site, and provides some additional configuration, e. g. regarding HTTP headers.

- [api-spec](https://github.com/giantswarm/api-spec/): Specification (in Swagger/OpenAPI) format for the Giant Swarm API. Available in the docs site under https://docs.giantswarm.io/api/.

- [sitesearch](https://github.com/giantswarm/sitesearch/): Search engine for the documentation site.

- [indexer](https://github.com/giantswarm/docs-indexer/): Indexing tool that pushes new content to the `sitesearch` index periodically, to keep the search engine up-to-date.

## Contributing

**We welcome any contributions on content to this repository in the form of pull requests!**

Please review the [Contribution guidelines](CONTRIBUTING.md) to ease getting your changes into this repository.

## License

The content in this repository is licensed under the [Creative Commons Attribution ShareAlike](http://creativecommons.org/licenses/by-sa/4.0/) license.

For attribution, please use either:

- Giant Swarm
- giantswarm.io

and link, if possible, to https://www.giantswarm.io/

## Deploying

To publish the content in this repository, a release is needed. Releases are created automatically for every push to the `master` branch, so normally whenever a pull request gets merged.

To publish the release, update the version of App `docs-app` in `gollum` in namespace `c68pn`. You can use this command:

```nohighlight
kubectl --context giantswarm-gollum -n c68pn patch app docs-app --type merge -p '{"spec": {"version": "X.Y.Z"}}'
```

Here, `giantswarm-gollum` is the kubeconfig context created by `opsctl create kubeconfig -i gollum`. `X.Y.Z` is to be replaced by the new version number of the app, without `v` prefix.

Latest content should be visible after a short period. When checking, make sure to circumvent any browser cache. For example, do this by keeping the Shift key pressed while hitting the reload button of your browser.

TODO: update this section as soon as app-updater is working.

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





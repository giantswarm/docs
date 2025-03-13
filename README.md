# Giant Swarm user documentation

This is the main documentation repository for the documentation available at https://docs.giantswarm.io.

## Repository overview

It holds the main **content** of our documentation. The documentation site is created using the static site generator [HUGO](http://gohugo.io/) based on markdown files in the `src/content/` directory of the `docs` repository.

Additional content is tied in through the scripts

- `scripts/aggregate-changelogs`: Aggregates changelog entries into the `src/content/changes` destination.
- `scripts/collect-changelog-entries`: Collects changelog entries from all apps defined in `giantswarm/github` repository to create a weekly update.
- `scripts/update-crd-reference`: Generates reference pages for our custom resource definitions in the `src/content/reference/platform-api` destination.
- `scripts/update-external-repos`: Tutorials that need their own code repository. They must have a `docs` subfolder with the Markdown content and optionally some images. Configuration is found in `scripts/update-external-repos/repositories.txt`.
- `scripts/update-helm-chart-reference`: Creates the cluster apps pages in the `src/content/reference/platform-api` destination.

To update these external content types, the `Makefile` provides specific targets:

- `make changes`
- `make update-external-repos`
- `make collect-changelog-entries`
- `make update-cluster-app-reference`
- `make update-crd-reference`

All pull requests to this repository will trigger a build of the documentation site. The site is hosted in a Cluster API environment (`gazelle`) and it's deployed to https://docs.giantswarm.io automatically thanks to GitOps setup.

## Contributing

**We welcome any contributions on content to this repository in the form of pull requests!**

Please review the [style guidelines](https://handbook.giantswarm.io/docs/content/docs-guide) before contributing.

While making changes, please use

```sh
make dev
```

to render the results. This serves the web content on http://localhost:1313/ by default. Please check if your changes display correctly before opening a pull request.

### Dev container (experimental)

This repository provides a [dev container](https://containers.dev/) configuration. When making changes to documentation content, we encourage you to use the container and give feedback to SIG docs. Prerequisites:

- IDE with dev container support (e.g. Visual Studio Code with the "Dev Containers" (`ms-vscode-remote.remote-containers`) extension.
- Docker
- at least 4 GiB of memory dedicated to Docker

### Front matter

Each documentation page consists of a markdown file that starts with some metadata called [front matter](https://gohugo.io/content-management/front-matter/). Some hints:

- Please look at the other pages to get an idea of what the front matter is good for.
- When your page's `title` is too long for the navigation menu, add a `linkTitle` field with a short title.
- Please double-check whether the `description` is still up-to-date or could be improved. It will often show up Google search results.

Special front matter fields we use:

- `last_review_date`: Date of the last time somebody checked the entire page for validity.
- `menu`: The menu entry under which the page should appear. Currently it's `principal` for the main menu,  vintage documentation is under `main`.
- `owner`: List of GitHub team URLs for the team(s) or SIG(s) owning the page. The owning team/SIG is the one responsible for keeping the content up-to-date and useful.
- `user_questions`: List of questions this article answers. Written from a user's perspective. E. g. _How do I ..._.

## Shortcodes

Shortcodes allow the use of a string in any number of places in the docs, while maintaining it only in one place. We use these to place, for example, configuration details. The goal here is to give users accurate, complete and up-to-date information.

Shortcodes exist as one file each in the folder [src/layouts/shortcodes](https://github.com/giantswarm/docs/tree/master/src/layouts/shortcodes).

A shortcode is used in a markdown file like this:

```markdown
... since version {{/*% first_aws_autoscaling_version */%}} and ...
```

### Content linting

When writing docs content, the linter can help you a great deal to keep the content consistent and clean. You can run the linter with:

```sh
make lint-prose
```

When editing content in Microsoft Visual Studio Code, you can also use the [vale-vscode](https://marketplace.visualstudio.com/items?itemName=ChrisChinchilla.vale-vscode) extension to see errors and editing suggestions while you write.

To keep third party style rules up-to-date, please run `make lint-prose-update` and commit the resulting changes.

## Search

The search functionality works since last Nov 2023 using a third-party system called [`Inkeep`](https://inkeep.com/) which makes use of Artificial Intelligence to index all the content of our docs and serve good results. Also, it allows to have a conversational interface to get a faster response in our wide documentation hub.

In [the internal portal](https://portal.inkeep.com/) we've defined our docs as main source of content for the Large Language Model(LLM) instance which will be scrapped weekly to digest new content. Access is granted via OIDC and Google.

Since we use `Inkeep` for more uses cases the project for docs is called "Giant Swarm customer facing". There in the integration you can see our docs and the configuration keys needed to bootstrap the widget. The code that triggers the render the widget is in `/src/assets/scripts/base.js` and the styles are part of `/static/css/inkeep.css`. Most of the options for the widget are defaulted and only style has be customized to fit our documentation's layout.

## Diagrams

We use [mermaid](https://mermaid.js.org/) for diagrams. You need to annotate the page previously in the front matter to load the mermaid code (`mermaid: true`). Then you can use the shortcode `{{< mermaid >}}` to add the diagram code.

## About the Header and Footer

The header and footer are to be kept in sync with `www.giantswarm.io`. In order to do this we copy the HTML and CSS specific to those parts of the page.

Files starting with `gs_` are involved in making the header and footer appear and behave correctly.

`partials/gs_header.html` - The unedited html of the header at www.giantswarm.io

`partials/gs_mobile_menu.html` - The unedited html of the mobile navigation menu at www.giantswarm.io

`partials/gs_footer.html` - The unedited html of the footer at www.giantswarm.io

`partials/gs_styles.html` - Automatically extracted styles which apply to
                            elements found in the header and footer, as well
                            as hand written override styles to make it play nicely
                            with CSS already present in docs.

`scripts/gs_menu.js`      - Hand written javascript that recreates the interactive
                            functionality of the navigation menus.

## License

The content in this repository is licensed under the [Creative Commons Attribution ShareAlike](http://creativecommons.org/licenses/by-sa/4.0/) license.

For attribution, please use either:

- Giant Swarm
- giantswarm.io

and link, if possible, to https://www.giantswarm.io/

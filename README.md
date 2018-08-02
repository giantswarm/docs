# Giant Swarm User Documentation

This is the main documentation repository for the documentation available at https://docs.giantswarm.io.

## Repository Overview


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

- [docs-proxy](https://github.com/giantswarm/docs-proxy/): nginx proxy server which integratesthe search engine and the API spec (see below) into the documentation site, and provides some additional configuration, e. g. regarding HTTP headers.

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

## License

The content in this repository is licensed under the [Creative Commons Attribution ShareAlike](http://creativecommons.org/licenses/by-sa/4.0/) license.

For attribution, please use either:

- Giant Swarm
- giantswarm.io

and link, if possible, to https://giantswarm.io

## Deploying

With every push to `master`, the latest content is automatically published. See `.circleci/config.yml` and `helm/` for details.


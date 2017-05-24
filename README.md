# docs - User documentation for Giant Swarm

Our Documentation is based on Markdown and HTML content and generated using [HUGO](http://gohugo.io/), a static site generator written in Go.

## Component Overview

![docs component architecture](https://cloud.githubusercontent.com/assets/273727/19264053/8344ef86-8f9f-11e6-9154-e6ee9b8d5668.png)

|Short name    | Docker image            | Source repository                                                      |
|--------------|-------------------------|------------------------------------------------------------------------|
|`content`     | `giantswarm/docs`       | this repository                                                        |
|`docs-proxy`  | `giantswarm/docs-proxy` | [giantswarm/docs-proxy](https://github.com/giantswarm/docs-proxy/)     |
|`sitesearch`  | `giantswarm/sitesearch` | [giantswarm/sitesearch](https://github.com/giantswarm/sitesearch/)     |
|`indexer`     | `giantswarm/indexer`    | [giantswarm/docs-indexer](https://github.com/giantswarm/docs-indexer/) |


## Where's the content?

Content is in this public repo: [giantswarm/docs-content](https://github.com/giantswarm/docs-content), plus in additional external repositories referenced in [docs-content/external-repositories.txt](https://github.com/giantswarm/docs-content/blob/master/external-repositories.txt).

The content is served using the `content` component. It's copied during the build process. Look at the `Makefile` for details.

## Development setup

In short:

```nohighlight
make
docker-compose up
```

Open `http://localhost/`.

The build will clone the [giantswarm/docs-content](https://github.com/giantswarm/docs-content) repository and copy it's content to the correct locations.

## Deploying

With every push to `master`, the latest content is automatically deployed to `docs.giantswarm.io`.

See `circle.yml` and `kubernetes/` for details.

## Maintaining the first generation docs site

The archived documentation at http://firstgen-docs.giantswarm.io is based on this repository, using the protected `firstgen` branch. However there is a separate repo for this, and the hosting is done using github pages.

## About writing for the documentation

There is more information available in the [Wiki](https://git.giantswarm.io/giantswarm/docs/wikis/home).

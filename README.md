# docs - User documentation for Giant Swarm

Our Documentation is based on Markdown and HTML content and generated using [HUGO](http://gohugo.io/), a static site generator written in Go.

## Setup for writing and checking content

In order to contribute content or simply review content, all you need is a local install of HUGO.

On the Mac:

```
brew install hugo
./run-dev.sh
```

(On Linux the process of installing HUGO in the correct version is more involved. Check the Dockerfile for hints.)

Access the site at [localhost:1313](http://localhost:1313/).

Content changes should automatically load in your browser. No manual reloading required.

In order to review a Pull Request, check out the according branch.

## Setup for development

The documentation application consists of several components. The best way to run them all locally is using `fig`. To start the application locally, including proxy and search functions, use

```
fig up
```

Look at the `fig.yml` file for details on what happens here.

## Building Docker images

For testing purposes, the image can be built using `make build`.

For a new production deployment, the latest image is created and pushed using `builder`.

```
builder release <patch|minor|major>
```

## Deploying content updates

1. Create and push a new docs image using builder, as decribed above

2. Stop and start the `content-master` component:

```
SWARM_CLUSTER_ID=cluster-01.giantswarm.io swarm stop swarmdocs/content-master
SWARM_CLUSTER_ID=cluster-01.giantswarm.io swarm start swarmdocs/content-master
```

This will update the search index adn replace the first of the content servers.

3. Stop and start the `content-slave` component:

```
SWARM_CLUSTER_ID=cluster-01.giantswarm.io swarm stop swarmdocs/content-slave
SWARM_CLUSTER_ID=cluster-01.giantswarm.io swarm start swarmdocs/content-slave
```

This will replace the second of the content servers.

## Update CLI download links

There are two files you need to modify to update the download links in the docs:

- [`swarmdocs/layouts/partials/cli_latest_version.html`](/giantswarm/docs/blob/master/swarmdocs/layouts/partials/cli_latest_version.html)
- [`swarmdocs/layouts/shortcodes/cli_latest_version.html`](https://github.com/giantswarm/docs/blob/master/swarmdocs/layouts/shortcodes/cli_latest_version.html)

Please make sure that there is **no white space** in these file.

Having that changed and deployed, users will be able to download the latest tagged CLI version.

## About writing for the documentation

There is more information available in the [Wiki](https://git.giantswarm.io/giantswarm/docs/wikis/home).

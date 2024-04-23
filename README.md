# Giant Swarm user documentation

This is the main documentation repository for the documentation available at https://docs.giantswarm.io.

## Contributing

**We welcome any contributions on content to this repository in the form of pull requests!**

Please review the [Contribution guidelines](CONTRIBUTING.md) for guidelines on suggesting changes and getting them published this repository.

If you are an employee of Giant Swarm you can get more information per [intranet page](https://intranet.giantswarm.io/docs/product/docs/) with info on style and other pre-requisites.

While making changes, please use

```sh
make dev
```

to render the results. This serves the web content on http://localhost:1313/ by default. Please check if your changes display correctly before opening a pull request.

### Content linting

When writing docs content, the linter can help you a great deal to keep the content consistent and clean. You can run the linter with:

```sh
make lint-prose
```

When editing content in Microsoft Visual Studio Code, you can also use the [vale-vscode](https://marketplace.visualstudio.com/items?itemName=ChrisChinchilla.vale-vscode) extension to see errors and editing suggestions while you write.

To keep third party style rules up-to-date, please run `make lint-prose-update` and commit the resulting changes.

## Search

The search functionality works since last Nov 2023 using a third-party system called [Inkeep](https://inkeep.com/) which makes use of Artificial Intelligence to index all the content of our docs and serve good results. Also, it allows to have a conversational interface to get a faster response in our wide documentation hub.

In [the internal portal](https://portal.inkeep.com/) we have defined our docs as main source of content for the Large Language Model(LLM) instance which will be scrapped weekly to digest new content. Access is granted via OIDC and Google.

Since we use Inkeep for more uses cases the project for docs is called "Giant Swarm customer facing". There in the integration you can see our docs and the configuration keys needed to bootstrap the widget. The code that triggers the render the widget is in `/src/assets/scripts/base.js` and the styles are part of `/static/css/inkeep.css`. Most of the options for the widget are defaulted and only style has be customized to fit our docs's layout.

## Diagrams

We use [mermaid](https://mermaid.js.org/) for diagrams. You need to annotate the page previously in the frontmatter to load the mermaid code (`mermaid: true`). Then you can use the shortcode `{{< mermaid >}}` to add the diagram code.

## License

The content in this repository is licensed under the [Creative Commons Attribution ShareAlike](http://creativecommons.org/licenses/by-sa/4.0/) license.

For attribution, please use either:

- Giant Swarm
- giantswarm.io

and link, if possible, to https://www.giantswarm.io/

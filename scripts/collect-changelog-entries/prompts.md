# Prompt to enhance the highlights

Please rewrite these changelog entries in the attached file grouping the projects within this categories: Fleet Management, Security, Connectivity, Continuous Deployment, Developer Portal and Observability.

Make the messages more towards to the end customer, removing repeated content or unimportant entries. Make sure the link of the version compares from the previous versions to the current one.

Only keep the link to the latest Github release version though you should list all important changes through all changes in the project.

Example input
```
- [aws-ebs-csi-driver-app](https://github.com/giantswarm/aws-ebs-csi-driver-app)
  - [3.0.3](https://github.com/giantswarm/aws-ebs-csi-driver-
app/compare/v3.0.2...v3.0.3)
      * Chart: Sync to upstream. ([#255](https://github.com/giantswarm/aws-ebs-csi-driver-app/pull/255))
      * Chart: Fix proxy settings.
  - [3.0.2](https://github.com/giantswarm/aws-ebs-csi-driver-
app/compare/v3.0.1...v3.0.2)
      * Chart: Sync to upstream. ([#253](https://github.com/giantswarm/aws-ebs-csi-driver-app/pull/253))
      * Chart: Add FIPS endpoint support.
      * Chart: Add SELinux support.
      * Chart: Sync to upstream. ([#253](https://github.com/giantswarm/aws-ebs-csi-driver-app/pull/253))
      * Chart: Consume `global.image.registry`.
      * Chart: Fix IRSA annotation rendering.
      * Chart: Bump images.
  - [3.0.1](https://github.com/giantswarm/aws-ebs-csi-driver-
app/compare/v3.0.0...v3.0.1)
      * Repository: Some chores. ([#235](https://github.com/giantswarm/aws-ebs-csi-driver-app/pull/235))
      * Repository: Add `Makefile.custom.mk`.
      * Chart: Add `snapshot-controller` NetworkPolicy. ([#246](https://github.com/giantswarm/aws-ebs-csi-driver-app/pull/246))
      * Kustomization: Add `snapshot-controller` NetworkPolicy.
      * Harden security context for controller and node.

- [alloy-app](https://github.com/giantswarm/alloy-app)
  - [0.9.0](https://github.com/giantswarm/alloy-app/compare/v0.8.0...v0.9.0)
      * Upgrade Alloy upstream chart from 0.11.0 to 0.12.1
      * This bumps the version of Alloy from 1.6.1 to 1.7.1
  - [0.8.0](https://github.com/giantswarm/alloy-app/compare/v0.7.0...v0.8.0)
      * Upgrade Alloy upstream chart from 0.10.1 to 0.11.0
      * This bumps the version of Alloy from 1.5.0 to 1.6.1
...
```

Example output
```

## Fleet management

- [AWS EBS CSI Driver App](https://github.com/giantswarm/aws-ebs-csi-driver-app) version [3.0.3](https://github.com/giantswarm/aws-ebs-csi-driver-app/compare/v3.0.0...v3.0.3)
  - Improved the chart settings to better structure and readability.
  - Added a snapshot network policy to allow communication to API.
  - Hardened the security contexts of the components.
  - Brought the latest changes from upstream.

## Observability

- [Alloy App](https://github.com/giantswarm/alloy-app) version [0.31.0](https://github.com/giantswarm/alloy-app/compare/v0.7.0...v0.9.0)
    - Upgraded to the latest Allow version to get the new changes and bugfixes.

...
```

Make sure all projects of the attached file are considered for the output.

# Prompt to get the summary to share in Slack

Now from the previous summary I would like to have a summary without links and just mentioning main changes grouped by the categories.

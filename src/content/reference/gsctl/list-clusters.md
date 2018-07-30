+++
title = "gsctl Command Reference: list clusters"
description = "The 'gsctl list clusters' command shows all clusters you have access to with a few details like cluster ID, name, creation date, and owner organization."
date = "2018-03-08"
type = "page"
weight = 51
+++

# `gsctl list clusters`

The `gsctl list clusters` command shows all clusters you have access to with a few details like cluster ID, name, creation date, and owner organization.

## Example {#example}

```nohighlight
$ gsctl list clusters
ID     ORGANIZATION  NAME        RELEASE  CREATED
feogv  acme          Staging     3.0.2    2018 Feb 01, 13:59 UTC    
pmb9q  acme          Production  3.0.2    2018 Feb 01, 11:12 UTC
z63so  testteam      Dan's Test  2.7.2    2017 Jun 19, 09:12 UTC  
```

The details displayed are:

- `ID`: The unique cluster ID.
- `ORGANIZATION`: The cluster's owner organization.
- `NAME`: The name selected for the cluster on creation.
- `RELEASE`: The version number of the release used by the cluster. For older clusters, this may be `n/a`.
- `CREATED`: The date and time when the cluster has been created (UTC).

## Related

- [`gsctl create cluster`](../create-cluster/): Creating a cluster
- [`gsctl delete cluster`](../create-cluster/): Deleting a cluster
- [`gsctl list releases`](../list-releases/): Listing available releases

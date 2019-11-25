+++
title = "gsctl Command Reference: list clusters"
description = "The 'gsctl list clusters' command shows all clusters you have access to with a few details like cluster ID, name, creation date, and owner organization."
date = "2019-11-25"
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

## Argument reference

- `--output` or `-o`: Using this flag with the value `json`, the output can be printed in JSON format. This is convenient for use in automation. The default output format is `table`, which results in an output like shown above.
- `--show-deleting`: Set this flag to also list clusters that are currently being deleted and add a `DELETING SINCE` column. Has no effect with `--output json`, as JSON output contains all clusters, deleted or not.

## Related

- [`gsctl create cluster`](../create-cluster/)
- [`gsctl scale cluster`](../scale-cluster/)
- [`gsctl delete cluster`](../delete-cluster/)
- [API: Get clusters](/api/#operation/getClusters)

+++
title = "Using the Cabin Mobile App"
description = "You can use the Cabin mobile app to access and control your Kubernetes cluster."
date = "2016-11-22"
type = "page"
weight = 100
tags = ["tutorial"]
+++

# Using the Cabin Mobile App

You can use the free Cabin smartphone app for [iOS](https://itunes.apple.com/fr/app/cabin-manage-kubernetes-applications/id1137054392) or [Android](https://play.google.com/store/apps/details?id=com.skippbox.cabin) from [skippbox](http://www.skippbox.com/cabin/) to acces your cluster from your mobile device.

All you need is your API Endpoint

```nohighlight
https://api.<cluster-id>.k8s.gigantic.io
```

and an access token. You can get your default service account token by running (the last part of the pod name should be different in your case):

```nohighlight
$ kubectl get secrets
NAME                  TYPE                                  DATA      AGE
default-token-76jq5   kubernetes.io/service-account-token   3         2d
$ kubectl describe secret default-token-76jq5
```

Note: The token is quite long so you might want to use some relatively safe way to copy or send it to your phone digitally.

Once you have entered these into the respective fields in Cabin you should be able to access and control your cluster from the app.

![Cabin Screenshot](/img/cabin.jpg)

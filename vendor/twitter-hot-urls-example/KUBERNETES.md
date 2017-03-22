

## Start a local Kubernetes using minikube

> If some webpages don't show up immediately wait a bit and reload. Also the Kubernetes Dashboard needs reloading to update its view.

```bash
minikube start
# --vm-driver kvm

minikube dashboard
#^ maybe wait a bit and retry
kubectl get --all-namespaces services,pods
```

## Monitoring with Prometheus and Grafana

```bash
kubectl apply \
  --filename https://raw.githubusercontent.com/giantswarm/kubernetes-prometheus/master/manifests-all.yaml
minikube service --namespace monitoring prometheus
  # see /targets
minikube service --namespace monitoring grafana
  # see /dashboard/db/kubernetes-cluster-monitoring-via-prometheus
```

## Creating the Twitter api secrets manifest

Before running this example you unfortunately need to get four values from your personal Twitter [account](https://twitter.com/signup) and add them to `secrets/twitter-api-secret.yaml`. For some background see the Twitter documentation about [streaming API](https://dev.twitter.com/streaming/overview/connecting).

Go to [Twitter Application Management](https://apps.twitter.com/) and create a [new](https://apps.twitter.com/app/new) application. Enter some details like these:

    Name: thux
    Description: Tracks URLs mentioned on Twitter and creates a ranked list
    Website: https://github.com/giantswarm/twitter-hot-urls-example
    Callback URL: <leave this field blank>

After that also create an Access Token under "Keys and Access Tokens". Edit `secrets/twitter-api-secret.yaml` and fill all four data fields with the corresponding [`base64` encoded values]((http://kubernetes.io/docs/user-guide/secrets/#creating-a-secret-manually)).

```nohighlight
printf "exampletokenxyz" | base64
```

## Bring up our Twitter app

```bash
kubectl apply --filename secrets/twitter-api-secret.yaml
kubectl apply \
  --filename https://raw.githubusercontent.com/giantswarm/twitter-hot-urls-example/master/manifests-all.yaml

# there is an api limit. to not hit that accidentally, let's pause the tracker for now:
kubectl --namespace thux scale deployments/tracker --replicas 0

kubectl --namespace thux scale deployments/tracker --replicas 1
kubectl --namespace thux scale deployments/resolver --replicas 3

# there is an api limit. don't track too much.
kubectl --namespace thux scale deployments/tracker --replicas 0
```


## Turn down all the thux components

```bash
kubectl delete namespace thux
```

Works the same for `monitoring`.

To delete the whole local Kubernetes cluster use this:
```bash
minikube delete
```


# How to create one single manifest file

```bash
target="./manifests-all.yaml"
rm "$target"
printf -- "# Derived from ./manifests/*.yaml\n---\n" >> "$target"
for file in ./manifests/*.yaml ; do
  if [ -e "$file" ] ; then
     cat "$file" >> "$target"
     printf -- "---\n" >> "$target"
  fi
done
```

---
title: Installing the Kubernetes Dashboard
description: The Dashboard is a general-purpose administrative web UI for Kubernetes, running in Kubernetes itself. It's easy to install.
type: page
weight: 50
tags: ["recipe"]
owner:
  - https://github.com/orgs/giantswarm/teams/sig-customer-happiness
---

# Installing the Kubernetes Dashboard

[Kubernetes Dashboard](https://github.com/kubernetes/dashboard/) is the official general purpose web UI for Kubernetes clusters. It can show you all running workloads in your cluster and even includes some functionality to control and change those workloads. It can show logs of your pods and if you have Heapster monitoring installed also some basic resource usage.

![Kubernetes Dashboard](/img/dashboard-ui.png)

Keep in mind that Dashboard despite it 1.x version number is still an early-stage effort and might miss certain functionality (e.g. no cascaded deletes like `kubectl`).

If you want to have some simple metrics (as shown in the screenshot above) integrated in your Dashboard, you can additionally [install Heapster](/guides/kubernetes-heapster/).

## Deploying dashboard

Deploying dashboard is easy and straight forward.

```nohighlight
kubectl apply \
  -f https://raw.githubusercontent.com/kubernetes/dashboard/master/src/deploy/recommended/kubernetes-dashboard.yaml
```

Once the pod is running you can open Dashboard at `https://api.<cluster-id>.k8s.gigantic.io/ui`.

*Note*: The above URL uses your K8s API to proxy to the service. As the K8s API is guarded with your credentials, you need to [set them up in your system](/guides/accessing-services-from-the-outside/) (and/or browser). We do not recommend to set up an Ingress for the Dashboard at this time, as opening up the dashboard to public would create a non-official workaround to access K8s api. Please validate this with your security department and check the Heptio blog post [On Securing the Kubernetes Dashboard](https://blog.heptio.com/on-securing-the-kubernetes-dashboard-16b09b1b7aca)

Alternatively, you can run

```nohighlight
kubectl proxy
```

and then open your browser at this URL:

`http://localhost:8001/api/v1/namespaces/kube-system/services/https:kubernetes-dashboard:/proxy/`

You should see the authentication page for your dashboard, it is securely exposed.

![Kubernetes Dashboard Authentication](/img/dashboard-authentication.png)

You need to generate a Service Account token be have access to the dashboard.

### Create a cluster admin service account

You can create a service account with `cluster-admin` role that will have access to all your resources.

```nohighlight
kubectl create serviceaccount cluster-admin-dashboard-sa
kubectl create clusterrolebinding cluster-admin-dashboard-sa \
  --clusterrole=cluster-admin \
  --serviceaccount=default:cluster-admin-dashboard-sa
```

Copy the token from the generated secret

```nohighlight
$ kubectl get secret | grep cluster-admin-dashboard-sa
cluster-admin-dashboard-sa-token-6xm8l   kubernetes.io/service-account-token   3         18m

$ kubectl describe secret cluster-admin-dashboard-sa-token-6xm8l
Name:         cluster-admin-dashboard-sa-token-6xm8l
Namespace:    default
Labels:       <none>
Annotations:  kubernetes.io/service-account.name=cluster-admin-dashboard-sa-token-6xm8l
              kubernetes.io/service-account.uid=acba56a1-3ca1-11e8-b72f-000d3a275e3d

Type:  kubernetes.io/service-account-token

Data
====
ca.crt:     1314 bytes
namespace:  7 bytes
token:      eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJkZWZhdWx0Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZWNyZXQubmFtZSI6Im15LWRhc2hib2FyZC1zYS10b2tlbi02eG04bCIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VydmljZS1hY2NvdW50Lm5hbWUiOiJteS1kYXNoYm9hcmQtc2EiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC51aWQiOiJhY2JhNTZhMS0zY2ExLTExZTgtYjcyZi0wMDBkM2EyNzVlM2QiLCJzdWIiOiJzeXN0ZW06c2VydmljZWFjY291bnQ6ZGVmYXVsdDpteS1kYXNoYm9hcmQtc2EifQ.ovu7b1NYI4EqoPO-_54nbSdL50xqrkSSsB6HTEQ12aT_dgWr9QctkXIXgNYmSdOcgoCb4HbLsGZ0kWqG6KDwlPlOiPD_FzGeAPAiWCd_vHBHt1CAGeOsXa2b4-wKTt_iFaIKxS79mm_MsCoFilPUvdxzteC6hzYesSsq03faZkAXCGNQietgcn2Nw8BcvR2V7CgOnt87EMFz_4WNTLRSsaiu1QXW_YFMF1Wj3NG2IofX2g7dQwEavcm_tCq-dXCcSbvWbFutXOWzW5zmuIjDa4nmUOUzVKshEuzoPRtgjNV__WVvVC74Nhs6FC19F8FHYr0N7-IlSxGkaYven1ZSCE
```

Use this token to log into the dashboard.

### Create limited resources access service account

You can restrict the cluster access by creating a limited clusterrole.

The following example allow a user to only see `pods` and `namespaces`:

Create the `pod-viewer-role.yaml` file with the following content:

```yaml
kind: ClusterRole
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: pod-viewer
rules:
- apiGroups: [""] # core API group
  resources: ["pods", "namespaces"]
  verbs: ["get", "watch", "list"]
```

Create the service account associated with this role:

```nohighlight
kubectl create serviceaccount pod-viewer
kubectl apply -f pod-viewer-role.yaml
kubectl create clusterrolebinding pod-viewer-sa \
  --clusterrole=pod-viewer \
  --serviceaccount=default:pod-viewer-sa
```

Copy the token from the generated secret

```nohighlight
$ kubectl get secret | grep pod-viewer
pod-viewer-sa-token-2t2r9     kubernetes.io/service-account-token   3         2m
kubectl describe secret pod-viewer-sa-token-2t2r9
Name:         pod-viewer-sa-token-2t2r9
Namespace:    default
Labels:       <none>
Annotations:  kubernetes.io/service-account.name=pod-viewer-sa
              kubernetes.io/service-account.uid=6e9eaa6b-3ca5-11e8-b72f-000d3a275e3d

Type:  kubernetes.io/service-account-token

Data
====
ca.crt:     1314 bytes
namespace:  7 bytes
token:      eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJkZWZhdWx0Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZWNyZXQubmFtZSI6InBvZC12aWV3ZXItc2EtdG9rZW4tMnQycjkiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC5uYW1lIjoicG9kLXZpZXdlci1zYSIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VydmljZS1hY2NvdW50LnVpZCI6IjZlOWVhYTZiLTNjYTUtMTFlOC1iNzJmLTAwMGQzYTI3NWUzZCIsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OnBvZC12aWV3ZXItc2EifQ.MAKAeGNd7c170HZmpDTs1YS1TbU266hCNzTp-m6XcbxvUvhyu5-MKKMka7cn5R5EfY1oynHLfxOLnFuw_ArVdzjbDtPKBNNgU645135nOowRhxbGvaOCKUr5Pg3dFOUNV64OfWdqOU1vtrWLvu3vYRcAXFoWgfoAa2FyfRWuiaXdFURIVGKRkuFuqh3HK95BriVjnfH7JfWa0zYNB6oSDpy4QWcIGpVEMv7pL3JVCt6bz36l6AuGQkuev6maRC9oTTP6i-yLCi8O9gXZdjTBl3KOnK27Vj2oNXdj43KwErcMeWHOmRKcIBWzG5fl-vrly0x-4vxVCS4K5pO7jG_CCD
```

After login, the user can only see `namespaces` and `pods`.

![Kubernetes Dashboard Limited user](/img/dashboard-pod-viewer.png)

## Further reading

- [Official User Guide](https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/)
- [On Securing the Kubernetes Dashboard](https://blog.heptio.com/on-securing-the-kubernetes-dashboard-16b09b1b7aca)

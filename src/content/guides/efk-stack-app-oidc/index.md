---
title: Configure oidc for efk-stack-app
description: Configure authentication with kibana and the efk-stack-app through OIDC
date: 2020-10-30
type: page
weight: 50
tags: ["recipe"]
---
# Setup OIDC to authenticate with kibana and efk-stack-app

To manage access to the efk-stack-app using your company's user and group directories, the opendistro security plugin provides integration with different authentication backends.

Here, we configure the efk-stack-app with Azure AD through the OpenID Connect (OIDC) standard.

It should be portable to other authentication backends that provide the OIDC standard.

## Overview

- Step 1: Register app on Azure portal and configure JWT token
- Step 2: Configure opendistro-security plugin
- Step 3: Configure internal-users database
- Step 4: Configure roles-mapping to control users permission
- Step 5: Configure OIDC backend for Kibana

## Step 1: Register app on Azure portal and configure JWT token

### Limitation

As of writing: Opendistro security cannot map nested values in the JWT-token to roles. It's only possible to specify the key containing values that identify the user's role identifier.

### Register app on Azure portal

To setup a new "App registration" refer to the [official guide](https://docs.microsoft.com/en-us/Azure/active-directory/develop/quickstart-register-app).

The **redirect URI** pattern is:
`https://<your.kibana.url>/auth/openid/login`

*This can be changed later.*

(Note: Depends on the backend provider. Generally, there should be a mechanism that defines an object that represents the app with attributes to control who has which permissions. In Azure, this is "App registration".)

### Configure JWT token

The goal is to map a user's group ID in Azure to that user's permissions in Kibana. For example, if the user is a member of the Azure AD group "kibana-admins", the user obtains the role "admin" in Kibana.

Azure's JWT token needs to contain the group IDs of the user. Do this by adding an optional claim to the app-registration's token configuration.

1. In Azure platform, navigate to the app-registration created in the previous section
2. In the sidebar, click "Token configuration"
3. Click "+Add groups claim"
4. Select group types to include in the token (usually Security groups)
5. In "Customize token properties by type", select "Group ID" for every type
6. Click "Save"

For reference on how to define groups' optional claims, see [Microsoft's official documentation](https://docs.microsoft.com/en-us/Azure/active-directory/develop/active-directory-optional-claims#configuring-groups-optional-claims).

How to define and manage the required groups, as well as how to obtain the group IDs of those groups is out of scope for this guide. Check [Microsoft's documentation on Azure AD](https://docs.microsoft.com/en-us/Azure/devops/server/admin/setup-ad-groups?toc=%2FAzure%2Fdevops%2Forganizations%2Ftoc.json&bc=%2FAzure%2Fdevops%2Forganizations%2Fbreadcrumb%2Ftoc.json&view=Azure-devops-2020&viewFallbackFrom=Azure-devops)

## Step 2: Configure opendistro-security plugin

Opendistro-security is configured through secrets. These secrets need to be present in the app's namespace for the EFK configuration to deploy.

In this section, we create the target namespace and deploy the `configSecret` named `opendistro-security-config`.

Default namespace for the efk-stack-app is "efk-stack-app".

### Create namespace

To create the namespace on the tenant cluster, run:

```bash=
kubectl create namespace efk-stack-app
```

### Create configSecret

1. Save the .yaml lines below to a file called `config.yml`. Point `openid_connect_url` to the correct URL.
2. On the cluster run:

```bash=
kubectl create secret generic -n efk-stack-app opendistro-security-config --from-file=./config.yml
```

```yaml=config.yml
---
_meta:
  type: "config"
  config_version: 2

config:
  dynamic:
    http:
      anonymous_auth_enabled: false
      xff:
        enabled: false
        internalProxies: ".*"
        remoteIpHeader: "x-forwarded-for"
    authc:
      basic_internal_auth_domain:
        description: "Authenticate via HTTP Basic against internal users database"
        http_enabled: true
        transport_enabled: true
        order: 0
        http_authenticator:
          type: "basic"
          challenge: false
        authentication_backend:
          type: "internal"

      openid_auth_domain:
        http_enabled: true
        transport_enabled: true
        order: 1
        http_authenticator:
          type: "openid"
          challenge: false
          config:
            enable_ssl: false
            verify_hostnames: false
            roles_key: groups
            subject_key: preferred_username
            openid_connect_url: https://login.microsoftonline.com/XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX/v2.0/.well-known/openid-configuration
        authentication_backend:
          type: noop
    authz: {}
```

3. Check if secret was created correctly:

```bash=
kubectl get secret -n efk-stack-app opendistro-security-config -o yaml
```

Results should look like:

```yaml=
apiVersion: v1
data:
  config.yml: LS0tCl9tZXRhOgogIHR5cGU6ICJjb25maWciCiAgY29uZmlnX3ZlcnNpb246IDIKCmNvbmZpZzoKICBkeW5hbWljOgogICAgaHR0cDoKICAgICAgYW5vbnltb3VzX2F1dGhfZW5hYmxlZDogZmFsc2UKICAgICAgeGZmOgogICAgICAgIGVuYWJsZWQ6IGZhbHNlCiAgICAgICAgaW50ZXJuYWxQcm94aWVzOiAiLioiCiAgICAgICAgcmVtb3RlSXBIZWFkZXI6ICJ4LWZvcndhcmRlZC1mb3IiCiAgICBhdXRoYzoKICAgICAgYmFzaWNfaW50ZXJuYWxfYXV0aF9kb21haW46CiAgICAgICAgZGVzY3JpcHRpb246ICJBdXRoZW50aWNhdGUgdmlhIEhUVFAgQmFzaWMgYWdhaW5zdCBpbnRlcm5hbCB1c2VycyBkYXRhYmFzZSIKICAgICAgICBodHRwX2VuYWJsZWQ6IHRydWUKICAgICAgICB0cmFuc3BvcnRfZW5hYmxlZDogdHJ1ZQogICAgICAgIG9yZGVyOiAwCiAgICAgICAgaHR0cF9hdXRoZW50aWNhdG9yOgogICAgICAgICAgdHlwZTogImJhc2ljIgogICAgICAgICAgY2hhbGxlbmdlOiBmYWxzZQogICAgICAgIGF1dGhlbnRpY2F0aW9uX2JhY2tlbmQ6CiAgICAgICAgICB0eXBlOiAiaW50ZXJuYWwiCgogICAgICBvcGVuaWRfYXV0aF9kb21haW46CiAgICAgICAgaHR0cF9lbmFibGVkOiB0cnVlCiAgICAgICAgdHJhbnNwb3J0X2VuYWJsZWQ6IHRydWUKICAgICAgICBvcmRlcjogMQogICAgICAgIGh0dHBfYXV0aGVudGljYXRvcjoKICAgICAgICAgIHR5cGU6ICJvcGVuaWQiCiAgICAgICAgICBjaGFsbGVuZ2U6IGZhbHNlCiAgICAgICAgICBjb25maWc6CiAgICAgICAgICAgIGVuYWJsZV9zc2w6IGZhbHNlCiAgICAgICAgICAgIHZlcmlmeV9ob3N0bmFtZXM6IGZhbHNlCiAgICAgICAgICAgIHJvbGVzX2tleTogZ3JvdXBzCiAgICAgICAgICAgIHN1YmplY3Rfa2V5OiBwcmVmZXJyZWRfdXNlcm5hbWUKICAgICAgICAgICAgb3BlbmlkX2Nvbm5lY3RfdXJsOiBodHRwczovL2xvZ2luLm1pY3Jvc29mdG9ubGluZS5jb20vMzFmNzViZjktM2Q4Yy00NjkxLTk1YzAtODNkZDcxNjEzZGI4L3YyLjAvLndlbGwta25vd24vb3BlbmlkLWNvbmZpZ3VyYXRpb24KICAgICAgICBhdXRoZW50aWNhdGlvbl9iYWNrZW5kOgogICAgICAgICAgdHlwZTogbm9vcAogICAgYXV0aHo6IHt9Cg==
kind: Secret
metadata:
  creationTimestamp: "2020-11-03T16:24:02Z"
  name: opendistro-security-config
  namespace: efk-stack-app
  resourceVersion: "72854"
  selfLink: /api/v1/namespaces/efk-stack-app/secrets/opendistro-security-config
  uid: b3152bce-71d4-45a6-9837-9ba19eec5083
type: Opaque
```

**Note**
`roles_key` in `config.yml` defines what key from the OIDC token is used to identify the user's roles in Kibana. Here, it uses the user's group IDs. How to configure Azure to send the user's group IDs in the OIDC token is covered in the prev. section: **Register app on Azure portal and configure JWT token**

## Step 3: Configure internal-users database

Similar to the previous section, we use a secret to add to opendistro-security plugin's internal user database. This secret also needs to be present in the target namespace for efk-stack-app to deploy successfully.

### Create internalUsersSecret

1. Save the .yaml lines below to a file called `internal_users.yml`. Modify the `password hashes`.

It requires hashed passwords. Use https://bcrypt-generator.com/ or refer to the [opendistro-security guide](https://opendistro.github.io/for-elasticsearch-docs/docs/security/configuration/yaml/#internal_usersyml).

(Note: You will use these hashes as the admin password to be defined in the last section: "Configure OIDC backend for Kibana")

2. Generate and deploy the secret to the efk-stack-app namespace:

```bash=
kubectl create secret generic -n efk-stack-app opendistro-internal-users --from-file=./internal_users.yml
```

```yaml=internal_users.yml
---
# This is the internal user database
# The hash value is a bcrypt hash and can be generated with plugin/tools/hash.sh or https://bcrypt-generator.com/

_meta:
  type: "internalusers"
  config_version: 2

## Demo users
admin:
  hash: "$2y$12$GVKPJmDPILWPR8EQoF90zOXmtquEyqlzEGkE4mwPcx1s55maulQTa" #bdmin
  reserved: true
  backend_roles:
  - "admin"
  description: "Demo admin user"

logstash:
  hash: "$2y$12$zG9xarxF4as6ZvVEK8De/OC/3ErV/Um/szyHvASrTgzMv7SLq17Xq" #logstash
  reserved: false
  backend_roles:
  - "logstash"
  description: "Demo logstash user"
```

3. Check if the secret was created correctly:

```bash=
kubectl get secret -n efk-stack-app opendistro-internal-users -o yaml
```

The results should look similar to this:

```yaml=
apiVersion: v1
data:
  internal_users.yml: LS0tCiMgVGhpcyBpcyB0aGUgaW50ZXJuYWwgdXNlciBkYXRhYmFzZQojIFRoZSBoYXNoIHZhbHVlIGlzIGEgYmNyeXB0IGhhc2ggYW5kIGNhbiBiZSBnZW5lcmF0ZWQgd2l0aCBwbHVnaW4vdG9vbHMvaGFzaC5zaCBvciBodHRwczovL2JjcnlwdC1nZW5lcmF0b3IuY29tLwoKX21ldGE6CiAgdHlwZTogImludGVybmFsdXNlcnMiCiAgY29uZmlnX3ZlcnNpb246IDIKCiMjIERlbW8gdXNlcnMKYWRtaW46CiAgaGFzaDogIiQyeSQxMiRHVktQSm1EUElMV1BSOEVRb0Y5MHpPWG10cXVFeXFsekVHa0U0bXdQY3gxczU1bWF1bFFUYSIgI2JkbWluCiAgcmVzZXJ2ZWQ6IHRydWUKICBiYWNrZW5kX3JvbGVzOgogIC0gImFkbWluIgogIGRlc2NyaXB0aW9uOiAiRGVtbyBhZG1pbiB1c2VyIgoKbG9nc3Rhc2g6CiAgaGFzaDogIiQyeSQxMiR6Rzl4YXJ4RjRhczZadlZFSzhEZS9PQy8zRXJWL1VtL3N6eUh2QVNyVGd6TXY3U0xxMTdYcSIgI2xvZ3N0YXNoCiAgcmVzZXJ2ZWQ6IGZhbHNlCiAgYmFja2VuZF9yb2xlczoKICAtICJsb2dzdGFzaCIKICBkZXNjcmlwdGlvbjogIkRlbW8gbG9nc3Rhc2ggdXNlciIK
kind: Secret
metadata:
  creationTimestamp: "2020-11-04T13:04:02Z"
  name: opendistro-internal-users
  namespace: kube-public
  resourceVersion: "143672"
  selfLink: /api/v1/namespaces/kube-public/secrets/opendistro-internal-users
  uid: 614236f2-dcbb-4b1e-a22c-2baafc856b70
type: Opaque
```

## Step 4: Configure roles-mapping to control users permission

The `rolesMappingSecret` is used to configure initial role mappings to the opendistro-security plugin.

Here, the Azure AD group ID for group "kibana-admin" is mapped to the role "all_access". The Azure AD group ID for group "kibana-user" is mapped to the role "kibana_user"

### Create roleMappingSecret

1. Save the .yaml lines below to a file called `roles_mapping.yml`. Make sure to add the group ID of the Azure AD group to the backend_roles section of the corresponding role.
2. Generate and deploy the secret to the efk-stack-app namespace:

```bash=
kubectl create secret generic -n efk-stack-app opendistro-roles-mapping --from-file=./roles_mapping.yml
```

```yaml=roles_mapping.yml
---
_meta:
  type: "rolesmapping"
  config_version: 2
all_access:
  reserved: true
  hidden: false
  backend_roles:
  - "admin"
  - "ae208f58-48cf-4e38-9a42-fe33b454dc5c" # Group ID for kibana-admin
  hosts: []
  users: []
  and_backend_roles: []
  description: "Maps admin to all_access"
manage_snapshots:
  reserved: true
  hidden: false
  backend_roles:
  - "snapshotrestore"
  hosts: []
  users: []
  and_backend_roles: []
logstash:
  reserved: false
  hidden: false
  backend_roles:
  - "logstash"
  hosts: []
  users: []
  and_backend_roles: []
own_index:
  reserved: false
  hidden: false
  backend_roles: []
  hosts: []
  users:
  - "*"
  and_backend_roles: []
  description: "Allow full access to an index named like the username"
kibana_user:
  reserved: false
  hidden: false
  backend_roles:
  - "kibanauser"
  - "7ad5de3e-dc0e-4710-bc89-59e5b88058b0" # Group ID for kibana-user
  hosts: []
  users: []
  and_backend_roles: []
  description: "Maps kibanauser to kibana_user"
complex-role:
  reserved: false
  hidden: false
  backend_roles:
  - "ldap-analyst"
  hosts: []
  users:
  - "new-user"
  and_backend_roles: []
readall:
  reserved: true
  hidden: false
  backend_roles:
  - "readall"
  hosts: []
  users: []
  and_backend_roles: []
kibana_server:
  reserved: true
  hidden: false
  backend_roles: []
  hosts: []
  users:
  - "kibanaserver"
  and_backend_roles: []
```

3. Check if the secret was created correctly:

```bash=
kubectl get secret -n efk-stack-app opendistro-roles-mapping -o yaml
```

The results should look similar to this:

```yaml=
apiVersion: v1
data:
  roles_mapping.yml: LS0tCl9tZXRhOgogIHR5cGU6ICJyb2xlc21hcHBpbmciCiAgY29uZmlnX3ZlcnNpb246IDIKYWxsX2FjY2VzczoKICByZXNlcnZlZDogdHJ1ZQogIGhpZGRlbjogZmFsc2UKICBiYWNrZW5kX3JvbGVzOgogIC0gImFkbWluIgogIC0gIjg2YmQ4YzE3LTU3OGEtNDcxNy04MDJmLWZkZmE2MjYwYTQxOCIKICBob3N0czogW10KICB1c2VyczogW10KICBhbmRfYmFja2VuZF9yb2xlczogW10KICBkZXNjcmlwdGlvbjogIk1hcHMgYWRtaW4gdG8gYWxsX2FjY2VzcyIKbWFuYWdlX3NuYXBzaG90czoKICByZXNlcnZlZDogdHJ1ZQogIGhpZGRlbjogZmFsc2UKICBiYWNrZW5kX3JvbGVzOgogIC0gInNuYXBzaG90cmVzdG9yZSIKICBob3N0czogW10KICB1c2VyczogW10KICBhbmRfYmFja2VuZF9yb2xlczogW10KbG9nc3Rhc2g6CiAgcmVzZXJ2ZWQ6IGZhbHNlCiAgaGlkZGVuOiBmYWxzZQogIGJhY2tlbmRfcm9sZXM6CiAgLSAibG9nc3Rhc2giCiAgaG9zdHM6IFtdCiAgdXNlcnM6IFtdCiAgYW5kX2JhY2tlbmRfcm9sZXM6IFtdCm93bl9pbmRleDoKICByZXNlcnZlZDogZmFsc2UKICBoaWRkZW46IGZhbHNlCiAgYmFja2VuZF9yb2xlczogW10KICBob3N0czogW10KICB1c2VyczoKICAtICIqIgogIGFuZF9iYWNrZW5kX3JvbGVzOiBbXQogIGRlc2NyaXB0aW9uOiAiQWxsb3cgZnVsbCBhY2Nlc3MgdG8gYW4gaW5kZXggbmFtZWQgbGlrZSB0aGUgdXNlcm5hbWUiCmtpYmFuYV91c2VyOgogIHJlc2VydmVkOiBmYWxzZQogIGhpZGRlbjogZmFsc2UKICBiYWNrZW5kX3JvbGVzOgogIC0gImtpYmFuYXVzZXIiCiAgaG9zdHM6IFtdCiAgdXNlcnM6IFtdCiAgYW5kX2JhY2tlbmRfcm9sZXM6IFtdCiAgZGVzY3JpcHRpb246ICJNYXBzIGtpYmFuYXVzZXIgdG8ga2liYW5hX3VzZXIiCmNvbXBsZXgtcm9sZToKICByZXNlcnZlZDogZmFsc2UKICBoaWRkZW46IGZhbHNlCiAgYmFja2VuZF9yb2xlczoKICAtICJsZGFwLWFuYWx5c3QiCiAgaG9zdHM6IFtdCiAgdXNlcnM6CiAgLSAibmV3LXVzZXIiCiAgYW5kX2JhY2tlbmRfcm9sZXM6IFtdCnJlYWRhbGw6CiAgcmVzZXJ2ZWQ6IHRydWUKICBoaWRkZW46IGZhbHNlCiAgYmFja2VuZF9yb2xlczoKICAtICJyZWFkYWxsIgogIGhvc3RzOiBbXQogIHVzZXJzOiBbXQogIGFuZF9iYWNrZW5kX3JvbGVzOiBbXQpraWJhbmFfc2VydmVyOgogIHJlc2VydmVkOiB0cnVlCiAgaGlkZGVuOiBmYWxzZQogIGJhY2tlbmRfcm9sZXM6IFtdCiAgaG9zdHM6IFtdCiAgdXNlcnM6CiAgLSAia2liYW5hc2VydmVyIgogIGFuZF9iYWNrZW5kX3JvbGVzOiBbXQ==
kind: Secret
metadata:
  creationTimestamp: "2020-11-04T15:49:35Z"
  name: opendistro-roles-mapping
  namespace: kube-public
  resourceVersion: "182662"
  selfLink: /api/v1/namespaces/kube-public/secrets/opendistro-roles-mapping
  uid: d6acebb9-0404-4f4f-aa13-6c3f85d11f23
type: Opaque
```

## Step 5: Configure OIDC backend for Kibana

Now that the requirements to deploy the app are done, the efk-stack-app can be deployed to the tenant cluster.

Below is the minimal required `values.yaml` needed to configure EFK at time of installation. Currently, it's not supported to reload configuration from configMaps so make sure to finish this guide before deploying the app.

The required values to fill the template below can be found in Microsoft's [official guide](https://docs.microsoft.com/en-us/Azure/active-directory/develop/quickstart-register-app) for setting up an app-registration on Azure portal.

**Finally, ensure admin password matches with password hashes defined in "Step 3: Configure internal-users database".**

```yaml
opendistro-es:
  elasticsearch:
    securityConfig:
      enabled: true
      path: "/usr/share/elasticsearch/plugins/opendistro_security/securityconfig"
      internalUsersSecret: "opendistro-internal-users"
      configSecret: "opendistro-security-config"
      rolesMappingSecret: "opendistro-roles-mapping"


  kibana:
    username: admin
    password: <kibana-admin-password> 

    config:
      opendistro_security.openid.base_redirect_url: <your.kibana.url>
      opendistro_security.auth.type: openid
      opendistro_security.openid.client_id: <your client ID>
      opendistro_security.openid.client_secret: <your client secret>
      opendistro_security.openid.connect_url: https://login.microsoftonline.com/XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX/v2.0/.well-known/openid-configuration

    ingress:
      annotations:
        nginx.ingress.kubernetes.io/force-ssl-redirect: "true"
        nginx.ingress.kubernetes.io/proxy-buffer-size: 64k
        cert-manager.io/cluster-issuer: letsencrypt-giantswarm # This requires cert-manager to be installed.
      enabled: true
      hosts:
      - https://<your.kibana.url>
      path: /
      tls:
      - hosts:
        - https://<your.kibana.url>
        secretName: kibana.tls
    ssl:
      kibana:
        enabled: false
```

Once Kibana is deployed, users should be able to access Kibana with their Microsoft credentials and with permissions mapped to their groups.
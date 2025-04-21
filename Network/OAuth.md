
> An OAuth scope is a mechanism used in OAuth 2.0 to specify the level of access that a client application is requesting when interacting with an API or a service. Scopes define the specific permissions that the client application needs, and they help to ensure that the application only gets access to the resources it requires, rather than unrestricted access to the user's data.
> 

> 
> 1. **Permission Granularity**: Scopes allow you to specify fine-grained permissions. For example, an application might request only read access to a user's calendar rather than full read/write access.
> 
> 2. **Access Tokens**: When an OAuth token is issued (like an access token or a refresh token), it is often associated with one or more scopes. The token can then only be used to perform actions that are allowed by those scopes.
> 
> 3. **User Consent**: When a user authorizes an application to access their data, they are often shown a consent screen that lists the scopes the application is requesting. The user can then decide whether to grant those permissions.
> 
> 4. **Service-Specific Scopes**: Different services define their own scopes. For example, Google Cloud, Google APIs, GitHub, and Facebook all have different sets of scopes that can be requested by client applications.

> 
> In the Terraform code provided down below, there's an OAuth scope:
> 
> ```hcl
> 
> resource "google_container_cluster" "main" {
>   name               = "${var.cluster_name}-${var.branch}"
>   location           = var.location
>   initial_node_count = 3
> 
>   # Only for prod env it will be deployed, since prod won't accept not-attested images
>   dynamic "binary_authorization" {
>     for_each = var.branch == "prod" ? [1] : []
>     content {
>       evaluation_mode = "PROJECT_SINGLETON_POLICY_ENFORCE"
>     }
>   }
> 
>   node_config {
>     service_account = local.service_account_email # Retrieving the email of the service account from locals
>     disk_size_gb    = 10                          # Setting disk size to 10 GB because of the free account quota limits
>     oauth_scopes = [
>       # This scope is a Google Cloud OAuth scope that grants the service account full access to all Google Cloud services.
>       # It’s a broad scope that allows the application or service account to perform any action across the entire Google Cloud Platform,
>       # including managing resources, accessing APIs, and interacting with various services.
>       "https://www.googleapis.com/auth/cloud-platform"
> 
>     ]
>   }
>   # Defines how long Terraform should wait for the create and update operations to complete.
>   timeouts {
>     create = "30m" # Allows up to 30 minutes for the cluster creation process
>     update = "40m" # Allows up to 40 minutes for the cluster update process
>   }
> }
> 
> ```
> 
> This scope, `https://www.googleapis.com/auth/cloud-platform`, is a Google Cloud OAuth scope that grants the client full access to all Google Cloud services. It’s a broad scope that allows the application or service account to perform any action across the entire Google Cloud Platform, including managing resources, accessing APIs, and interacting with various services.

> - **Read-only Access**: An application might request a read-only scope for accessing Google Drive files, like `https://www.googleapis.com/auth/drive.readonly`.
> - **Limited API Access**: An app might request only the ability to read a user's email address and basic profile information, using scopes like `email` and `profile`.
> - **Cloud Platform Access**: As in Terraform example provided above, a service account might need broad access to manage resources across Google Cloud, which would require a scope like `https://www.googleapis.com/auth/cloud-platform`.

> [!n] What is the Difference Between IAM Role Assignments and OAuth Scope Access?
> - **IAM Roles**: Control what the service account can do on Google Cloud services. For example, if we assign `roles/container.admin` role to the service account, it allows for the management of GKE clusters.
> - **OAuth Scopes**: Define what level of API access the service account has when used by a GKE node or an application. Scopes are more about access to APIs rather than defining specific permissions on resources. 

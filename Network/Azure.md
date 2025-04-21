
```bash
# Install Azure CLI.
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
```
---

```bash
# Show current configs of azure cli. (subscription_id, tenant_id)
az account show
```
---
```bash
# Create a service principal for terraform to operate on Azure, and save the credentials into a file. If we specify scope in subscription level, then this service principal will have access within subscription scope.
az ad sp create-for-rbac --name="sp-contributor-terraform" --role="Contributor" \
--scopes="/subscriptions/$AZ_SUBSCRIPTION_ID" \
> az_sp_terraform.json
```
---
```bash
# Delete the network watcher resource. Network Watcher is a regional service that enables you to monitor and diagnose conditions at a network scenario level in, to, and from Azure.
az network watcher configure --resource-group NetworkWatcherRG --locations \
eastus --enabled false
```
---
```bash
# Delete the resource group
az group delete <resource_group_name NetworkWatcherRG>
```
---
```bash
# List all locations/regions available on Azure. Useful when provisioning resources using IaC
az account list-locations -o table
```
---
```bash
# List resource groups that exist in current scope.
az group list
```
---
```bash
# List all available subscriptions.
az account list --output table
```
---
```bash
# Change the current subscription into another one
az account set --subscription "<subscription_name>"
```
---
```bash
# Lists all storage accounts
az storage account list
```
---
```bash
# Get the storage account name
az storage account list --query "[].name" --output tsv
```
---
```bash
# Get the containers within a storage account
az storage container list --account-name <storage_account_name> --auth-mode \
login --query "[].name" --output tsv

```

> [!NOTE] VM Connections within same Virtual Network?
> **Note**: If we create virtual machines within the same virtual network, they will be able to create ssh connections just by using their VM names. `ssh web` would work, for instance.
> 

```bash
# List all available locations/regions in Azure
az account list-locations -o table
```
---
```bash
# List all available vm images according to the specifications
az vm image list --publisher <PublisherName Canonical> --offer <OfferName UbuntuServer> --sku <SKUName 18.04-LTS> --location <Location germanywestcentral> --all --output tsv
```
---
```bash
# Get IP addresses of VMs.
az vm list-ip-addresses --output table
```
---

> [!NOTE] Budgets vs. Cost Alerts?
> 1. **Budgets**:
>     
>     - Budgets allow you to set a **financial spending limit** for a specific subscription, resource group, or service over a defined time period (e.g., monthly, quarterly).
>     - You can monitor and track your spending relative to the budget you have set.
>     - Azure provides notifications when your spending reaches a certain percentage of your budget (e.g., 50%, 75%, or 100%), but it doesn’t stop services automatically when the budget is exceeded.
>     - **Example**: You set a budget of $500 for your Azure subscription for the month. Azure will notify you when your spending hits $250 (50%), $375 (75%), and $500 (100%).
> 2. **Cost Alerts**:
>     
>     - Cost alerts are used to notify you based on specific spending thresholds or anomalies.
>     - These alerts can be set independently of a budget and can be triggered when unexpected spending occurs, or specific conditions are met.
>     - **Example**: You create a cost alert to notify you when your spending exceeds $100 in a week, regardless of your monthly budget.
> 
> **Summary**:
> 
> - **Budgets** help you plan and monitor your spending over time.
> - **Cost Alerts** provide immediate notifications for custom thresholds or unexpected cost spikes.


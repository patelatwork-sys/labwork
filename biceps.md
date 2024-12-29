
### Main Template (`main.bicep`)
- **Scope**: Subscription
- **Resources**:
  - Resource Group
  - Storage Account (via module)
  - Storage Container (via module)

#### Parameters
- `location`: Azure region for deployment
- `environmentName`: Environment name (dev/test/prod)

#### Deployment Flow
1. **Resource Group**: Creates a resource group with naming convention `rg-{locationAcronym}-{environmentName}`
2. **Storage Account**: Deploys a storage account using `storage.bicep`
3. **Storage Container**: Creates a container named 'tfplan' in the storage account using `storage_container.bicep`

### Storage Module (`storage.bicep`)
- **Purpose**: Creates an Azure Storage Account
- **Outputs**: Storage account name

### Storage Container Module (`storage_container.bicep`)
- **Purpose**: Creates a container named 'tfplan' in the specified storage account

## GitHub Actions Workflow

### Workflow File: `infra.yml`
Located in `.github/workflows/infra.yml`, this workflow automates the deployment process.

#### Jobs
- **deploy**: Runs on `ubuntu-latest` and targets the `Dev` environment

#### Steps
1. **Checkout Code**: Uses `actions/checkout@v3` to checkout the repository code
2. **Azure Login**: Uses `azure/login@v1` to authenticate with Azure using service principal credentials
3. **Run What-If Analysis**: Uses `azure/cli@v1` to preview changes with `az deployment sub what-if`
4. **Manual Approval**: Uses `trstringer/manual-approval@v1` to wait for manual approval before proceeding
5. **Deploy Resources**: Uses `azure/cli@v1` to deploy resources with `az deployment sub create`

#### Conditions
- Deployment only proceeds if the branch is `main` or `master`

### Usage
To trigger the workflow, push changes to the `main` or `master` branch. The workflow will:
1. Run a what-if analysis
2. Wait for manual approval
3. Deploy the resources if approved

## Deployment Instructions
Deploy using Azure CLI:
```bash
az deployment sub create \
  --location <azure-region> \
  --template-file biceps/main.bicep \
  --parameters environmentName=<env-name> location=<azure-region>

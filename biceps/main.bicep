targetScope = 'subscription'
@description('Region for the resource group')
param region string

@allowed([
  'dev'
  'test'
  'prod'
]) 
@description('Environment name')
param environment string

var resourceGroupName = 'RGP-${region}-${environment}'

resource resourceGroup 'Microsoft.Resources/resourceGroups@2021-04-01' = {
  name: resourceGroupName
  location: region
}

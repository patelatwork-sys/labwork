targetScope = 'subscription'

@description('The Azure region for the deployment')
param location string
@description('The environment name')
param environmentName string

var locationAcronym = {
  eastus: 'eus'
  westus: 'wus'
  northeurope: 'neu'
  westeurope: 'weu'
}[toLower(location)]

resource resourceGroup 'Microsoft.Resources/resourceGroups@2021-04-01' = {
  name: 'rg-${locationAcronym}-${environmentName}'
  location: location
  tags: {
    Environment: environmentName
    Location: location
  }
}

output resourceGroupName string = resourceGroup.name

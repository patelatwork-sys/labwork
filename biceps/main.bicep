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

resource rg 'Microsoft.Resources/resourceGroups@2021-01-01' = {
  name: 'rg-${locationAcronym}-${environmentName}'
  location: location
  tags: {
    Environment: environmentName
    Location: location
  }
}

module storage 'resources/storage.bicep' = {
  name: 'storageAccountDeployment'
  scope: rg
  params: {
    location: location
    environmentName: environmentName
  }
}

module storageContainer 'resources/storage_container.bicep' = {
  name: 'storageContainerDeployment'
  scope: rg
  params: {
    storageAccountName: storage.outputs.storageAccountName
    containerName: 'tfplan'
  }
}

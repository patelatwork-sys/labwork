targetScope = 'subscription'

@description('The Azure region for the deployment')
param location string
@description('The environment name')
param environmentName string

module coreRG 'resources/rg.bicep' = {
  name: 'resourceGroupDeployment'
  params: {
    location: location
    environmentName: environmentName
  }
}

module storage 'resources/storage.bicep' = {
  name: 'storageAccountDeployment'
  scope: coreRG
  params: {
    location: location
    environmentName: environmentName
  }
  dependsOn: [
    coreRG
  ]
}

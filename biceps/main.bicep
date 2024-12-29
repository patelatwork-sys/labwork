targetScope = 'subscription'

@description('The Azure region for the deployment')
param location string

@description('The environment name (dev, test, prod)')
param environmentName string

resource resourceGroup 'Microsoft.Resources/resourceGroups@2021-04-01' = {
  name: 'rg-${environmentName}'
  location: location
  tags: {
    Environment: environmentName
  }
}

param location string
param environmentName string

var locationAcronym = {
  eastus: 'eus'
  westus: 'wus'
  northeurope: 'neu'
  westeurope: 'weu'
}[toLower(location)]

var uniqueSuffix = take(uniqueString(subscription().subscriptionId, resourceGroup().id), 5)

resource storageAccount 'Microsoft.Storage/storageAccounts@2022-09-01' = {
  name: 'sto${locationAcronym}${environmentName}${uniqueSuffix}'
  location: location
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
  tags: {
    Environment: environmentName
  }
}

output storageAccountName string = storageAccount.name

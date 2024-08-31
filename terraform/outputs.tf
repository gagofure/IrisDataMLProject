output "ml_workspace_id" {
  value = azurerm_machine_learning_workspace.ml_workspace.id
}

output "data_factory_id" {
  value = azurerm_data_factory.data_factory.id
}

output "storage_account_name" {
  value = azurerm_storage_account.storage.name
}

output "aks_cluster_name" {
  value = azurerm_kubernetes_cluster.aks.name
}

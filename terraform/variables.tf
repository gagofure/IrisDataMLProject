variable "location" {
  description = "The Azure region to deploy resources."
  default     = "East US"
}

variable "resource_group_name" {
  description = "Name of the resource group."
  default     = "rg-machine-learning"
}

variable "storage_account_name" {
  description = "Name of the storage account."
  default     = "mystorageaccount1234"
}

variable "ml_workspace_name" {
  description = "Name of the Azure Machine Learning workspace."
  default     = "ml-workspace"
}

variable "data_factory_name" {
  description = "Name of the Azure Data Factory."
  default     = "data-factory"
}

variable "aks_cluster_name" {
  description = "Name of the Azure Kubernetes Service cluster."
  default     = "aks-cluster"
}

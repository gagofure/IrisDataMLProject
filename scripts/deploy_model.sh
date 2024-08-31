#!/bin/bash

# Variables (passed from CI/CD pipeline)
RESOURCE_GROUP=$1
WORKSPACE_NAME=$2
MODEL_NAME=$3
SERVICE_NAME=$4

# Log in to Azure CLI
echo "Logging in to Azure CLI..."
az login --service-principal -u $(SP_APP_ID) -p $(SP_PASSWORD) --tenant $(TENANT_ID)

# Set the subscription (optional, if you have multiple subscriptions)
az account set --subscription $(SUBSCRIPTION_ID)

# Deploy the model using Python script
echo "Deploying the model..."
python scripts/deploy_model.py \
  --resource-group "$RESOURCE_GROUP" \
  --workspace-name "$WORKSPACE_NAME" \
  --model-name "$MODEL_NAME" \
  --service-name "$SERVICE_NAME"

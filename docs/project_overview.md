# Project Overview

## Introduction

This project involves building and deploying a predictive maintenance model using Azure services with the Iris dataset from scikit-learn.

## Components

1. **Azure Machine Learning**: For model training and deployment.
2. **Azure Data Factory**: For data pipeline management (optional).
3. **Azure Kubernetes Service (AKS)**: For deploying and scaling the model.
4. **Terraform**: To provision Azure infrastructure.
5. **Azure Pipelines**: For CI/CD to automate testing and deployment.

## Getting Started

1. **Infrastructure**: Run `terraform apply` in the `/terraform` directory to set up Azure resources.
2. **Model Training**: Use `train.py` to train the model.
3. **Model Deployment**: Use `deploy_model.sh` or `deploy_model.py` to deploy the model.

## CI/CD

The CI/CD pipeline is configured in `azure-pipelines.yml` and includes steps for installing dependencies, running tests, and deploying the model.

## License

This project is licensed under the MIT License. See `LICENSE` for details.

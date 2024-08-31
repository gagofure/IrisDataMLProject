# Project Overview

## Introduction

This project involves building and deploying a predictive maintenance model using Azure services with the Iris dataset from scikit-learn.

## Components

1. **Azure Machine Learning**: For model training and deployment.
2. **Azure Data Factory**: For data pipeline management (optional).
3. **Azure Kubernetes Service (AKS)**: For deploying and scaling the model.
4. **Terraform**: For provisioning Azure infrastructure.
5. **Azure Pipelines**: For CI/CD to automate infrastructure provisioning, testing, model training, scoring, and deployment.

## Getting Started

1. **CI/CD Pipeline**: Configure and run the Azure Pipelines to automate the setup of infrastructure, model training, scoring, and deployment. The pipeline is defined in `azure-pipelines.yml`.

2. **Model Training**: The model will be trained as part of the CI/CD pipeline. Ensure that `train.py` script is available for training the model.

3. **Model Scoring**: After training, the model will be evaluated using `score_model.py` to assess its performance.

4. **Model Deployment**: The model deployment will be handled within the CI/CD pipeline using `deploy_model.sh` or `deploy_model.py`.

## CI/CD

The CI/CD pipeline is configured in `azure-pipelines.yml` and includes the following steps:

1. **Terraform**: Automatically provisions Azure infrastructure as specified in the `/terraform` directory.
2. **Dependencies**: Installs necessary Python dependencies.
3. **Testing**: Runs tests to validate the model and code.
4. **Model Training**: Trains the model using the preprocessed data.
5. **Model Scoring**: Evaluates the model’s performance using test data and generates performance metrics.
6. **Model Deployment**: Deploys the trained model to Azure Machine Learning and/or AKS.

## License

This project is licensed under the MIT License. See `LICENSE` for details.

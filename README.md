# Predictive Maintenance Project

## Overview

This project involves the development and deployment of a predictive maintenance model using Azure services.

## Folder Structure

- `/terraform`: Terraform configuration for Azure infrastructure.
- `/scripts`: Scripts for model training, scoring, and deployment.
- `/data`: Raw and processed data storage.
- `/azure-pipelines`: CI/CD pipeline configuration for Azure DevOps.
- `/docs`: Project documentation.

## Setup

1. **Terraform**: Configure and apply Terraform scripts to set up infrastructure.
2. **Scripts**: Use provided Python and shell scripts for model management.
3. **CI/CD**: Set up Azure Pipelines for continuous integration and deployment.

## Instructions

1. **Deploy Infrastructure**: `terraform apply` in the `/terraform` directory.
2. **Train Model**: Run `train.py` to train the model.
3. **Deploy Model**: Use `deploy_model.py` or `deploy_model.sh` to deploy the model.
4. **CI/CD**: Configure Azure Pipelines with `azure-pipelines.yml`.

For detailed information, see `/docs/project_overview.md`.

## License

This project is licensed under the MIT License. See `LICENSE` for details.

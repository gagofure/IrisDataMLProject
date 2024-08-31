import argparse
import azureml.core
from azureml.core import Workspace, Model
from azureml.core.webservice import AksWebservice, InferenceConfig

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--resource-group', type=str, required=True, help='Azure Resource Group name')
    parser.add_argument('--workspace-name', type=str, required=True, help='Azure Machine Learning Workspace name')
    parser.add_argument('--model-name', type=str, required=True, help='Model name')
    parser.add_argument('--service-name', type=str, required=True, help='Service name')
    args = parser.parse_args()

    # Connect to Azure Machine Learning workspace
    ws = Workspace.get(name=args.workspace_name, resource_group=args.resource_group, subscription_id='your-subscription-id')

    # Load the model
    model = Model(ws, name=args.model_name)

    # Define the inference configuration
    inference_config = InferenceConfig(entry_script='score.py', environment=model.env)

    # Define the deployment configuration
    aks_config = AksWebservice.deploy_configuration(cpu_cores=1, memory_gb=1)

    # Deploy the model
    service = Model.deploy(ws, args.service_name, [model], inference_config, aks_config)
    service.wait_for_deployment(show_output=True)

    print(f"Model deployed to service: {service.name}")

if __name__ == '__main__':
    main()
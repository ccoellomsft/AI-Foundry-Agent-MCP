# AI Agent Solution using MCP Tools and Azure AI Foundry SDK

This solution demonstrates how to use MCP tools for AI agents with the Azure AI Foundry SDK.

## Prerequisites

- Python 3.x
- Azure subscription
- Access to Azure AI Foundry portal

## Setup Instructions

1. Navigate to the project directory:

   cd ai-foundry-agents-mcp/ai-foundry-agents-mcp-tools/Python

2. Create and activate a virtual environment:

   python -m venv labenv
   source ../labenv/Scripts/activate  # On Windows

3. Install the required packages:

   pip install -r requirements.txt azure-ai-projects mcp

4. Edit the `.env` file:

   code .env

   - Replace the `your_project_endpoint` placeholder with the endpoint for your project (copied from the project **Overview** page in the Azure AI Foundry portal).
   - Ensure that the `MODEL_DEPLOYMENT_NAME` variable is set to your model deployment name.

5. Log in to Azure:

   az login

You're now ready to use MCP tools with your AI agent project!

6. Run client.py:

   python client.py

7. Sample Queries:

    What is Microsoft's stock price?

    What exchange is MSFT listed on?

    Give me a list of Microsofts popular products.
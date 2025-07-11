# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("msft_info")

# Add an Msft Info tool
@mcp.tool()
def get_msft_stock_info() -> dict:
     """Returns MSFT stock information."""
     return {
  "symbol": "MSFT",
  "companyName": "Microsoft Corporation",
  "exchange": "NASDAQ",
  "currency": "USD",
  "currentPrice": 442.18,
  "open": 438.50,
  "high": 445.00,
  "low": 437.20,
  "previousClose": 439.10,
  "volume": 18234000,
  "marketCap": 3280000000000,
  "peRatio": 38.2,
  "eps": 11.57,
  "dividendYield": 0.78,
  "timestamp": "2025-07-10T13:50:00Z"
}



# Add a product info tool
@mcp.tool()
def get_msft_product_info() -> dict:
     """Returns a list of Microsoft Products."""
     return {
  "company": "Microsoft Corporation",
  "year": 2025,
  "top_product_1": {
    "name": "Microsoft 365 Copilot",
    "category": "AI Productivity",
    "description": "AI assistant integrated into Microsoft 365 apps like Word, Excel, and Outlook."
  },
  "top_product_2": {
    "name": "Azure OpenAI Service",
    "category": "Cloud AI",
    "description": "Platform for deploying and managing generative AI models in the cloud."
  },
  "top_product_3": {
    "name": "Microsoft Teams Premium",
    "category": "Collaboration",
    "description": "Enhanced Teams experience with AI-powered meeting summaries and security."
  },
  "top_product_4": {
    "name": "Surface Pro 11",
    "category": "Hardware",
    "description": "AI-enhanced 2-in-1 device with OLED display and Windows 12 integration."
  },
  "top_product_5": {
    "name": "Xbox Series Z",
    "category": "Gaming",
    "description": "Next-gen gaming console with cloud-native and AI-driven gameplay."
  },
  "top_product_6": {
    "name": "Azure Quantum",
    "category": "Quantum Computing",
    "description": "Hybrid quantum platform for enterprise-grade quantum applications."
  },
  "top_product_7": {
    "name": "Microsoft Defender XDR",
    "category": "Cybersecurity",
    "description": "Extended detection and response platform with AI threat intelligence."
  },
  "top_product_8": {
    "name": "Power Platform AI Builder",
    "category": "Low-Code AI",
    "description": "Tool for building AI models into Power Apps and Power Automate workflows."
  },
  "top_product_9": {
    "name": "Microsoft Loop",
    "category": "Collaboration",
    "description": "Flexible workspace for real-time co-creation across Microsoft 365."
  },
  "top_product_10": {
    "name": "Windows 12",
    "category": "Operating System",
    "description": "Latest OS with native AI features, enhanced security, and Copilot integration."
  }
}



mcp.run()
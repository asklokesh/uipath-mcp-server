"""
Basic usage example for Uipath MCP Server.

This example demonstrates how to:
1. Set up the MCP server
2. Make basic API calls
3. Handle responses

Prerequisites:
- Install the package: pip install uipath-mcp-server
- Set required environment variables (see .env.example or README.md)
"""

import asyncio
import os
from uipath_mcp.server import main


async def example_usage():
    """
    Example usage of Uipath MCP Server.

    Make sure to set the required environment variables before running:
    - See the README.md for complete environment variable requirements
    - Copy .env.example to .env and fill in your credentials
    """
    print("Starting Uipath MCP Server...")
    print("Make sure your environment variables are configured correctly.")
    print("")
    print("The server will start and listen for MCP protocol messages via stdio.")
    print("You can connect to it using Claude Desktop or any MCP-compatible client.")
    print("")
    print("Example Claude Desktop configuration:")
    print("""
{
  "mcpServers": {
    "uipath": {
      "command": "uvx",
      "args": ["uipath-mcp-server"],
      "env": {
        // Add your environment variables here
        // See README.md for required variables
      }
    }
  }
}
""")

    # Start the MCP server
    await main()


if __name__ == "__main__":
    # Check if required environment variables are set
    # Each service has different requirements - see README.md
    print("\n" + "="*60)
    print(f"  Uipath MCP Server - Basic Usage Example")
    print("="*60 + "\n")

    try:
        asyncio.run(example_usage())
    except KeyboardInterrupt:
        print("\nShutting down server...")
    except Exception as e:
        print(f"Error: {e}")
        print("\nPlease check:")
        print("1. Environment variables are set correctly")
        print("2. All dependencies are installed: pip install uipath-mcp-server")
        print("3. API credentials are valid")

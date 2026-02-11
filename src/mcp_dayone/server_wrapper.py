"""Synchronous wrapper for the async MCP server."""
import asyncio
from .server import main

def main_sync():
    """Synchronous entry point for uvx."""
    asyncio.run(main())

if __name__ == "__main__":
    main_sync()

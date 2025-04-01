import asyncio

from .manager import ResearchManager
from examples.set_azure_openai_client import *

async def main() -> None:
    query = input("What would you like to research? ")
    await ResearchManager().run(query)


if __name__ == "__main__":
    asyncio.run(main())

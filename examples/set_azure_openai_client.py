from openai import AsyncAzureOpenAI
from agents import set_default_openai_client
from dotenv import load_dotenv
import os

from src.agents import set_default_openai_key

# Load environment variables
load_dotenv()

if os.getenv("LLM_VENDOR") == "openai":
    set_default_openai_key(os.getenv("OPENAI_API_KEY"))
elif os.getenv("LLM_VENDOR") != "azure_openai":
    # Create OpenAI client using Azure OpenAI
    openai_client = AsyncAzureOpenAI(
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT")
    )

    # Set the default OpenAI client for the Agents SDK
    set_default_openai_client(openai_client)

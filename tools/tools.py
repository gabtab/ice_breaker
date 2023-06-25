from langchain.serpapi import SerpAPIWrapper
import os

def get_profile_url(text:str) -> str:
    """searches for Linkedin profile page"""
    search= SerpAPIWrapper(serpapi_api_key=os.environ.get("SERPAPI_API_KEY"))
    result = search.run(f"{text}")
    return result
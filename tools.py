from serpapi import GoogleSearch
from dotenv import load_dotenv
import os
import requests

load_dotenv()

SERP_API_KEY = os.getenv("SERPAPI_API_KEY")

def search_web(query):
    params = {
        "engine": "google",
        "q": query,
        "api_key": SERP_API_KEY
    }

    session = requests.Session()
    session.verify = False

    search = GoogleSearch(params)

    results = search.get_dict()

    if "organic_results" in results:
        return results["organic_results"][0]["snippet"]

    return "No web results found."
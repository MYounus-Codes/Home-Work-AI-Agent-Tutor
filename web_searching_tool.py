import requests
from agents import function_tool
import os
from dotenv import load_dotenv
from typing import List, Dict

# Load environment variables
load_dotenv()

@function_tool
def educational_search(
    query: str,
    subject: str = "general",
    resource_type: str = "all",
    num_results: int = 5
) -> Dict:
    """
    Search for fresh and relevant educational content (YouTube, docs, tutorials, PDFs).

    Parameters:
        query (str): The search query.
        subject (str): Topic area ("math", "physics", "general").
        resource_type (str): "tutorial", "documentation", "video", or "all".
        num_results (int): Number of results to return.

    Returns:
        dict: Categorized educational resources.
    """
    API_KEY = os.getenv('GOOGLE_SEARCHING_API_KEY')
    CSE_ID = os.getenv('GOOGLE_CSE_ID')

    if not API_KEY or not CSE_ID:
        return {
            'status': 'error',
            'message': 'Missing API key or CSE ID in environment variables.'
        }

    # Build base query
    edu_sites = (
        "site:khanacademy.org OR site:mathway.com OR site:brilliant.org OR "
        "site:byjus.com OR site:youtube.com OR site:physicsclassroom.com OR filetype:pdf"
    )

    filters = {
        "tutorial": "tutorial OR guide OR learn",
        "documentation": "reference OR explanation OR formula OR doc",
        "video": "lecture OR lesson OR explanation site:youtube.com"
    }

    # Compose query
    enhanced_query = f"{query} {edu_sites} after:2024"
    if subject != "general":
        enhanced_query += f" {subject}"
    if resource_type != "all" and resource_type in filters:
        enhanced_query += f" {filters[resource_type]}"

    params = {
        'q': enhanced_query,
        'key': API_KEY,
        'cx': CSE_ID,
        'num': num_results
    }

    try:
        response = requests.get("https://www.googleapis.com/customsearch/v1", params=params)
        response.raise_for_status()
        data = response.json()

        tutorials, documentation, videos, pdfs = [], [], [], []

        for item in data.get("items", []):
            title = item.get("title", "")
            link = item.get("link", "")
            snippet = item.get("snippet", "")
            source = item.get("displayLink", "")

            result = {
                "title": title,
                "link": link,
                "description": snippet,
                "source": source
            }

            if "youtube.com" in link:
                videos.append(result)
            elif link.lower().endswith(".pdf"):
                pdfs.append(result)
            elif any(keyword in title.lower() for keyword in ["tutorial", "guide", "learn"]):
                tutorials.append(result)
            else:
                documentation.append(result)

        return {
            "status": "success",
            "query_info": {
                "original_query": query,
                "subject": subject,
                "resource_type": resource_type
            },
            "resources": {
                "tutorials": tutorials,
                "documentation": documentation,
                "videos": videos,
                "pdfs": pdfs
            }
        }

    except requests.exceptions.RequestException as e:
        return {
            "status": "error",
            "message": f"Search failed: {str(e)}",
            "query": query
        }

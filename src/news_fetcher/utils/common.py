import requests
from news_fetcher import logger

def make_api_request(url, params):
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        logger.info(f"Successfully made API request: {response.url}")
        return response.json()
    except requests.RequestException as e:
        logger.error(f"Error in making API request: {e}")
        return {"error": str(e)}
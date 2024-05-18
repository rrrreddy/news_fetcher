from dotenv import load_dotenv
import os
from newsapi import NewsApiClient
from news_fetcher import logger


# Load environment variables from .env file
load_dotenv()

logger.info(f"Successfully loaded environment variables")

# Get API key from environment variables

class Config:
    @staticmethod
    def get_api_key():
        logger.info(f"Fetching API key from environment variables")
        
        try:
            api_key = os.getenv('NEWS_API_KEY')
            if not api_key:
                logger.error(f"API key not found in environment variables")
                return {"error": "API key not found in environment variables"}
            return api_key
        except Exception as e:
            logger.error(f"Error occurred while fetching API key: {str(e)}")
            return {"error": "Error occurred while fetching API key"}

    @staticmethod
    def get_news_api_client():
        logger.info(f"Fetching News API client")
        try:
            api_key = Config.get_api_key()
            logger.info(f"Successfully fetched News API client")
            return NewsApiClient(api_key=api_key)
        except Exception as e:
            logger.error(f"Error in fetching News API client: {str(e)}")
            return {"error": "Error in fetching News API client"}
            

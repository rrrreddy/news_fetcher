from dotenv import load_dotenv
import os
from news_fetcher import logger

# Load environment variables from .env file
load_dotenv()

class Google_News_Config:
    def __init__(self):
        pass
    
    
    # apply exception handling for the below functions

    @staticmethod
    def get_api_key():
        try:
            api_key = os.getenv('Google_News_API_Key')
            if api_key is None:
                logger.error("API Key is not set. Please set the NEWS_API_KEY environment variable.")
                raise ValueError("API Key is not set. Please set the NEWS_API_KEY environment variable.")
            logger.info("API Key successfully retrieved")
            return api_key
        except Exception as e:
            logger.error(f"An error occurred while retrieving the API key: {str(e)}")
            raise
    
    
    @staticmethod
    def get_google_news_url():
        try:
            news_url = os.getenv('Google_News_Url')
            return news_url
        except Exception as e:
            logger.error(f"An error occurred while retrieving the Google News URL: {str(e)}")
            raise
    
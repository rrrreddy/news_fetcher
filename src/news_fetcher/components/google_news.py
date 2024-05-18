from news_fetcher import logger
import logging
from news_fetcher.config.configuration import Config
from datetime import datetime


logger = logging.getLogger(__name__)

def fetch_google_news(keywords=None, search_in=None, sources=None, domains=None, exclude_domains=None, from_date=None, to_date=None, language='en', sort_by='publishedAt', page_size=20, page=1):
    """
    Fetch news from Google News API with optional filtering by keywords, language, date range, and other parameters.
    
    :param keywords: Search keywords (default: None)
    :param search_in: Fields to search in (title, description, content)
    :param sources: Comma-separated string of identifiers for news sources or blogs
    :param domains: Comma-separated string of domains to restrict the search to
    :param exclude_domains: Comma-separated string of domains to remove from the results
    :param from_date: Start date for the news (default: None)
    :param to_date: End date for the news (default: None)
    :param language: Language of the news (default: 'en')
    :param sort_by: Sort order of the news (default: 'publishedAt')
    :param page_size: Number of results per page (default: 20)
    :param page: Page number (default: 1)
    :return: JSON response from the API
    """
    newsapi = Config.get_news_api_client()
    logger.info(f"Fetching news from Google News API")
    # Default keyword to ensure the request is valid
    if not keywords and not sources and not domains:
        keywords = "news"  # Default keyword to ensure the request is valid
    
     # Validate and format dates
    def validate_date(date_str):
        if date_str:
            try:
                datetime.fromisoformat(date_str)
                return date_str
            except ValueError:
                logger.error(f"Invalid date format: {date_str}")
                raise ValueError(f"Date input should be in format of either YYYY-MM-DD or YYYY-MM-DDTHH:MM:SS")
        return None

    from_date = validate_date(from_date)
    to_date = validate_date(to_date)

    try:
        response = newsapi.get_everything(
            q=keywords,
            sources=sources,
            domains=domains,
            exclude_domains=exclude_domains,
            from_param=from_date,
            to=to_date,
            language=language,
            sort_by=sort_by,
            page=page,
            page_size=page_size
        )
        logger.info("API request successful")
        if response.get('status') == 'error':
            raise ValueError(response.get('message'))
    except Exception as e:
        logger.error(f"Error in API response: {e}")
        response = {"error": str(e)}
    
    return response

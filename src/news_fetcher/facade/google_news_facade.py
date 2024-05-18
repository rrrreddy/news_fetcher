from news_fetcher import logger
from news_fetcher.components.google_news import fetch_google_news
from news_fetcher.entity.config_entity import GoogleNewsConfig
import logging
from ..components.google_news import fetch_google_news
from ..entity.config_entity import GoogleNewsConfig

logger = logging.getLogger(__name__)

def get_news(keywords=None, search_in=None, sources=None, domains=None, exclude_domains=None, from_date=None, to_date=None, language='en', sort_by='publishedAt', page_size=20, page=1):
    """
    Fetch news with optional filtering by keywords, language, date range, and other parameters.
    """
    news_data = fetch_google_news(keywords, search_in, sources, domains, exclude_domains, from_date, to_date, language, sort_by, page_size, page)
    logger.info(f"Received news data")

    if 'articles' in news_data:
        news_items = [
            GoogleNewsConfig(
                source=article['source']['name'],
                author=article.get('author'),
                title=article['title'],
                description=article['description'],
                url=article['url'],
                urlToImage=article.get('urlToImage'),
                publishedAt=article['publishedAt'],
                content=article.get('content')
            ) for article in news_data['articles']
        ]
        return news_items
    else:
        logger.info("No articles found")
        return {"error": "No articles found"}


from news_fetcher import logger
from news_fetcher.components.google_news import fetch_google_news
from news_fetcher.entity.config_entity import GoogleNewsConfig

def get_news(keywords=None, language='en'):
    """
    Fetch news with optional filtering by keywords, country, language, and date range.
    """
    news_data = fetch_google_news(keywords, language)
    logger.info(f"News data fetched successfully")
    if 'articles' in news_data:
        news_items = [GoogleNewsConfig(article['title'], article['source']['name'], article['description'], article['url']) for article in news_data['articles']]
        logger.info(f"Found {len(news_items)} articles")
        return news_items
    else:
        logger.info(f"No articles found")
        return {"error": "No articles found"}

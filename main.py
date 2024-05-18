from news_fetcher import logger

from news_fetcher.facade.google_news_facade import get_news


logger.info(f"Fetching news")
news = get_news()
logger.info(f"Fetched news")
logger.info(f"News: {news}")

logger.info(f"Done")


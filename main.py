from news_fetcher import logger

from news_fetcher.facade.google_news_facade import get_news

# Fetch news articles
news_data = get_news(keywords='bitcoin', language='en', sort_by='publishedAt')

for article in news_data:
    print(article.title)


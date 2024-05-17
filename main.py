from news_fetcher import logger

from news_fetcher.facade.google_news_facade import get_news

# Fetch latest technology news in English from the United States
news_data = get_news(keywords="technology", language="en")
print(news_data)


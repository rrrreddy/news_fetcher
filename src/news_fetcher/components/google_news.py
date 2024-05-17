from news_fetcher import logger
from news_fetcher.utils.common import make_api_request
from news_fetcher.config.configuration import Google_News_Config

def fetch_google_news(keywords=None, language='en', from_date=None, to_date=None):
    params = {
        'apiKey': Google_News_Config.get_api_key(),
        'language': language,
        'sortBy': 'publishedAt'
    }
    
    if keywords:
        params['q'] = keywords
    if from_date:
        params['from'] = from_date
    if to_date:
        params['to'] = to_date
    
    logger.info(f"API request success for : {Google_News_Config.get_google_news_url()} with params: {params}")
    
    return make_api_request(Google_News_Config.get_google_news_url(), params)

import unittest
from news_fetcher.config.configuration import Config
import os

class TestConfiguration(unittest.TestCase):

    def setUp(self):
        os.environ['NEWS_API_KEY'] = 'test_api_key'

    def test_get_api_key(self):
        api_key = Config.get_api_key()
        self.assertEqual(api_key, 'test_api_key')

    def test_get_news_api_client(self):
        newsapi = Config.get_news_api_client()
        self.assertIsNotNone(newsapi)

if __name__ == '__main__':
    unittest.main()

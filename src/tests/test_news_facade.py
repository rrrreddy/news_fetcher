import unittest
from unittest.mock import patch
from news_fetcher.facade.google_news_facade import get_news
from news_fetcher.entity.config_entity import GoogleNewsConfig

class TestNewsFacade(unittest.TestCase):

    @patch('news_fetcher.facade.google_news_facade.fetch_google_news')
    def test_get_news(self, mock_fetch_google_news):
        mock_fetch_google_news.return_value = {
            'status': 'ok',
            'articles': [{
                'source': {'name': 'Test Source'},
                'author': 'Test Author',
                'title': 'Test Title',
                'description': 'Test Description',
                'url': 'http://test.url',
                'urlToImage': 'http://test.url/image.jpg',
                'publishedAt': '2024-01-01T00:00:00Z',
                'content': 'Test Content'
            }]
        }

        news_items = get_news(keywords='test')
        self.assertIsInstance(news_items, list)
        self.assertEqual(len(news_items), 1)
        self.assertIsInstance(news_items[0], GoogleNewsConfig)
        self.assertEqual(news_items[0].title, 'Test Title')

    @patch('news_fetcher.facade.google_news_facade.fetch_google_news')
    def test_get_news_with_error(self, mock_fetch_google_news):
        mock_fetch_google_news.return_value = {
            'error': 'No articles found'
        }

        news_items = get_news(keywords='test')
        self.assertIsInstance(news_items, dict)
        self.assertIn('error', news_items)
        self.assertEqual(news_items['error'], 'No articles found')

if __name__ == '__main__':
    unittest.main()
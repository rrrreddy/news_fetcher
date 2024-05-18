import unittest
from unittest.mock import patch
from news_fetcher.components.google_news import fetch_google_news

class TestGoogleNews(unittest.TestCase):

    @patch('news_fetcher.components.google_news.Config.get_news_api_client')
    def test_fetch_google_news(self, mock_get_news_api_client):
        mock_api_client = mock_get_news_api_client.return_value
        mock_api_client.get_everything.return_value = {
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

        news_data = fetch_google_news(keywords='test')
        self.assertEqual(news_data['status'], 'ok')
        self.assertEqual(len(news_data['articles']), 1)
        self.assertEqual(news_data['articles'][0]['title'], 'Test Title')

    @patch('src.news_fetcher.components.google_news.Config.get_news_api_client')
    def test_fetch_google_news_with_invalid_api_key(self, mock_get_news_api_client):
        mock_api_client = mock_get_news_api_client.return_value
        mock_api_client.get_everything.return_value = {
            'status': 'error',
            'code': 'apiKeyInvalid',
            'message': 'Your API key is invalid or incorrect.'
        }

        news_data = fetch_google_news(keywords='test')
        self.assertEqual(news_data['error'], 'Your API key is invalid or incorrect.')

if __name__ == '__main__':
    unittest.main()

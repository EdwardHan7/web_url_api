import unittest
from app.main import app

class UrlShortenerTests(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_valid_url_shortening(self):
        response = self.client.post('/shorten_url', json={"long_url": "https://www.quantbe.com/welcome/canada/logs/validate"})
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(data["short_url"].startswith("https://example.co/"))

    def test_invalid_url_format(self):
        response = self.client.post('/shorten_url', json={"long_url": "invalid_url"})
        self.assertEqual(response.status_code, 400)

    def test_empty_url(self):
        response = self.client.post('/shorten_url', json={"long_url": ""})
        self.assertEqual(response.status_code, 400)

if __name__ == "__main__":
    unittest.main()

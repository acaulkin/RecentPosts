import unittest
import json
from api import app

class TestIntegrations(unittest.TestCase):
    def setUp(self):
        """
        This method ensures the app is in testing mode.
        """
        self.app = app.test_client()

    def test_thing(self):
        """
        This method makes sure the response returns 100 posts.
        This is likely the most important test, so it's the one I made :D
        """
        response = self.app.get('/posts')
        assert len(json.loads(response.data)) == 100

if __name__ == "__main__":
    unittest.main()

import unittest
from main import app

class TestFrontend(unittest.TestCase):
    def test_homepage(self):
        response = app.get("/")
        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        response = app.get("/login")
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()

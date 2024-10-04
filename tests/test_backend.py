import unittest
from main import app

class TestBackend(unittest.TestCase):
    def test_get_agents(self):
        response = app.get("/agents/")
        self.assertEqual(response.status_code, 200)

    def test_post_agent(self):
        agent_data = {"name": "Test Agent", "description": "A test agent"}
        response = app.post("/agents/", json=agent_data)
        self.assertEqual(response.status_code, 201)

if __name__ == "__main__":
    unittest.main()

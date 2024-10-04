import unittest
from src.main import main

class TestPrismaPulse(unittest.TestCase):
    def test_conversation_simulation(self):
        try:
            main()
            self.assertTrue(True)  # If no exceptions are raised, the test passes
        except Exception as e:
            self.fail(f"Test failed with exception: {e}")

if __name__ == "__main__":
    unittest.main()

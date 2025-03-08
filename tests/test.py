
import unittest
from main import *
#phase testing
class Test_result(unittest.TestCase):
    def test_coding(self):
        code = self.coding_password("azerty","google.com")
        self.assertEqual(code,"cBgtvA")

if __name__ == "__main__":
    unittest.main
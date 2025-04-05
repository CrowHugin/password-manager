from oop import ressources
import unittest
import string

printable = string.printable

class Test_result(unittest.TestCase):

    def test_coding(self):
        password= ressources.code.coding_password("azerty",printable)
        self.assertEqual(password,"cBgtvA")

    def test_decoding(self):
        decoded_password= ressources.code.decoding_password("cBgtvA",printable)
        self.assertEqual(decoded_password,"azerty")

if __name__ == "__main__":
    unittest.main()
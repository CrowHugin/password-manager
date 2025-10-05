#! /bin/python3


import sys
import os
import string
import unittest

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from ressources.ressources import code

to_remove = ["\t", "\n", "\r", "\x0b", "\x0c", " "]
printable = ''.join(ch for ch in string.printable if ch not in to_remove)


class Test_code(unittest.TestCase):
    def test_coding(self):
        coded_password = code.coding_password("test",printable) 
        self.assertEqual(coded_password,"vguv")
    
    def test_decoding(self):
        decoded_password = code.decoding_password("vguv",printable)
        self.assertEqual(decoded_password,"test")

if __name__ == "__main__":
    unittest.main()

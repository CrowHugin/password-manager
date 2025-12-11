#! /bin/python3
"""
    module to test some functions
"""

import sys
import os
import string
import unittest

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from ressources.ressources import code, json_functions, users

to_remove = ["\t", "\n", "\r", "\x0b", "\x0c", " "]
printable = ''.join(ch for ch in string.printable if ch not in to_remove)

os.system("rm -rf ./pass ./output.txt")


class test_code(unittest.TestCase):
    def test_coding(self):
        coded_password = code.coding_password("test",printable)
        self.assertEqual(coded_password,"vguv")

    def test_decoding(self):
        decoded_password = code.decoding_password("vguv",printable)
        self.assertEqual(decoded_password,"test")

    def test_add(self):
        os.system("./main.py -a -em test@proton.me -w roadmap.sh \
-p password -drun")
        data = json_functions.load_json("./pass")
        self.assertEqual(data["infos"][0]["website"],"roadmap.sh")
        self.assertEqual(data["infos"][0]["email"],"test@proton.me")
        decoded_password = code.decoding_password(data["infos"][0]
                                                  ["password"],printable)
        self.assertEqual(decoded_password,"password")

    def test_view(self):
        os.system("./main.py -v -em test@proton.me -drun >> output.txt") 

        wanted_data = """Used -drun
Showing info for test@proton.me
website: roadmap.sh
password: password
"""
        with open("output.txt","r",encoding="UTF-8") as file:
            content = file.read()
        self.assertEqual(content.strip(),wanted_data.strip())

    def test_create(self):
        #tester si la longueur est correct
        passe = users.create(printable,20)
        passe_ = "".join(passe)

        self.assertEqual(len(passe_),20)


if __name__ == "__main__":
    unittest.main()

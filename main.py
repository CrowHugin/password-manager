# from ressources import users, password, code,stockage
from ressources.ressources import password, view
import argparse
import string
import os
printable = string.printable


def parsing():
    parser = argparse.ArgumentParser()
    parser.add_argument("-view",
                        help = "to view a password with the email or website",
                        action = "store_true")

    parser.add_argument("-add",
                        help = "to add an email and a password",
                        action = "store_true")

    parser.add_argument("-create",
                        help = "to enable the creation od the password, put here your password lenght",
                        action = "store")

    parser.add_argument("-email",
                        help = "to put an email",
                        action = "store")

    parser.add_argument("-password",
                        help = "to put a password",
                        action = "store")



    arguments = parser.parse_args()
    return arguments
#main function
if __name__ == "__main__":
    args = parsing()
    if args.view:
        view.viewing(printable, args.email)
  
    if args.add:
        password.put_password(printable, args.email, args.password)

    if args.create:
        lenght = int(args.create)
        passe = password.create(printable,lenght)
        os.path.join(lenght, "")
        print(passe)
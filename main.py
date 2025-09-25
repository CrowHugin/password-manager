#! /bin/python3

# from ressources import users, password, code,stockage
from ressources.ressources import password, view
import argparse
import string
import sys
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

def check(email,password):
    if email and password:
        return True
    else:
        return False
    


#main function
if __name__ == "__main__":
    args = parsing()
    if args.view:
        if check(args.email,"password") == True:
            view.viewing(printable, args.email)
        else:
            print("ERROR: Missing required email")
  
    elif args.add:
        if check(args.email, args.password) == True:
            password.put_password(printable, args.email, args.password)
        else:
            print("ERROR: email or password not found")
            sys.exit()

    elif args.create:
        lenght = int(args.create)
        passe = password.create(printable,lenght)
        os.path.join(lenght, "")
        print(passe)

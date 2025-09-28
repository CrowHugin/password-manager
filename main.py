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
    parser.add_argument("--view",
                        "-v",
                        help = "to view a password with the email or website",
                        action = "store_true")

    parser.add_argument("--add",
                        "-a",
                        help = "to add an email and a password",
                        action = "store_true")

    parser.add_argument("--create",
                        "-c",
                        help = "to enable the creation od the password, put here your password lenght",
                        action = "store")

    parser.add_argument("--email",
                        "-em",
                        help = "to put an email",
                        action = "store")

    parser.add_argument("--password",
                        "-p",
                        help = "to put a password",
                        action = "store")
    
    parser.add_argument("--website",
                        "-w",
                        help = "Put a website here",
                        action = "store")


    arguments = parser.parse_args()
    return arguments

def check(email,password,website):
    if email and password and website:
        return True
    else:
        return False
    


#main function
if __name__ == "__main__":
    args = parsing()
    if args.view:
        if check(args.email,"password",args.website) == True:
            view.viewing(printable, args.email, args.website)
        else:
            if not args.email and args.website:
                print(f"Showing info for {args.website}")
                view.viewing(printable,"pass", args.website)
            elif not args.website and args.email:
                print(f"Showing info for {args.email}")
                view.viewing(printable,args.email, "pass")
            else:
                print("""ERROR:
Please provide --email or --password with --view""")
                sys.exit()

    elif args.add:
        if check(args.email, args.password, args.website) == True:
            password.put_password(printable, args.email, args.password, 
                                  args.website)
        else:
            if not args.email:
                print("ERROR: Missing required email")
            elif not args.website:
                print("ERROR: Missing required website") 
            elif not args.password:
                print("ERROR: Missing required password")
            sys.exit()

    elif args.create:
        lenght = int(args.create)
        passe = password.create(printable,lenght)
        os.path.join(lenght, "")
    


    else:
        print("""ERROR: 
    use --view (-v), --add (-a) or --create (-c)
    with the following options:
        --email(-em), --password (-p) and/or --website (-w)""")

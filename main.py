#! /bin/python3

# from ressources import users, password, code,stockage
import argparse
import string
import sys
from ressources.ressources import password, view, users
#remove tabs, newlines, carriage returns, vertical tab, form feed, and space.
to_remove = ["\t", "\n", "\r", "\x0b", "\x0c", " "]
printable = ''.join(ch for ch in string.printable if ch not in to_remove)


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
                        help = "to enable the creation od the password,\
                        put here your password lenght",
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

def check(mail,passwrd,website):
    return bool(mail and passwrd and website)




#main function
if __name__ == "__main__":
    args = parsing()
    if args.view:
        if check(args.email,"password",args.website) is True:
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
        if check(args.email, args.password, args.website) is True:
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
        if lenght > 20 or 0 > lenght:
            print("""The password cannot be longer than 20 caratere
please retry""")
            sys.exit()

        passe = users.create(printable,lenght)
        passe = "".join(passe)
        print(f"password: {passe}")
        email, wbsti = users.save_info()
        if check(email,passe,wbsti) is True:
            password.put_password(printable,email,passe,wbsti)



    else:
        print("""ERROR:
    use --view (-v), --add (-a) or --create (-c)
    with the following options:
        --email(-em), --password (-p) and/or --website (-w)""")

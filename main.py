#! /bin/python3

# from ressources import users, password, code,stockage
import argparse
import string
import sys
from ressources.ressources import view, users, code, stockage
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

def view_(eml,passs, wbs):
    if check(eml,passs,wbs) is True:
        view.viewing(printable, eml, wbs)
    else:
        if not eml and wbs:
            print(f"Showing info for {wbs}")
            view.viewing(printable,"pass", wbs)
        elif not wbs and eml:
            print(f"Showing info for {eml}")
            view.viewing(printable,eml, "pass")
        else:
            print("""ERROR:
    Please provide --email or --password with --view""")
            sys.exit()

def add_(eml,passwrd,website):
    if check(eml, passwrd, website) is True:
        cd_pas = code.coding_password(passwrd, printable)
        stockage.stockage(cd_pas, eml,website)
    else:
        if not eml:
            print("ERROR: Missing required email")
        elif not website:
            print("ERROR: Missing required website")
        elif not passwrd:
            print("ERROR: Missing required password")
        sys.exit()

def create_(crt):
    lenght = int(crt)
    if lenght > 20 or 0 > lenght:
        print("""The password cannot be longer than 20 caratere
please retry""")
        sys.exit()

    passe = users.create(printable,lenght)
    passe_ = "".join(passe)
    print(f"password: {passe_}")
    email, wbsti = users.save_info()
    if check(email,passe,wbsti) is True:
        cdc_pass = code.coding_password(passe_,printable)
        stockage.stockage(cdc_pass,email,wbsti)



#main function
if __name__ == "__main__":
    args = parsing()
    if args.view:
        view_(args.email,"password",args.website)

    elif args.add:
        add_(args.email,args.password,args.website)

    elif args.create:
        create_(args.create)

    else:
        print("""ERROR:
    use --view (-v), --add (-a) or --create (-c)
    with the following options:
        --email(-em), --password (-p) and/or --website (-w)""")

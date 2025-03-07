import string
import random

import csv
import os
printable = string.printable
def users_input():

    password = input("rentrez votre mot de passe\n")
    website = input("rentrez le site associé svp\n")
    return password,website

def coding_password(password, table):
    coded_password_list = []
    for cara in password:
        if cara in table:
            ind = table.index(cara)
            coded_password_list.append(table[ind+2])
    coded_password = "".join(coded_password_list)
    print(coded_password)
    return coded_password

def decoding_password(coded_password,printable):
    user_password = coded_password
    for i in coded_password:
        if i in printable:
            ind = printable.index(i)
            new_cara = printable[ind-2]
        user_password = user_password.replace(i,new_cara)
    return user_password

def put_password():
    password,website = users_input()
    coded_password=coding_password(password,printable)
    stockage(coded_password,website)
    decode_password = decoding_password(coded_password,printable)

    # print(f"the password is {password}, the associated website is {website}")
    # print(f"the coded password is {coded_password}, the associated website is {website}")
    # print(f"the coded password is {decode_password}, the associated website is {website}")
    


def choices_users():
    loop = 0
    users_choice = input("""gérérer un mot de passe ?\n
rentrer un mot de passe avec un login ?\n""")
    while loop == 0:
        if users_choice == "1":
            print("please wait for this functionnality to be made")
            loop += 1
            break
        if users_choice == "2":
            put_password()
            loop += 1
        else:
            print(f"""{users_choice} isn't a valid choice\n
please choose a valid one""")
            users_choice = input("""gérérer un mot de passe ?\n
rentrer un mot de passe avec un login ?\n""")



def stockage(mdp,website):
    csv_file = "stockage/stock.csv"
    # print(mdp,website)
    if not os.path.exists(csv_file):
        with open(csv_file, 'w', newline='', encoding="UTF-8") as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(["mdp", "website"])
            file.write(f"{mdp},{website}")
    else:
        with open(csv_file, 'a', newline='', encoding="UTF-8") as file:
            file.write(f"\n{mdp},{website}")


#main function
if __name__ == "__main__":
    choices_users()
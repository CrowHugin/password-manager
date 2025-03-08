import string
import random
import csv
import os


class password:
    def put_password(printable):
        password,website = users.users_input()
        coded_password=code.coding_password(password,printable)
        stockage.stockage(coded_password,website)
        decode_password = code.decoding_password(coded_password,printable)

class users:
    def choices_users(table):
        loop = 0
        users_choice = input("""gérérer un mot de passe ?\n
rentrer un mot de passe avec un login ?\n""")
        while loop == 0:
            if users_choice == "1":
                print("please wait for this functionnality to be made")
                loop += 1
                break
            if users_choice == "2":
                password.put_password(table)
                loop += 1
            else:
                print(f"""{users_choice} isn't a valid choice\n
    please choose a valid one""")
                users_choice = input("""gérérer un mot de passe ?\n
    rentrer un mot de passe avec un login ?\n""")


    def users_input():
        password = input("rentrez votre mot de passe\n")
        website = input("rentrez le site associé svp\n")
        return password,website

class code():
    def coding_password(password, table):
        coded_password_list = []
        for cara in password:
            if cara in table:
                ind = table.index(cara)
                coded_password_list.append(table[ind+2])
        coded_password = "".join(coded_password_list)
        return coded_password

    def decoding_password(coded_password,printable):
        user_password = coded_password
        for i in coded_password:
            if i in printable:
                ind = printable.index(i)
                new_cara = printable[ind-2]
            user_password = user_password.replace(i,new_cara)
        return user_password
    
class stockage:
    def stockage(mdp,website):
        csv_file = "stockage/stock.csv"
        if not os.path.exists(csv_file):
            with open(csv_file, 'w', newline='', encoding="UTF-8") as file:
                writer = csv.writer(file, delimiter=',')
                writer.writerow(["mdp", "website"])
                file.write(f"{mdp},{website}")
        else:
            with open(csv_file, 'a', newline='', encoding="UTF-8") as file:
                file.write(f"\n{mdp},{website}")
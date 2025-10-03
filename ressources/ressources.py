#! /bin/python3

import string
import random
import sys
import csv
import os


class password:
    def put_password(printable, email, mdp, website):
        coded_password=code.coding_password(mdp,printable)
        stockage.stockage(coded_password,email,website)

class users:
    def create(printable,lenght):
        liste = []
        i = 0
        while i  < lenght:
            liste.append(random.choice(printable))
            i +=1

        return liste

    def save_info():
        loop = True
        ans = input("Would you like to save it ?\nY or N\n")

        while loop:
            if ans == "Y" or ans == "y":
                eml = input("With which email adress?\n")
                wbsti = input("on which website?\n")
                loop = False
                return eml, wbsti

            elif ans == "N" or ans == "n":
                print("Please ensure to copy the password")
                return None, None
                loop = False

            else:
                ans = input("Please be sure to put an answer\n")

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
    def stockage(mdp, email, website):
        csv_file = os.path.join(os.path.expanduser('~'),'password-manager')

        if os.path.exists(csv_file):
            with open(f"{csv_file}/stock.csv", 'a', newline='', encoding="UTF-8") as file:
                file.write(f"\n{mdp},{email},{website}")

        if not os.path.exists(csv_file):
            os.system(f"mkdir -p {csv_file}")

            with open(f"{csv_file}/stock.csv", 'w', newline='', encoding="UTF-8") as file:
                writer = csv.writer(file, delimiter=',')
                writer.writerow(["mdp", "email", "website"])
                file.write(f"\n{mdp},{email},{website}")

class password_crea():
    def input_user():
            long = input("How much caratere will be your password ?\n")
            try:
                long = int(long)
            except ValueError:
                print("Please be sure to choose a number")
                sys.exit()
                
            return long
                
                
    def check_input(length):
        if length > 20 or 0 > length: 
            print("The password cannot be longer than 20 caratere\
             please retry\n")
        else:
            return True
    
    def looping():
        loop = 1
        longueur = password_crea.input_user()
        while loop == 1:
            if password_crea.check_input(longueur):
                print(f"The password is {longueur} caratere long")
                loop += 1
            else:
                longueur = password_crea.input_user()
                
class view():    
    def read_file(file, variable, prtable,wnt_srch):
        liste = []
        with open(f"{file}/stock.csv", 'r', newline='',encoding="UTF-8") as file:
            for i in file:
                if variable in i:
                    split = i.split(",")
                    passwrd = split[0]
                    mail = split[1]
                    wbst = split[2].replace("\n"," ")
                    passw = code.decoding_password(passwrd,prtable)
                    if wnt_srch == "email":
                        liste.append(wbst)
                        liste.append(passw)

                    elif wnt_srch == "website":
                        liste.append(mail)
                        liste.append(passw)
                    elif wnt_srch == "both":
                        liste.append(passw)

            for j in liste:
                print(j)



    def viewing(table, email, website):
        csv_file = os.path.join(os.path.expanduser('~'),'password-manager')
        if not os.path.exists("stockage"): #maybe need to change it later
            print("ERROR: make sure to have a stockage file")
            sys.exit()
        else:
            #if email isn't put
            if email == "pass":
                var = website  
                search = "website"            
           
            #if website isn't put
            elif website == "pass":
                var = email
                search = "email"
 
            #if both of them are put
            else:
                var = f"{email},{website}"
                search = "both"

            view.read_file(csv_file, var, table, search)


#! /bin/python3

import random
import json
import sys
import csv
import os



class users():
    @staticmethod
    def create(printable,lenght):
        liste = []
        i = 0
        while i  < lenght:
            liste.append(random.choice(printable))
            i +=1

        return liste

    @staticmethod
    def save_info():
        ans = input("Would you like to save it ?\nY or N\n")

        if ans in ("Y","y"):
            eml = input("With which email adress?\n")
            wbsti = input("on which website?\n")

        elif ans in ("N","n"):
            print("Please ensure to copy the password")
            eml = None
            wbsti = None

        else:
            print("Please be sure to put a correct answer")
            sys.exit()

        return eml, wbsti

class code():
    @staticmethod
    def coding_password(passwrd, table):
        coded_password_list = []
        for cara in passwrd:
            if cara in table:
                # } and ~ are the last two of the list
                # and , is the separator inside the password file
                if cara not in ("}","~",","):
                    ind = table.index(cara)
                    coded_password_list.append(table[ind+2])
                else:
                    if cara == "}":
                        coded_password_list.append("0")
                    elif cara == "~":
                        coded_password_list.append("1")
                    elif cara ==",":
                        coded_password_list.append(".")

        coded_password = "".join(coded_password_list)
        return coded_password

    @staticmethod
    def decoding_password(coded_password,printable):
        user_password = coded_password
        for i in coded_password:
            if i in printable:
                ind = printable.index(i)
                new_cara = printable[ind-2]
                user_password = user_password.replace(i,new_cara)
        return user_password


class json_functions():
    @staticmethod
    def write_json(path_file_):
        os.system(f"mkdir {path_file_}")
        with open(f"{path_file_}/index.json", 'w', encoding="UTF-8") as f:
            data_start={
                    "infos":[]
            }
            json.dump(data_start,f,indent=4)

    @staticmethod
    def add_json(passwrd,email_,website_, path_file_):

        data = {
                "website":f"{website_}",
                "email":f"{email_}",
                "password":f"{passwrd}"
        }

        with open(f"{path_file_}/index.json","r+",encoding="UTF-8") as f:
            file_data = json.load(f)
            file_data["infos"].append(data)
            f.seek(0)
            json.dump(file_data,f,indent=4)

    @staticmethod
    def read_json():
        pass


    @staticmethod
    def check_json():
        pass

class stockage():
    @staticmethod
    def stockage(mdp, email, website,path_file):
        if os.path.exists(f"{path_file}/index.json"):
            json_functions.add_json(mdp,email,website,path_file)

        elif not os.path.exists(f"{path_file}/index.json"):
            json_functions.write_json(path_file)
            json_functions.add_json(mdp,email,website,path_file)




class view():
    @staticmethod
    def read_file(file, variable, prtable,wnt_srch):
        liste = []
        with open(f"{file}/stock.csv", 'r', newline='',
                  encoding="UTF-8") as f:
            for i in f:
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


    @staticmethod
    def viewing(table, email, website, csv_file):
        if not os.path.exists(csv_file): #maybe need to change it later
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

#imprt part
import string
import random

printable = string.printable
def users_input():

    password = input("rentrez votre mot de passe\n")
    website = input("rentrez le site associé svp\n")
    return password,website

def coding_password(password, printable):
    for i in password:
        if i in printable:
            ind = printable.index(i)
            new_cara = printable[ind+2]
        coded_password = password.replace(i,new_cara)
    return coded_password

def decoding_password(coded_password,printable):
    for i in coded_password:
        if i in printable:
            ind = printable.index(i)
            new_cara = printable[ind-2]
        user_password = password.replace(i,new_cara)
    return user_password

if __name__ == "__main__":
    # coding_password("ui",printable)
    password,website = users_input()
    coded_password=coding_password(password,printable)
    decode_password = decoding_password(coded_password,printable)

    print(f"the password is {password}, the associated website is {website}")
    print(f"the coded password is {coded_password}, the associated website is {website}")



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
            password()
            loop += 1
        else:
            print(f"""{users_choice} isn't a valid choice\n
please choose a valid one""")
            users_choice = input("""gérérer un mot de passe ?\n
rentrer un mot de passe avec un login ?\n""")



#main function
if __name__ == "__main__":
    choices_users()

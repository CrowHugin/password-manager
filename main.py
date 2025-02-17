#imprt part
import string
import random

#to get every caractere while coded the password
letters = string.ascii_letters


#defining the functions we need
def users_input():

    password = input("rentrez votre mot de passe\n")
    website = input("rentrez le site associé svp\n")
    return password,website

def randomizing_password(password, letters):
    for i in password:
        
        one_letter = random.choice(letters)
        password = password.replace(i,one_letter)
    return password


#main function
if __name__ == "__main__":

    password,website = users_input()
    coded_password=randomizing_password(password,letters)

    print(f"the password is {password}, the associated website is {website}")
    print(f"the coded password is {coded_password}, the associated website is {website}")

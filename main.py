def users_input():

    password = input("rentrez votre mot de passe\n")
    website = input("rentrez le site associé svp\n")
    return password,website


if __name__ == "__main__":

    password,website = users_input()

print(f"the password is {password}, the associated website is {website}")

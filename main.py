# from ressources import users, password, code,stockage
import ressources.ressources as rs

import string
printable = string.printable

#main function
if __name__ == "__main__":
   rs.users.choices_users(printable)
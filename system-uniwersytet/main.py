
from system_admin import *
from system_wykladowca import *
from system_student import *

import mysql.connector as mysql

db = mysql.connect(host="localhost", user="root", password="", database="uniwersytet_system")

command_handler = db.cursor(buffered=True)

def main():
    print("")
    print("Witamy w systemie Politechniki Krakowskiej!")
    print("")

    print("Prosze wybrać opcje logowania.")
    print("1. Student")
    print("2. Wykładowca")
    print("3. Admin")

    wybrana_opcja = input("Numer wybranej opcji: ")
    wybrana_opcja = str(wybrana_opcja)

    if wybrana_opcja == "1":
        print("")
        print("Logowanie jako student")
        print("")
        logowanie_student()
    elif wybrana_opcja == "2":
        print("")
        print("Logowanie jako wykładowca")
        print("")
        logowanie_wykładowca()
    elif wybrana_opcja == "3":
        print("")
        print("Logowanie jako admin")
        print("")
        logowanie_admin()
    else:
        print("")
        print("Została wybrana niewłaściwa liczba")
        print("No valid value")
        main()

main()



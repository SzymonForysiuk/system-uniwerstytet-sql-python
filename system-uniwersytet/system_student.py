from main.py import main


import mysql.connector as mysql

db = mysql.connect(host="localhost", user="root", password="", database="uniwersytet_system")

command_handler = db.cursor(buffered=True)

def student_system(wpisany_studentId):
    print("")
    print("Prosze wybrać opcje.")
    print("1. Wyświetl rejestacje/obecności")
    print("2. Pobierz dane")
    print("3. Wylogowywanie")

    wybrana_opcja = str(input("Numer wybranej opcji: "))

    if wybrana_opcja == "1":
        print("1. Wyświetlanie rejestacji/obecności")
        student_id = wpisany_studentId
        komenda = "SELECT student_id, data, obecnosc FROM obecnosci WHERE student_id ={}.".format(student_id)
        command_handler.execute(komenda)
        records = command_handler.fetchall()
        print("Student_id | Data | Obecność")
        for record in records:
            print(record)
    elif wybrana_opcja == "2":
        print(("Pobieranie danych"))
        student_id = wpisany_studentId
        komenda = "SELECT student_id, data, obecnosc FROM obecnosci WHERE student_id ={}.".format(student_id)
        command_handler.execute(komenda)
        records = command_handler.fetchall()
        print("Student_id | Data | Obecność")
        for record in records:
            with open("obecnosci.txt", "w") as f:
                f.write(str(record) + "\n")
            f.close()
        print()
def logowanie_student():
    print("")
    wpisany_imie = input("Prosze podać imie: ")
    wpisany_imie = str(wpisany_imie)
    wpisane_nazwisko = input("Prosze podać nazwisko: ")
    wpisane_nazwisko = str(wpisane_nazwisko)
    wpisany_student_id = input("Prosze podać student_id: ")
    wpisany_student_id = str(wpisany_student_id)
    dane = (wpisany_imie, wpisane_nazwisko, wpisany_student_id)
    command_handler.execute("SELECT * FROM lista_studentow WHERE imie = %s AND nazwisko = %s AND student_id = %s", dane)
    if command_handler.rowcount <= 0:
        print("Dany student nie istnieje!")
        main()
    else:
        student_system(wpisany_student_id)
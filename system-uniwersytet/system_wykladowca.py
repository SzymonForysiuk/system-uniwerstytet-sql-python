from main.py import main


import mysql.connector as mysql

db = mysql.connect(host="localhost", user="root", password="", database="uniwersytet_system")

command_handler = db.cursor(buffered=True)

def wyklad_system():
    print("")
    print("Prosze wybrać opcje.")
    print("1. Wyświetl studentów")
    print("2. Wpisywanie obecnosci studentowi")
    print("3. Wylogowywanie")

    wybrana_opcja = str(input("Numer wybranej opcji: "))
    if wybrana_opcja == "1":
        print("")
        tabela = ['student_id', 'numer_albumu', 'imie', 'nazwisko', 'kierunek', 'rok_studiow', 'wydzial_id',
                  'dziekan_id']
        print("Wyświetl studentów")
        command_handler.execute("SELECT student_id, imie, nazwisko, kierunek FROM lista_studentow")
        records = command_handler.fetchall()
        print("Wypis studentów")
        for record in records:
            print(record)

    elif wybrana_opcja == "2":
        print("")
        print("Rejestracja obecnosci")
        print("")
        command_handler.execute("SELECT student_id FROM lista_studentow")
        records = command_handler.fetchall()  #
        data = input(str("Data: dzień/miesiąc/rok (DD/MM/RRRR)  :"))
        for record in records:
            record = str(record).replace("'", "")
            record = str(record).replace(",", "")
            record = str(record).replace("(", "")
            record = str(record).replace(")", "")

            status = input(str("Obecność studenta" + str(record) + " (O/N/S) :"))
            dane = (str(record), data, status)
            command_handler.execute("INSERT INTO obecnosci (student_id,data,obecnosc) VALUES (%s,%s,%s)", dane)
            db.commit()
            print(record + " dostał status " + status)
    elif wybrana_opcja == "3":
        print("Wylogowywanie")
        main()
    else:
        print("Niewłaściwy numer")
        wyklad_system()

def logowanie_wykładowca():
    login = "wyklad"  # Domyślny login dla wykładowcy to "wyklad"
    haslo = "haslo"  # Domyślne hasło dla wykładowcy to "haslo"

    wpisany_imie = input("Prosze podać imie: ")
    wpisany_imie = str(wpisany_imie)
    wpisane_nazwisko = input("Prosze podać nazwisko: ")
    wpisane_nazwisko = str(wpisane_nazwisko)
    dane = (wpisany_imie, wpisane_nazwisko)
    command_handler.execute("SELECT * FROM lista_wykladowcow WHERE imie = %s AND nazwisko = %s", dane)
    if command_handler.rowcount <= 0:
        print("Dane wykładowcy nie istnieją!")
        logowanie_wykładowca()
    else:
        wyklad_system()
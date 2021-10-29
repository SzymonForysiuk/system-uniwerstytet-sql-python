from main.py import main


import mysql.connector as mysql

db = mysql.connect(host="localhost", user="root", password="", database="uniwersytet_system")

command_handler = db.cursor(buffered=True)

def admin_system():
    print("")
    print("Prosze wybrać opcje administratora.")
    print("1. Dodawanie student")
    print("2. Zmienienie danych studenta")
    print("3. Dodawanie wykładowcy")
    print("4. Zmienienie danych wykladowcy")
    print("5. Usuwanie studenta")
    print("6. Usuwanie wykładowcy")
    print("7. Dodanie wydziału")
    print("8. Zmienienie danych wydziału")
    print("9. Usunięcie wydziału")
    print("10. Wylogowywanie")

    wybrana_opcja = str(input("Numer wybranej opcji: "))

    if wybrana_opcja == "1":
        print("")
        print("Rejestrowanie studenta")
        print("")

        numer_albumu = str(input("Numer albumu studenta: "))
        imie = str(input("Imie studenta: "))
        nazwisko = str(input("Nazwisko studenta: "))
        kierunek = str(input("Kierunek studenta: "))
        rok = str(input("Rok studiów studenta: "))
        wydzial_id = str(input("ID Wydziału studenta: "))
        dziekan_id = str(input("ID Dziekana Wydziału studenta: "))

        wpisane_dane = (numer_albumu, imie, nazwisko, kierunek, rok, wydzial_id, dziekan_id)
        command_handler.execute(
            "INSERT INTO lista_studentow (numer_albumu,imie,nazwisko,kierunek,rok_studiow,wydzial_id,dziekan_id) VALUES (%s,%s,%s,%s,%s,%s,%s)",
            wpisane_dane)
        numer_albumu = (numer_albumu)
        command_handler.execute("INSERT INTO obecnosci (numer_albumu) VALUES %s", numer_albumu)
        db.commit()
    elif wybrana_opcja == "2":
        numer_albumu_wybranego_studenta = str(input("Numer albumu wybranego studenta:"))
        print("Dana studenta, która ma zostać zmieniona: ")
        print("1. Numer albumu studenta")
        print("2. Imie studenta")
        print("3. Nazwisko studenta")
        print("4. Kierunek studenta")
        print("5. Rok studiów studenta")
        print("6. ID Wydziału studenta")
        print("7. ID Dziekana Wydziału studenta")
        zmiana_dana_studenta = str(input(("Numer wybranej opcji: ")))
        nowa_wartosc = str(input("Nowa wartość: "))
        if zmiana_dana_studenta == "1":
            wartosc = (nowa_wartosc, numer_albumu_wybranego_studenta)
            command_handler.execute("UPDATE lista_studentow SET numer_albumu=%s WHERE numer_albumu=%s", wartosc)
            db.commit()
        elif zmiana_dana_studenta == "2":
            wartosc = (nowa_wartosc, numer_albumu_wybranego_studenta)
            command_handler.execute("UPDATE lista_studentow SET imie=%s WHERE numer_albumu=%s", wartosc)
            db.commit()

        elif zmiana_dana_studenta == "3":
            wartosc = (nowa_wartosc, numer_albumu_wybranego_studenta)
            command_handler.execute("UPDATE lista_studentow SET nazwisko=%s WHERE numer_albumu=%s", wartosc)
            db.commit()

        elif zmiana_dana_studenta == "4":
            wartosc = (nowa_wartosc, numer_albumu_wybranego_studenta)
            command_handler.execute("UPDATE lista_studentow SET kierunek=%s WHERE numer_albumu=%s", wartosc)
            db.commit()

        elif zmiana_dana_studenta == "5":
            wartosc = (nowa_wartosc, numer_albumu_wybranego_studenta)
            command_handler.execute("UPDATE lista_studentow SET rok_studiow=%s WHERE numer_albumu=%s", wartosc)
            db.commit()
        elif zmiana_dana_studenta == "6":
            wartosc = (nowa_wartosc, numer_albumu_wybranego_studenta)
            command_handler.execute("UPDATE lista_studentow SET wydzial_id=%s WHERE numer_albumu=%s", wartosc)
            db.commit()

        elif zmiana_dana_studenta == "7":
            wartosc = (nowa_wartosc, numer_albumu_wybranego_studenta)
            command_handler.execute("UPDATE lista_studentow SET dziekan_id=%s WHERE numer_albumu=%s", wartosc)
            db.commit()
        else:
            print("Została wybrana niewłaściwa liczba")
            admin_system()
    elif wybrana_opcja == "3":
        print("")
        print("Rejestrowanie wykładowcy")
        print("")

        imie = str(input("Imie wykładowcy: "))
        nazwisko = str(input("Nazwisko wykładowcy: "))
        stopien_naukowy = str(input("Stopień naukowy wykładowcy: "))
        przedmiot = str(input("wykładany przedmiot: "))
        wydzial_id = str(input("ID Wydziału na, którym wykładowca wykłada: "))

        wpisane_dane = (imie, nazwisko, stopien_naukowy, przedmiot, wydzial_id)

        command_handler.execute(
            "INSERT INTO lista_wykladowcow (imie,nazwisko,stopien_naukowy,przedmiot,wydzial_id) VALUES (%s,%s,%s,%s,%s)",
            wpisane_dane)
        db.commit()
    elif wybrana_opcja == "4":
        imie_wykladowcy = str(input("Imie wykładowcy: "))
        nazwisko_wykladowcy = str(input("Nazwisko wykładowcy: "))

        print("Dana studenta, która ma zostać zmieniona: ")
        print("1. Imie wykładowcy")
        print("2. Nazwisko wykładowcy")
        print("3. Stopień naukowy wykładowcy")
        print("4. Wykładany przedmiot")
        print("5. ID Wydziału")
        zmiana_dana_wykladowcy = str(input(("Numer wybranej opcji: ")))
        nowa_wartosc = str(input("Nowa wartość: "))
        if zmiana_dana_wykladowcy == "1":
            wartosc = (nowa_wartosc, imie_wykladowcy, nazwisko_wykladowcy)
            command_handler.execute("UPDATE lista_wykladowcow SET imie=%s WHERE imie=%s AND nazwisko=%s", wartosc)
            db.commit()
        elif zmiana_dana_wykladowcy == "2":
            wartosc = (nowa_wartosc, imie_wykladowcy, nazwisko_wykladowcy)
            command_handler.execute("UPDATE lista_wykladowcow SET nazwisko=%s WHERE imie=%s AND nazwisko=%s", wartosc)
            db.commit()

        elif zmiana_dana_wykladowcy == "3":
            wartosc = (nowa_wartosc, imie_wykladowcy, nazwisko_wykladowcy)
            command_handler.execute("UPDATE lista_wykladowcow SET stopien_naukowy=%s WHERE imie=%s AND nazwisko=%s",
                                    wartosc)
            db.commit()

        elif zmiana_dana_wykladowcy == "4":
            wartosc = (nowa_wartosc, imie_wykladowcy, nazwisko_wykladowcy)
            command_handler.execute("UPDATE lista_wykladowcow SET przedmiot=%s WHERE imie=%s AND nazwisko=%s", wartosc)
            db.commit()

        elif zmiana_dana_wykladowcy == "5":
            wartosc = (nowa_wartosc, imie_wykladowcy, nazwisko_wykladowcy)
            command_handler.execute("UPDATE lista_wykladowcow SET wydzial_id=%s WHERE imie=%s AND nazwisko=%s", wartosc)
            db.commit()
        else:
            print("Została wybrana niewłaściwa liczba")
            admin_system()
    elif wybrana_opcja == "5":
        numer_albumu_wybranego_studenta = int(input("Numer albumu wybranego studenta:"))
        czy_na_pewno = str(input("Czy na pewno chcesz usunąć studenta z listy? \n Jeśli tak to napisz 'tak' : "))
        komenda = "DELETE FROM lista_studentow WHERE numer_albumu={}.".format(numer_albumu_wybranego_studenta)
        if czy_na_pewno == "tak":

            command_handler.execute(komenda)
            db.commit()
        else:
            admin_system()
    elif wybrana_opcja == "6":
        imie_wykladowcy = str(input("Imie wykładowcy: "))
        nazwisko_wykladowcy = str(input("Nazwisko wykładowcy: "))
        czy_na_pewno = str(input("Czy na pewno chcesz usunąć wykładowce z listy? \n Jeśli tak to napisz 'tak' : "))
        dane_wykladowcy = (imie_wykladowcy, nazwisko_wykladowcy)
        if czy_na_pewno == "tak":
            command_handler.execute("DELETE FROM lista_wykladowcow WHERE imie=%s AND nazwisko=%s", dane_wykladowcy)
            db.commit()
        else:
            admin_system()
    elif wybrana_opcja == "7":
        print("")
        print("Rejestrowanie nowego wydziału")
        print("")

        nazwa_wydzialu = str(input("Nazwa nowego wydziału: "))
        wydzial_id = str(input("Numer wydziału: "))
        dziekan_imie = str(input("Imie dziekana wydziału: "))
        dziekan_nazwisko = str(input("Nazwisko dziekana wydziału: "))
        dziekan_id = str(input("Numer ID dziekana: "))

        wpisane_dane = (wydzial_id, nazwa_wydzialu, dziekan_imie, dziekan_nazwisko, dziekan_id)

        command_handler.execute(
            "INSERT INTO lista_wydzialow (wydzial_id,nazwa_wydzialu,dziekan_imie,dziekan_nazwisko,dziekan_id) VALUES (%s,%s,%s,%s,%s)",
            wpisane_dane)
        db.commit()
    elif wybrana_opcja == "8":
        numer_wybranego_wydzialu = str(input("Numer ID wybranego wydzialu:"))
        print("Dane wydzialu, które mają zostać zmienione ")
        print("1. Nazwa wydziału ")
        print("2. Numer wydziału")
        print("3. Imie dziekana wydziału")
        print("4. Nazwisko dziekana wydziału")
        print("5. Numer ID dziekana ")
        zmiana_dana_wydzial = str(input(("Numer wybranej opcji: ")))
        nowa_wartosc = str(input("Nowa wartość: "))
        if zmiana_dana_wydzial == "1":
            wartosc = (nowa_wartosc, numer_wybranego_wydzialu)
            command_handler.execute("UPDATE lista_wydzialow SET nazwa_wydzialu=%s WHERE wydzial_id=%s", wartosc)
            db.commit()
        elif zmiana_dana_wydzial == "2":
            wartosc = (nowa_wartosc, numer_wybranego_wydzialu)
            command_handler.execute("UPDATE lista_wydzialow SET wydzial_id=%s WHERE wydzial_id=%s", wartosc)
            db.commit()
        elif zmiana_dana_wydzial == "3":
            wartosc = (nowa_wartosc, numer_wybranego_wydzialu)
            command_handler.execute("UPDATE lista_wydzialow SET dziekan_imie=%s WHERE wydzial_id=%s", wartosc)
            db.commit()
        elif zmiana_dana_wydzial == "4":
            wartosc = (nowa_wartosc, numer_wybranego_wydzialu)
            command_handler.execute("UPDATE lista_wydzialow SET dziekan_nazwisko=%s WHERE wydzial_id=%s", wartosc)
            db.commit()
        elif zmiana_dana_wydzial == "5":
            wartosc = (nowa_wartosc, numer_wybranego_wydzialu)
            command_handler.execute("UPDATE lista_wydzialow SET dziekan_id=%s WHERE wydzial_id=%s", wartosc)
            db.commit()
        else:
            print("Została wybrana niewłaściwa liczba")
            admin_system()
    elif wybrana_opcja == "9":
        numer_wybranego_wydzialu = str(input("Numer ID wybranego wydzialu:"))
        czy_na_pewno = str(input("Czy na pewno chcesz usunąć wydział z listy? \n Jeśli tak to napisz 'tak' : "))
        komenda = "DELETE FROM lista_wydzialow WHERE wydzial_id={}.".format(numer_wybranego_wydzialu)
        if czy_na_pewno == "tak":
            command_handler.execute(komenda)
            db.commit()
        else:
            admin_system()
    elif wybrana_opcja == "10":
        main();
    else:
        print("Nie została wybrana żadna z podanych opcji")
        admin_system()

def logowanie_admin():
    login = "admin"  # Domyślny login dla admina to "admin"
    haslo = "haslo"  # Domyślne hasło dla admina to "haslo"

    wpisany_login = input("Prosze podać login: ")
    wpisany_login = str(wpisany_login)
    wpisane_haslo = input("Prosze podać hasło: ")
    wpisane_haslo = str(wpisane_haslo)

    if wpisany_login == login:
        if wpisane_haslo == haslo:
            print("")
            print("Wpisano poprawne hasło i login")
            admin_system()
        else:
            print("")
            print("Wpisano nie poprawne hasło")
            wpisane_haslo = str(input("Prosze podać hasło ponownie: "))
            if wpisane_haslo == haslo:
                print("")
                print("Wpisano poprawne hasło i login")
                admin_system()
            else:
                print("")
                print("Wpisano nie poprawne hasło")
                wpisane_haslo = str(input("Prosze podać hasło ponownie: "))

                if wpisane_haslo == haslo:
                    print("")
                    print("Wpisano poprawne hasło i login")
                    print("")
                    admin_system()
                else:
                    print("")
                    print("Wpisano nie poprawne hasło")
                    print("Powrót do menu głównego")
                    main()

    else:
        print("Wpisano nie poprawny login")
        logowanie_admin()
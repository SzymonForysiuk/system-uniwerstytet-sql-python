import mysql.connector as mysql

db = mysql.connect(host="localhost", user="root", password="", database="uniwersytet_system")

command_handler = db.cursor(buffered=True)

# Tworzenie tabeli lista_studentow
command_handler.execute("CREATE TABLE lista_studentow("
                        "student_id INT PRIMARY KEY,"
                        "numer_albumu INT,"
                        "imie VARCHAR(25),"
                        "nazwisko VARCHAR(25),"
                        "kierunek VARCHAR(25),"
                        "rok_studiow INT,"
                        "wydzial_id INT,"
                        "dziekan_id INT"
                        ")")
db.commit()

# Tworzenie tabeli lista_wykladowcow
command_handler.execute("CREATE TABLE lista_wykladowcow("
                        "wykladowca_id INT PRIMARY KEY,"
                        "imie VARCHAR(25),"
                        "nazwisko VARCHAR(25),"
                        "stopien_naukowy VARCHAR(25),"
                        "przedmiot VARCHAR(25),"
                        "wydzial_id INT"
                        ")")
db.commit()

# Tworzenie tabeli lista_wydzialow
command_handler.execute("CREATE TABLE lista_wydzialow("
                        "wydzial_id INT PRIMARY KEY,"
                        "nazwa_wydzialu VARCHAR(25),"
                        "dziekan_imie VARCHAR(25),"
                        "dziekan_nazwisko VARCHAR(25),"
                        "dziekan_id INT"
                        ")")
db.commit()

# Tworzenie tabeli obecnosci
command_handler.execute("CREATE TABLE obecnosci("
                        "student_id INT PRIMARY KEY,"
                        "data DATE,"
                        "obecnosc VARCHAR(1),"  # Obecnosc jest zapisywana jedną literą: O-obecnosc, N-nieobecnosc, S-spóźnienie
                        ")")
db.commit()

# FOREIGN KEY
#lista_studentow
command_handler.execute("ALTER TABLE lista_studentow ADD FOREIGN KEY (wydzial_id) REFERENCES lista_wydzialow(wydzial_id);")
db.commit()
command_handler.execute("ALTER TABLE lista_studentow ADD FOREIGN KEY (dziekan_id) REFERENCES lista_wydzialow(dziekan_id);")
db.commit()
#lista_wykladowcow
command_handler.execute("ALTER TABLE lista_wykladowcow ADD FOREIGN KEY (wydzial_id) REFERENCES lista_wydzialow(wydzial_id);")
db.commit()
#obecnosci
command_handler.execute("ALTER TABLE obecnosci ADD FOREIGN KEY (student_id) REFERENCES lista_studentow(student_id);")
db.commit()
import os, random, datetime
#banka = {'123123': (['Ime i prezime', 'Domagoj Jug'], ['Stanje racuna', 11000], ['OIB', 7854785478])}
banka = {}
id = 0
povijest_transakcija = {}
valuta = '€'

#izbornik
def izbornik(postojeci, broj_kartice):
    if postojeci:
        print("*" * 60)
        print(f"Dobrodošli natrag, {banka[broj_kartice][0][1]}!")
        print("\nIzbornik: ")
        print("\t1. Otvaranje računa banke")
        print("\t2. Prikaz stanja računa")
        print("\t3. Prikaz prometa po računu")
        print("\t4. Polog novca na račun")
        print("\t5. Podizanje novca s računa")
        print("\t6. Povratak u log-in screen")
        print("\t7. Izlazak iz aplikacije")
    else:
        print("*" * 60)
        print("NISTE KORISNIK NAŠE BANKE. ZA POČETAK OTVORITE BANKOVNI RAČUN")
        print("\nIzbornik: ")
        print("\t1. Otvaranje računa banke")
        print("\t6. Povratak u log-in screen")
        print("\t7. Izlazak iz aplikacije")

#funkcija provjere - provjerava ima li korisnik registriran racun u banci
def provjera_korisnika(broj_kartice):
    if broj_kartice in banka.keys():
        #print(f"Dobrodošli natrag, {banka[broj_kartice][0][1]}!")
        return True
    else:
        print("Krivi unos! Ako nemate postojeći račun u banci, odaberite 1.")
        print("Ako imate račun u našoj banci, odaberite 6. kako biste ponovno unesli broj kartice.")
        return False

#otvaranje računa tvrtke
def otvaranje_racuna():
    os.system('cls')
    global banka
    print("*" * 60)
    print("\t\t*OTVARANJE BANKOVNOG RAČUNA*")
    broj = random.randint(1000, 9999)
    broj_racuna = str(broj)
    print("Ako želite izaći iz trenutačnog odabira, upišite 'q'")
    ime_i_prezime = input("Unesite Vaše ime i prezime: ")
    if ime_i_prezime == 'q':
        return
    polog = input("Koliko iznos želite položiti (€): ")
    if polog == 'q':
        return
    oib = ''
    while len(oib) != 11:
        oib = input("Unesite OIB: ")
        if oib == 'q':
            return
        elif len(oib) != 11:
            print("\nVaš OIB mora imati 11 znamenki!")
        else:
            int(oib)
    print("\nNAKON DODJELJENOG BROJA KARTICE, ULOGIRAJTE SE SA BROJEM SVOJE KARTICE!")
    print("Vaš dodjeljeni broj kartice je: ", broj_racuna)
    banka[broj_racuna] = ['Ime i prezime', ime_i_prezime], ['Stanje računa', float(polog)], ['OIB', int(oib)]
    povijest_transakcija[id+1] = [(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day, float(polog), banka[broj_racuna][1][1], banka[broj_racuna][0][1], 'Ulog kod otvaranja računa')]
    input("\n\n\t\tZA NASTAVAK PRITISNITE ENTER!")


#prikaz stanja računa
def prikaz_stanja_računa(postojeci):#treba nam broj racuna ako tvrtka ima vise racuna u banci, ako nema ne treba
    os.system('cls')
    print("*" * 60)
    print("\n\t\t*PRIKAZ STANJA RAČUNA*")
    if postojeci:
        for kljuc, vrijednost in banka.items():
            print(f'\nBROJ RAČUNA: {kljuc}')
            print(f"{vrijednost[0][0].upper()}: {vrijednost[0][1]}")
            print(f"{vrijednost[1][0].upper()}: {vrijednost[1][1]:.2f}{valuta}")
            print(f"{vrijednost[2][0].upper()}: {vrijednost[2][1]}")
            input("\n\n\t\tZA NASTAVAK PRITISNITE ENTER!")
            #ili kraće:
            """for vrijednost in vrijednost:
                print(f"{vrijednost[0]}: {vrijednost[1]}")"""#ali se onda ne moze stavit euro pokraj iznosa stanja racuna
    else:
        print("\nNemate otvoren račun u banci!")
        input("\n\n\t\tZA NASTAVAK PRITISNITE ENTER!")

#prikaz prometa po računu
def prikaz_prometa(postojeci):
    os.system('cls')
    print("*" * 60)
    print(f"*POVIJEST TRANSAKCIJA NA DAN {datetime.datetime.now()}*")
    if postojeci:
        print()
        for kljuc, vrijednost in povijest_transakcija.items():

            print(f"\nBroj transakcije: {kljuc}")
            print(f"Dan/Mjesec/Godina: {vrijednost[0][2]}/{vrijednost[0][1]}/{vrijednost[0][0]}")
            print(f"Iznos: {vrijednost[0][3]:.2f}{valuta}")
            print(f"Trenutačno stanje: {vrijednost[0][4]:.2f}{valuta}")
            print(f"Korisnik: {vrijednost[0][5]}")
            print(f"Opis: {vrijednost[0][6]}")
        input("\n\n\t\tZA NASTAVAK PRITISNITE ENTER!")
    else:
        print("\nNemate otvoren račun u našoj banci!")
        input("\n\n\t\tZA NASTAVAK PRITISNITE ENTER!")

#polog novca na račun
def polog_novca(broj_kartice, postojeci):
    global banka
    global povijest_transakcija
    os.system('cls')
    print("*" * 60)
    print("*POLOG NOVCA NA BANKOVNI RAČUN*")
    if postojeci:
        while True:
            print(f"\nTrenutačno stanje Vašeg računa je {banka[broj_kartice][1][1]}€")
            print("Unesite 'q' za izlaz.")
            polog = input("\nUNESITE IZNOS KOJI ŽELITE POLOŽITI NA VAŠ RAČUN: ")
            if polog.isdigit():
                banka[broj_kartice][1][1] = banka[broj_kartice][1][1] + int(polog)
                opis = 'Polog novca'
                for key in povijest_transakcija.keys():
                    a = key
                zadnji_id = int(a)
                povijest_transakcija[zadnji_id+1] = [(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day, float(polog), banka[broj_kartice][1][1], banka[broj_kartice][0][1], opis)]
                print(f"Uspješan polog!")
                print(f"\n\t\t*NOVO STANJE RAČUNA: {banka[broj_kartice][1][1]:.2f}{valuta}")
                input("\n\n\t\tZA NASTAVAK PRITISNITE ENTER!")
                return
            elif polog == 'q':
                break
            else:
                print("Krivi unos!")
    else:
        print("\nNemate račun u banci. Otvorite novi račun!")
        input("\n\n\t\tZA NASTAVAK PRITISNITE ENTER!")
    

#podizanje novca s računa
def podizanje_novca(postojeci, broj_kartice):#moze biti jos uvjetovano sa brojem kartice
    global banka
    global povijest_transakcija
    os.system('cls')
    print("*" * 60)
    print("*PODIZANJE NOVCA SA BANKOVNOG RAČUNA*")
    if postojeci:
        print(f"\nTrenutačno stanje Vašeg računa je {banka[broj_kartice][1][1]:.2f}€")
        iznos = input("\nUNESITE IZNOS KOJI ŽELITE PODIĆI SA VAŠEG RAČUNA: ")
        if float(iznos) > banka[broj_kartice][1][1]:
            print("Ne možete podići toliko iznos jer prelazite iznos na Vašem računu!")
            input("\n\n\t\tZA NASTAVAK PRITISNITE ENTER!")
        else:
            banka[broj_kartice][1][1] = banka[broj_kartice][1][1] - float(iznos)
            opis = 'Podizanje novca'
            for key in povijest_transakcija.keys():
                    a = key
            zadnji_id = int(a)
            povijest_transakcija[zadnji_id+1] = [(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day, float(iznos), banka[broj_kartice][1][1], banka[broj_kartice][0][1], opis)]
            print(f"\n\t\t*NOVO STANJE RAČUNA: {banka[broj_kartice][1][1]}{valuta}")
            input("\n\n\t\tZA NASTAVAK PRITISNITE ENTER!")
    else:
        print("\nNemate račun u banci. Otvorite novi račun!")
        input("\n\n\t\tZA NASTAVAK PRITISNITE ENTER!")
    


def main():
    aktivnost = True
    while aktivnost:
        os.system('cls')
        print("*" * 60)
        print("\n\t\t\tDOBRODOŠLI U NAŠU BANKU!")
        print("\nAko ste korisnik naše banke, unesite broj kartice. Ako niste korisnik naše banke, unesite '1'.")
        broj_kartice = input("Unesite Vaš broj kartice: ")
        if broj_kartice == '1':
            postojeci = False
        else:
            postojeci = provjera_korisnika(broj_kartice)
        glavni_izbornik = True
        while glavni_izbornik:
            os.system('cls')
            izbornik(postojeci, broj_kartice)
            odabir = int(input("\nOdaberite redni broj ispred ponuđenih opcija: "))
            if odabir == 1:
                otvaranje_racuna()
            elif odabir == 2:
                prikaz_stanja_računa(postojeci)
            elif odabir == 3:
                prikaz_prometa(postojeci)
            elif odabir == 4:
                polog_novca(broj_kartice, postojeci)
            elif odabir == 5:
                podizanje_novca(postojeci, broj_kartice)
            elif odabir == 6:
                glavni_izbornik = False
            elif odabir == 7:
                print("Kraj rada.")
                return

main()
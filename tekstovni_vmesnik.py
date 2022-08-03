from model import Stanje, Trening, Vaja, Vaja_ponovitev

IME_DATOTEKE = "tekstovni.json"
try:
    stanje = Stanje.preberi_iz_datoteke(IME_DATOTEKE)
except FileNotFoundError:
    stanje = Stanje(treningi=[], vaje=[])

def preberi_stevilo():
    while True:
        vnos = input("> ")
        try:
            return int(vnos)
        except ValueError:
            print("Vnesti morate število.")

def izberi_moznost(moznosti):
    """Uporabniku našteje možnosti ter vrne izbrano."""
    for i, (_moznost, opis) in enumerate(moznosti, 1):
        print(f"{i}) {opis}")
    while True:
        i = preberi_stevilo()
        if 1 <= i <= len(moznosti):
            moznost, _opis = moznosti[i - 1]
            return moznost
        else:
            print(f"Vnesti morate število med 1 in {len(moznosti)}.")

# od tu nazaj ne spreminjaj!

def izberi_vajo_v_treningu(trening):
    print("Izberite vajo: ")
    return izberi_moznost(
        [(vaja_ponovitev, vaja_ponovitev.ime) for vaja_ponovitev in trening.vaje_ponovitev]
    )    

def dodaj_vajo_ponovitev(trening):
    print("Dodajte vajo:")
    vaja = izberi_moznost(
        [
            (vaja, vaja.ime) for vaja in stanje.vaje
        ]
    )
    print("Stevilo ponovitev")
    ponovitev = preberi_stevilo()
    vaja_ponovitev = Vaja_ponovitev(vaja.ime, vaja.opis, ponovitev)
    trening.dodaj_vajo_ponovitev(vaja_ponovitev)


def zacetni_pozdrav():
    print("Pozdravljeni v programu za telesno vadbo!")


def ustvari_trening():
    if len(stanje.vaje) == 0:
        print("Zal nimate nobene vaje, zato ne morete ustvariti treninga. \nNajprej ustvarite nekaj vaj, nato boste iz njih lahko sestavili trening.")
    else:    
        print("Vnesite podatke novega treninga.")
        ime = input("Ime> ")
        nov_trening = Trening(ime, [])
        stanje.ustvari_trening(nov_trening)
        dokoncaj_trening(nov_trening)

def dokoncaj_trening(trening):
    dodaj_vajo_ponovitev(trening)

def ustvari_vajo():
    print("Vnesite podatke nove vaje.")
    ime = input("Ime> ")
    opis = input("Opis> ")
    nova_vaja = Vaja(ime, opis)
    stanje.ustvari_vajo(nova_vaja)

def izbrisi_vajo(vaja):
    vaje = stanje.vaje
    id_vaje = vaje.index(vaja)
    stanje.izbrisi_vajo(id_vaje)

def preglej_vajo(vaja):
    print(f"Ime vaje: {vaja.ime}\nOpis vaje: {vaja.opis}\nAli zelis izbrisati vajo?")
    izbrano_dejanje = izberi_moznost(
            [
                (izbrisi_vajo, "Ja"),
                (hvala_vseeno, "Ne"),
            ]
        )
    izbrano_dejanje(vaja)

def pobrisi_trening(trening):
    treningi = stanje.treningi
    id_treninga = treningi.index(trening)
    stanje.pobrisi_trening(id_treninga)

def hvala_vseeno(nepotrebno=1):
    print("OK")

def preglej_vaje():
    if not stanje.vaje:
        print(
            "Trenutno nimate še nobene vaje."
        )
        print("Bi radi ustvarili vajo?")
        izbrano_dejanje = izberi_moznost(
            [
                (ustvari_vajo, "Ja"),
                (hvala_vseeno, "Ne"),
            ]
        )
        izbrano_dejanje()
    else:
        vaja = izberi_moznost(
        [
            (vaja, vaja.ime) for vaja in stanje.vaje
        ]
        )
        preglej_vajo(vaja)

def treniraj(trening):
    dejanje = izberi_moznost(
        [
            (prikazi_trening, "Start")
        ]
        )
    dejanje(trening)

def prikazi_trening(trening):
    print("Vaje:")
    for vaja in trening.vaje_ponovitev:
        print(f"{vaja.ime}, {vaja.ponovitve} krat")
    dejanje = izberi_moznost(
        [
            (koncaj_trening, "Koncaj s treningom")
        ]
        )
    dejanje(trening)

def koncaj_trening(trening):
    print("Priden!")
    
    

def odvzemi_vajo(trening):
    vaje = trening.vaje_ponovitev
    if len(vaje) == 0:
        return print("Ta trening nima nobene vaje")
    else:
        vaja = izberi_vajo_v_treningu(trening)
        vaje = trening.vaje_ponovitev
        id_vaje = vaje.index(vaja)
        trening.odstrani_vajo_ponovitev(id_vaje)
    

def preglej_treninge():
    if not stanje.treningi:
        print(
            "Trenutno nimate še nobenega treninga."
        )
        print("Bi radi ustvarili trening?")
        izbrano_dejanje = izberi_moznost(
            [
                (ustvari_trening, "Ja"),
                (hvala_vseeno, "Ne"),
            ]
        )
        izbrano_dejanje()
    else:
        print("Izberite trening:")
        trening = izberi_moznost(
            [
                (trening, trening.ime) for trening in stanje.treningi
            ]
        )
        preglej_trening(trening)
   
def preglej_trening(trening):
    print("Kaj bi radi naredili?")
    izbrano_dejanje = izberi_moznost(
            [
                (dokoncaj_trening, "dodal vajo"),
                (odvzemi_vajo, "odvzel vajo"),
                (zacni_trening, "treniral")
            ]
        )
    izbrano_dejanje(trening)
    
def zacni_trening(trening):
    print('Ne pozabi se ogreti!')
    return treniraj(trening)

def zakljuci_izvajanje():
    stanje.shrani_v_datoteko(IME_DATOTEKE)
    print("Zapomni si: Mens sana in corpore sano! \nNasvidenje!")
    exit()

def ponudi_moznosti():
    print("Kaj bi radi naredili?")
    izbrano_dejanje = izberi_moznost(
        [
            (preglej_treninge, "pregledal treninge"),
            (ustvari_trening, "ustvaril trening"),
            (preglej_vaje, "pregledal vaje"),
            (ustvari_vajo, "ustvaril vajo"),
            (zakljuci_izvajanje, "odšel iz programa"),
        ]
    )
    izbrano_dejanje()

def tekstovni_vmesnik():
    zacetni_pozdrav()
    while True:
        ponudi_moznosti()

tekstovni_vmesnik()

# from datetime import date
from model import Stanje, Trening, Vaja

# IME_DATOTEKE = "stanje.json"
# try:
#     stanje = Stanje.preberi_iz_datoteke(IME_DATOTEKE)
# except FileNotFoundError:
#     stanje = Stanje(treningi=[], vaje=[])

stanje = Stanje([],[])

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


def prikaz_treninga(trening):
    return f"{trening.ime.upper()}"
    # zamujena = kategorija.stevilo_zamujenih()
    # neopravljena = kategorija.stevilo_neopravljenih()
    # if zamujena:
    #     return f"{kategorija.ime.upper()} (!!{zamujena}!! / {neopravljena})"
    # else:
    #     return f"{kategorija.ime.upper()} ({neopravljena})"


def prikaz_vaje(vaja):
    print(vaja.ime)
    print(vaja.opis)
    # if opravilo.opravljeno:
    #     return f"☑︎ {opravilo.opis}"
    # elif opravilo.zamuja():
    #     return f"☐ !!{opravilo.opis}!! ({opravilo.rok})"
    # elif opravilo.rok:
    #     return f"☐ {opravilo.opis} ({opravilo.rok})"
    # else:
    #     return f"☐ {opravilo.opis}"


def izberi_trening(stanje):
    print("Izberite trening:")
    return izberi_moznost(
        [
            (trening, prikaz_treninga(trening))
            for trening in stanje.treningi
        ]
    ) 


def izberi_vajo():
    print("Izberite vajo:")
    return izberi_moznost(
        [(vaja, vaja.ime) for vaja in stanje.vaje]
    )


def zacetni_pozdrav():
    print("Pozdravljeni v programu za telesno vadbo!")


def ustvari_trening():
    print("Vnesite podatke novega treninga.")
    ime = input("Ime> ")
    vaje = izberi_vajo()
    nov_trening = Trening(ime, vaje)
    stanje.ustvari_trening(nov_trening)


def ustvari_vajo():
    # kategorija = izberi_trening(stanje)
    print("Vnesite podatke nove vaje.")
    ime = input("Ime> ")
    opis = input("Opis> ")
    # rok = input("Rok (YYYY-MM-DD)> ")
    # if rok.strip():
    #     rok = date.fromisoformat(rok)
    # else:
    #     rok = None
    nova_vaja = Vaja(ime, opis)
    stanje.ustvari_vajo(nova_vaja)

def potrdi_izbris(opravilo, kategorija):
    print("Ali zelite izbrisati opravilo?")
    return izberi_moznost(
        [
            (kategorija.izbrisi_opravilo(opravilo), "Ja"),
            (print('Opravilo bo ostalo'), "Ne"),
        ]
    )

# def opravi_opravilo():
#     kategorija = izberi_kategorijo(stanje)
#     if len(kategorija.opravila) == 0:
#         print('Ta kategorija nima opravil.')
#         return opravi_opravilo()
#     opravilo = izberi_opravilo(kategorija)
#     opravilo.opravi()
#     potrdi_izbris(opravilo, kategorija)

def pobrisi_trening():
    trening = izberi_trening(stanje)
    stanje.pobrisi_trening(trening)


def izpisi_trenutno_stanje():
    if not stanje.treningi:
        print(
            "Trenutno nimate še nobenega treninga."
        )
    for trening in stanje.treningi:
        print(f"{prikaz_treninga(trening)}")
    if not stanje.vaje:
        print(
            "Trenutno nimate še nobene vaje."
        )
    for vaja in stanje.vaje:
        print(f"{vaja.ime}")


def zakljuci_izvajanje():
    stanje.shrani_v_datoteko(IME_DATOTEKE)
    print("Nasvidenje!")
    exit()


def ponudi_moznosti():
    print("Kaj bi radi naredili?")
    izbrano_dejanje = izberi_moznost(
        [
            (ustvari_trening, "ustvaril trening"),
            (pobrisi_trening, "pobrisal trening"),
            (ustvari_vajo, "ustvaril novo vajo"),
            (zakljuci_izvajanje, "odšel iz programa"),
        ]
    )
    izbrano_dejanje()




def tekstovni_vmesnik():
    zacetni_pozdrav()
    while True:
        izpisi_trenutno_stanje()
        ponudi_moznosti()


tekstovni_vmesnik()

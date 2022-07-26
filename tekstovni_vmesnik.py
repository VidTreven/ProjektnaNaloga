from model import Stanje

stanje = Stanje()

def tekstovni_vmesnik():
    prikazi_pozdravno_sporocilo()
    while True:
        osnovni_zaslon()

DODAJ_OPRAVILO = 'dodaj'
OPRAVI_OPRAVILO = 'opravi'

def osnovni_zaslon():
    prikazi_aktualna_opravila()
    ukaz = preberi_ukaz()
    if ukaz == DODAJ_OPRAVILO:
        dodaj_opravilo()
    elif ukaz == OPRAVI_OPRAVILO:
        opravi_opravilo()
    ...

def dodaj_opravilo():
    ime = input('Ime opravila> ')
    ...
    opravilo = Opravilo(ime, ...)
    stanje.aktualni_spisek.dodaj_opravilo(opravilo)


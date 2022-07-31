import bottle
from model import Stanje, Vaja_ponovitev, Vaja, Trening

stanje_obj = Stanje([],[])

IME_DATOTEKE = "stanje.json"
try:
    stanje = stanje_obj.preberi_iz_datoteke(IME_DATOTEKE)
except FileNotFoundError:
    stanje = Stanje(treningi=[], vaje=[])

@bottle.get("/")
def zacetna_stran():
    return bottle.template(
        "zacetna_stran.tpl",
        treningi = stanje.treningi 
        )

def url_treninga_uredi(id_treninga):
    return f"/trening/{id_treninga}/uredi/"

def url_vaje():
    return f"/vaje/"

def url_zacetna_stran():
    return f"/"

@bottle.get("/trening/<indeks>/")
def trening(indeks):
    trening = stanje.treningi[int(indeks)]
    return bottle.template(
        "trening.tpl",
        trening = trening,
        vaje_treninga = trening.vaje_ponovitev,
        )

@bottle.get("/trening/<id_treninga>/uredi/")
def trening_uredi(id_treninga):
    trening = stanje.treningi[int(id_treninga)]
    return bottle.template(
        "trening_uredi.tpl",
        trening = trening,
        vaje_treninga = trening.vaje_ponovitev,
        vaje = stanje.vaje
        )

@bottle.get("/trening/<id_treninga>/uredi/izbrisi/")
def trening_izbrisi(id_treninga):
    trening = stanje.treningi[int(id_treninga)]
    stanje.pobrisi_trening(trening)
    stanje.shrani_v_datoteko(IME_DATOTEKE)
    bottle.redirect(url_zacetna_stran)
    

@bottle.post("/trening/<id_treninga>/uredi/odstrani/<id_vaje>/")
def trening_uredi_odstrani(id_treninga, id_vaje):
    trening = stanje.treningi[int(id_treninga)]
    vaja = trening.vaje_ponovitev[int(id_vaje)]
    trening.odstrani_vajo_ponovitev(vaja)
    bottle.redirect(url_treninga_uredi(id_treninga))

@bottle.post("/trening/<id_treninga>/uredi/dodaj/<id_vaje>/")
def trening_uredi_dodaj(id_treninga, id_vaje):
    trening = stanje.treningi[int(id_treninga)]
    vaja = stanje.vaje[int(id_vaje)]
    ponovitve = bottle.request.forms["ponovitve"]
    vaja_ponovitev = Vaja_ponovitev(vaja.ime, vaja.opis, ponovitve)
    trening.dodaj_vajo_ponovitev(vaja_ponovitev)
    stanje.shrani_v_datoteko(IME_DATOTEKE)
    bottle.redirect(url_treninga_uredi(id_treninga))

@bottle.post("/vaje/dodaj/")
def vaje_dodaj():
    ime = bottle.request.forms["ime"]
    opis = bottle.request.forms["opis"]
    vaja = Vaja(ime, opis)
    stanje.ustvari_vajo(vaja)
    stanje.shrani_v_datoteko(IME_DATOTEKE)
    bottle.redirect(url_vaje())

@bottle.post("/trening/dodaj/")
def trening_dodaj():
    ime = bottle.request.forms["ime_treninga"]
    trening = Trening(ime, [])
    stanje.ustvari_trening(trening)
    stanje.shrani_v_datoteko(IME_DATOTEKE)
    treningi = stanje.treningi
    id_treninga = treningi.index(trening)
    bottle.redirect(url_treninga_uredi(id_treninga))

@bottle.get("/vaje/<indeks>/")
def vaje_indeks(indeks):
    return bottle.template(
        "vaja.tpl",
        vaja = stanje.vaje[int(indeks)],
        )

@bottle.get("/vaje/<id_vaje>/izbrisi/")
def vaje_id(id_vaje):
    vaja = stanje.vaje[int(id_vaje)]
    stanje.izbrisi_vajo(vaja)
    stanje.shrani_v_datoteko(IME_DATOTEKE)
    bottle.redirect(url_vaje())

@bottle.get("/nov_trening/")
def nov_trening():
    return bottle.template(
        "nov_trening.tpl",
        vaje = stanje.vaje,
        )

@bottle.get("/vaje/")
def vaje():
    return bottle.template(
        "vaje.tpl",
        vaje = stanje.vaje,
        )



bottle.run(debug=True, reloader=True)
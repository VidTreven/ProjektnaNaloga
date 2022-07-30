import bottle
from model import Stanje

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

@bottle.get("/trening/<indeks>/")
def trening(indeks):
    trening = stanje.treningi[int(indeks)]
    return bottle.template(
        "trening.tpl",
        trening = trening,
        vaje = trening.vaje_ponovitev
        )

@bottle.get("/vaje/<indeks>/")
def vaje_indeks(indeks):
    return bottle.template(
        "vaja.tpl",
        vaja = stanje.vaje[int(indeks)],
        )

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
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

def url_treninga_uredi_novo(id_treninga):
    return f"/trening/{id_treninga}/uredi_novo/"

def url_vaje():
    return f"/vaje/"

def url_zacetna_stran():
    return f"/"

@bottle.get("/trening/<id_treninga>/uredi_novo/")
def trening_uredi(id_treninga):
    trening = stanje.treningi[int(id_treninga)]
    return bottle.template(
        "trening_uredi_novo.tpl",
        trening = trening,
        vaje_treninga = trening.vaje_ponovitev,
        vaje = stanje.vaje
        )

@bottle.post("/trening/<id_treninga>/uredi_novo/dodaj/vecer/")
def trening_uredi_dodaj_prvo(id_treninga):
    trening = stanje.treningi[int(id_treninga)]
    vaja = bottle.request.forms["dodana_vaja"]
    ime_in_opis = vaja.split(',')
    ime = ime_in_opis[0]
    opis = ime_in_opis[1]
    ponovitve = bottle.request.forms["st_ponovitev"]
    vaja_ponovitev = Vaja_ponovitev(ime, opis, ponovitve)
    trening.dodaj_vajo_ponovitev( vaja_ponovitev)
    stanje.shrani_v_datoteko(IME_DATOTEKE)
    bottle.redirect(url_treninga_uredi(id_treninga))

@bottle.get("/trening/<indeks>/")
def trening(indeks):
    trening = stanje.treningi[int(indeks)]
    return bottle.template(
        "trening.tpl",
        trening = trening,
        vaje_treninga = trening.vaje_ponovitev,
        )

@bottle.get("/trening/<id_treninga>/treniraj/")
def trening(id_treninga):
    trening = stanje.treningi[int(id_treninga)]

    return bottle.template(
        "treniraj.tpl",
        trening = trening,
        vaje_treninga = trening.vaje_ponovitev,
        st_vaj = len(trening.vaje_ponovitev),
        id_treninga = int(id_treninga)
        )    

@bottle.get("/trening/<id_treninga>/treniraj/<id_vaje>/")
def trening(id_treninga, id_vaje):
    trening = stanje.treningi[int(id_treninga)]
    vaje_treninga = trening.vaje_ponovitev
    vaja_trenutna = vaje_treninga[int(id_vaje)]
    vaja_naslednja = vaje_treninga[int(id_vaje)+1]
    return bottle.template(
        "treniraj_vajo.tpl",
        trening = trening,
        vaja_trenutna = vaja_trenutna,
        vaja_naslednja = vaja_naslednja,
        id_treninga = int(id_treninga),
        id_trenutne_vaje = int(id_vaje),
        id_naslednje_vaje = int(id_vaje) + 1,
        st_vaj = len(vaje_treninga),
        )  

@bottle.get("/trening/<id_treninga>/treniraj_zadnjo/")
def trening_treniraj_zadnja_vaja(id_treninga):
    trening = stanje.treningi[int(id_treninga)]
    vaje_treninga = trening.vaje_ponovitev
    vaja_trenutna = vaje_treninga[-1]   
    return bottle.template(
        "treniraj_zadnjo_vajo.tpl",
        trening = trening,
        vaja_trenutna = vaja_trenutna,
        id_treninga = int(id_treninga),
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

@bottle.get("/trening/<id_treninga>/uredi/dodaj/<id_vaje>/")
def trening_uredi_dodaj(id_treninga, id_vaje):
    trening = stanje.treningi[int(id_treninga)]
    nasa_vaja = stanje.vaje[int(id_vaje)]
    return bottle.template(
        "trening_uredi_dodaj.tpl",
        trening = trening,
        vaje_treninga = trening.vaje_ponovitev,
        nasa_vaja = nasa_vaja,
        ime_nase_vaje = nasa_vaja.ime,
        )

@bottle.post("/trening/<id_treninga>/uredi/dodaj/vecer/<id_naslednje_vaje>/prosim/")
def trening_uredi_dodaj_pred(id_treninga, id_naslednje_vaje):
    trening = stanje.treningi[int(id_treninga)]
    vaja = bottle.request.forms["dodana_vaja"]
    ime_in_opis = vaja.split(',')
    ime = ime_in_opis[0]
    opis = ime_in_opis[1]
    ponovitve = bottle.request.forms["st_ponovitev"]
    vaja_ponovitev = Vaja_ponovitev(ime, opis, ponovitve)
    trening.vrini_vajo_ponovitev(int(id_naslednje_vaje), vaja_ponovitev)
    stanje.shrani_v_datoteko(IME_DATOTEKE)
    bottle.redirect(url_treninga_uredi(id_treninga))

@bottle.post("/trening/<id_treninga>/uredi/dodaj/vecer/")
def trening_uredi_dodaj_pred(id_treninga):
    trening = stanje.treningi[int(id_treninga)]
    vaja = bottle.request.forms["dodana_vaja"]
    ime_in_opis = vaja.split(',')
    ime = ime_in_opis[0]
    opis = ime_in_opis[1]
    ponovitve = bottle.request.forms["st_ponovitev"]
    vaja_ponovitev = Vaja_ponovitev(ime, opis, ponovitve)
    trening.dodaj_vajo_ponovitev( vaja_ponovitev)
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
    bottle.redirect(url_treninga_uredi_novo(id_treninga))

@bottle.get("/vaje/<indeks>/")
def vaje_indeks(indeks):
    return bottle.template(
        "vaja.tpl",
        vaja = stanje.vaje[int(indeks)],
        )

@bottle.get("/vaje/uredi/<id_vaje>/izbrisi/")
def vaje_id(id_vaje):
    #vaja = stanje.vaje[int(id_vaje)]
    stanje.izbrisi_vajo(int(id_vaje))
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

@bottle.get("/vaje/uredi/")
def vaje_uredi():
    return bottle.template(
        "vaje_uredi.tpl",
        vaje = stanje.vaje,
        )



bottle.run(debug=True, reloader=True)
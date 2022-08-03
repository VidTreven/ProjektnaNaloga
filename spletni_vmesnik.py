import bottle
from model import Stanje, Trening, Vaja_ponovitev, Vaja

# Poskrbim za ustrezno branje in shranjevanje podatkov posameznega uporabnika

SIFRIRNI_KLJUC = "To je poseben šifrirni ključ"

def ime_uporabnikove_datoteke(uporabnisko_ime):
    return f"stanja_uporabnikov/{uporabnisko_ime}.json"

def stanje_trenutnega_uporabnika():
    uporabnisko_ime = bottle.request.get_cookie("uporabnisko_ime", secret=SIFRIRNI_KLJUC)
    if uporabnisko_ime == None:
        bottle.redirect("/prijava/")
    ime_datoteke = ime_uporabnikove_datoteke(uporabnisko_ime)
    try:
        stanje = Stanje([],[]).preberi_iz_datoteke(ime_datoteke)
    except FileNotFoundError:
        stanje = Stanje(treningi=[], vaje=[])
        stanje.shrani_v_datoteko(ime_datoteke)
    return stanje

def shrani_stanje_trenutnega_uporabnika(stanje):
    uporabnisko_ime = bottle.request.get_cookie("uporabnisko_ime", secret=SIFRIRNI_KLJUC)
    ime_datoteke = ime_uporabnikove_datoteke(uporabnisko_ime)
    stanje.shrani_v_datoteko(ime_datoteke)

# Prijava in odjava

@bottle.get("/prijava/")
def prijava_get():
    return bottle.template(
        "prijava.tpl"
    )

@bottle.post("/prijava/")
def prijava_post():
    uporabnisko_ime = bottle.request.forms.getunicode("uporabnisko_ime")
    geslo = bottle.request.forms.getunicode("geslo")
    if uporabnisko_ime == geslo[::-1]:
        bottle.response.set_cookie("uporabnisko_ime", uporabnisko_ime, path="/", secret=SIFRIRNI_KLJUC)
        bottle.redirect("/")
    else:
        return "Napaka ob prijavi"

@bottle.post("/odjava/")
def odjava_post():
    bottle.response.delete_cookie("uporabnisko_ime", path="/")
    bottle.redirect("/")

# Zacetna stran in url-ji za preusmeritve

@bottle.get("/")
def zacetna_stran():
    stanje = stanje_trenutnega_uporabnika()
    return bottle.template(
        "zacetna_stran.tpl",
        treningi = stanje.treningi,
        uporabnisko_ime = bottle.request.get_cookie("uporabnisko_ime", secret=SIFRIRNI_KLJUC) 
        )

def url_treninga_uredi(id_treninga):
    return f"/trening/{id_treninga}/uredi/"

def url_treninga_uredi_novo(id_treninga):
    return f"/trening/{id_treninga}/uredi_novo/"

def url_vaje_uredi():
    return f"/vaje/uredi/"

def url_zacetna_stran():
    return f"/"

# Vaje

@bottle.get("/vaje/")
def vaje():
    stanje = stanje_trenutnega_uporabnika()
    return bottle.template(
        "vaje.tpl",
        vaje = stanje.vaje,
        )

@bottle.get("/vaje/<id_vaje>/")
def vaja(id_vaje):
    stanje = stanje_trenutnega_uporabnika()
    return bottle.template(
        "vaja.tpl",
        vaja = stanje.vaje[int(id_vaje)],
        )

@bottle.get("/vaje/uredi/")
def vaje_uredi():
    stanje = stanje_trenutnega_uporabnika()
    return bottle.template(
        "vaje_uredi.tpl",
        vaje = stanje.vaje,
        )

@bottle.post("/vaje/dodaj/")
def vaje_dodaj():
    stanje = stanje_trenutnega_uporabnika()
    ime = bottle.request.forms["ime"]
    opis = bottle.request.forms["opis"]
    vaja = Vaja(ime, opis)
    napake = stanje.preveri_podatke_nove_vaje(vaja)
    if napake:
        return bottle.template("vaje_uredi_z_napako.tpl",
            ime = ime,
            vaje = stanje.vaje,
            )
    else:
        stanje.ustvari_vajo(vaja)
        shrani_stanje_trenutnega_uporabnika(stanje)
        bottle.redirect(url_vaje_uredi())

@bottle.post("/vaje/uredi/<id_vaje>/izbrisi/")
def vaja_izbrisi(id_vaje):
    stanje = stanje_trenutnega_uporabnika()
    stanje.izbrisi_vajo(int(id_vaje))
    shrani_stanje_trenutnega_uporabnika(stanje)
    bottle.redirect(url_vaje_uredi())

# Treningi

@bottle.get("/trening/<id_treninga>/")
def trening(id_treninga):
    stanje = stanje_trenutnega_uporabnika()
    trening = stanje.treningi[int(id_treninga)]
    return bottle.template(
        "trening.tpl",
        trening = trening,
        vaje_treninga = trening.vaje_ponovitev,
        )

@bottle.get("/trening/<id_treninga>/treniraj/")
def treniraj_trening(id_treninga):
    stanje = stanje_trenutnega_uporabnika()
    trening = stanje.treningi[int(id_treninga)]
    return bottle.template(
        "treniraj.tpl",
        trening = trening,
        vaje_treninga = trening.vaje_ponovitev,
        st_vaj = len(trening.vaje_ponovitev),
        id_treninga = int(id_treninga)
        )

@bottle.get("/trening/<id_treninga>/treniraj/<id_vaje>/")
def treniraj_trening_vajo(id_treninga, id_vaje):
    stanje = stanje_trenutnega_uporabnika()
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
        id_naslednje_vaje = int(id_vaje) + 1,
        st_vaj = len(vaje_treninga),
        ) 

@bottle.get("/trening/<id_treninga>/treniraj_zadnjo/")
def treniraj_trening_zadnjo_vajo(id_treninga):
    stanje = stanje_trenutnega_uporabnika()
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
    stanje = stanje_trenutnega_uporabnika()
    trening = stanje.treningi[int(id_treninga)]
    return bottle.template(
        "trening_uredi.tpl",
        trening = trening,
        vaje_treninga = trening.vaje_ponovitev,
        vaje = stanje.vaje
        )

@bottle.post("/trening/<id_treninga>/uredi/izbrisi/")
def trening_izbrisi(id_treninga):
    stanje = stanje_trenutnega_uporabnika()
    stanje.pobrisi_trening(int(id_treninga))
    shrani_stanje_trenutnega_uporabnika(stanje)
    bottle.redirect(url_zacetna_stran())

@bottle.post("/trening/<id_treninga>/uredi/odstrani/<id_vaje>/")
def trening_uredi_odstrani_vajo(id_treninga, id_vaje):
    stanje = stanje_trenutnega_uporabnika()
    trening = stanje.treningi[int(id_treninga)]
    trening.odstrani_vajo_ponovitev(int(id_vaje))
    shrani_stanje_trenutnega_uporabnika(stanje)
    bottle.redirect(url_treninga_uredi(id_treninga))

@bottle.post("/trening/<id_treninga>/uredi/vrini/<id_naslednje_vaje>/")
def trening_uredi_vrini_vajo_pred(id_treninga, id_naslednje_vaje):
    stanje = stanje_trenutnega_uporabnika()
    trening = stanje.treningi[int(id_treninga)]
    vaja = bottle.request.forms["dodana_vaja"]
    ime_in_opis = vaja.split(',')
    ime = ime_in_opis[0]
    opis = ime_in_opis[1]
    ponovitve = bottle.request.forms["st_ponovitev"]
    vaja_ponovitev = Vaja_ponovitev(ime, opis, ponovitve)
    trening.vrini_vajo_ponovitev(int(id_naslednje_vaje), vaja_ponovitev)
    shrani_stanje_trenutnega_uporabnika(stanje)
    bottle.redirect(url_treninga_uredi(id_treninga))

@bottle.post("/trening/<id_treninga>/uredi/dodaj/")
def trening_uredi_dodaj_vajo(id_treninga):
    stanje = stanje_trenutnega_uporabnika()
    trening = stanje.treningi[int(id_treninga)]
    vaja = bottle.request.forms["dodana_vaja"]
    ime_in_opis = vaja.split(',')
    ime = ime_in_opis[0]
    opis = ime_in_opis[1]
    ponovitve = bottle.request.forms["st_ponovitev"]
    vaja_ponovitev = Vaja_ponovitev(ime, opis, ponovitve)
    trening.dodaj_vajo_ponovitev( vaja_ponovitev)
    shrani_stanje_trenutnega_uporabnika(stanje)
    bottle.redirect(url_treninga_uredi(id_treninga))

@bottle.get("/trening/<id_treninga>/uredi_novo/")
def trening_uredi_novo(id_treninga):
    stanje = stanje_trenutnega_uporabnika()
    trening = stanje.treningi[int(id_treninga)]
    return bottle.template(
        "trening_uredi_novo.tpl",
        trening = trening,
        vaje = stanje.vaje
        )

@bottle.post("/trening/<id_treninga>/uredi_novo/izbrisi/")
def trening_izbrisi_novo(id_treninga):
    stanje = stanje_trenutnega_uporabnika()
    stanje.pobrisi_trening(int(id_treninga))
    shrani_stanje_trenutnega_uporabnika(stanje)
    bottle.redirect(url_zacetna_stran())

@bottle.post("/trening/<id_treninga>/uredi_novo/dodaj_novo/")
def trening_uredi_dodaj_novo(id_treninga):
    stanje = stanje_trenutnega_uporabnika()
    trening = stanje.treningi[int(id_treninga)]
    vaja = bottle.request.forms["dodana_vaja"]
    ime_in_opis = vaja.split(',')
    ime = ime_in_opis[0]
    opis = ime_in_opis[1]
    ponovitve = bottle.request.forms["st_ponovitev"]
    vaja_ponovitev = Vaja_ponovitev(ime, opis, ponovitve)
    trening.dodaj_vajo_ponovitev( vaja_ponovitev)
    shrani_stanje_trenutnega_uporabnika(stanje)
    bottle.redirect(url_treninga_uredi(id_treninga))    

@bottle.get("/nov_trening/")
def nov_trening():
    return bottle.template(
        "nov_trening.tpl",
        )

@bottle.post("/trening/dodaj/")
def trening_dodaj():
    stanje = stanje_trenutnega_uporabnika()
    ime = bottle.request.forms["ime_treninga"]
    trening = Trening(ime, [])
    napake = stanje.preveri_podatke_novega_treninga(trening)
    if napake:
        return bottle.template("nov_trening_z_napako.tpl",
            ime = ime)
    else:
        stanje.ustvari_trening(trening)
        shrani_stanje_trenutnega_uporabnika(stanje)
        treningi = stanje.treningi
        id_treninga = treningi.index(trening)
        bottle.redirect(url_treninga_uredi_novo(id_treninga))

# Pogon

bottle.run(debug=True, reloader=True)
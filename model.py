import json


class Stanje:
    def __init__(self, treningi, vaje):
        self.treningi = treningi
        self.vaje = vaje

    def ustvari_trening(self, trening):
        self.treningi.append(trening)
        # return len(self.treningi) - 1

    def pobrisi_trening(self, id_treninga):
        self.treningi.pop(id_treninga)

    def preveri_podatke_novega_treninga(self, nov_trening):
        for trening in self.treningi:
            if trening.ime == nov_trening.ime:
                return True

    
    def ustvari_vajo(self, vaja):
        self.vaje.append(vaja)
        # return len(self.treningi) - 1

    def izbrisi_vajo(self, id_vaje):
        self.vaje.pop(id_vaje)
        # return Stanje

    def preveri_podatke_nove_vaje(self, nova_vaja):
        for vaja in self.vaje:
            if vaja.ime == nova_vaja.ime:
                return True





    def v_slovar(self):
        return {
            "treningi": [trening.v_slovar() for trening in self.treningi],
            "vaje": [vaja.v_slovar() for vaja in self.vaje],
        }

    @staticmethod
    def iz_slovarja(slovar):
        stanje = Stanje(
            [
                Trening.iz_slovarja(sl_treningi)
                for sl_treningi in slovar["treningi"]
            ], 
            [
                Vaja.iz_slovarja(sl_vaje)
                for sl_vaje in slovar["vaje"]
            ]
        )
        return stanje

    def shrani_v_datoteko(self, ime_datoteke):
        with open(ime_datoteke, "w") as dat:
            slovar = self.v_slovar()
            json.dump(slovar, dat, indent=4, ensure_ascii=False)

    @staticmethod
    def preberi_iz_datoteke(ime_datoteke):
        with open(ime_datoteke) as dat:
            slovar = json.load(dat)
            return Stanje.iz_slovarja(slovar)


class Trening:
    def __init__(self, ime, vaje_ponovitev):
        self.ime = ime
        self.vaje_ponovitev = vaje_ponovitev

    def dodaj_vajo_ponovitev(self, vaja_ponovitev):
        self.vaje_ponovitev.append(vaja_ponovitev)

    def vrini_vajo_ponovitev(self, naslednik, vaja_ponovitev,):
        self.vaje_ponovitev.insert(naslednik, vaja_ponovitev)

    def odstrani_vajo_ponovitev(self, id_vaja_ponovitev):
        self.vaje_ponovitev.pop(id_vaja_ponovitev)

    def v_slovar(self):
        return {
            "ime": self.ime,
            "vaje_ponovitev": [vaja_ponovitev.v_slovar() for vaja_ponovitev in self.vaje_ponovitev],
        }

    @staticmethod
    def iz_slovarja(slovar):
        return Trening(
            slovar["ime"],
            [Vaja_ponovitev.iz_slovarja(sl_vaje_ponovitev) for sl_vaje_ponovitev in slovar["vaje_ponovitev"]],
       )


class Vaja_ponovitev:
    def __init__(self, ime, opis, ponovitve):
        self.ime = ime
        self.opis = opis
        self.ponovitve = ponovitve
        
    def v_slovar(self):
        return {
            "ime": self.ime,
            "opis": self.opis,
            "ponovitve": self.ponovitve
        }

    @staticmethod
    def iz_slovarja(slovar):
        return Vaja_ponovitev(
            slovar["ime"],
            slovar["opis"],
            slovar["ponovitve"],
        )

class Vaja:
    def __init__(self, ime, opis):
        self.ime = ime
        self.opis = opis

    def v_slovar(self):
        return {
            "ime": self.ime,
            "opis": self.opis,
        }

    @staticmethod
    def iz_slovarja(slovar):
        return Vaja(
            slovar["ime"],
            slovar["opis"],
        )
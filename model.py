# from datetime import date
import json


class Stanje:
    def __init__(self, treningi, vaje):
        self.treningi = treningi
        self.vaje = vaje

    def ustvari_trening(self, trening):
        self.treningi.append(trening)
        # return len(self.treningi) - 1

    def pobrisi_trening(self, trening):
        self.treningi.remove(trening)

    def preveri_podatke_novega_trenigna(self, nov_trening):
        for trening in self.treningi:
            if trening.ime == nov_trening.ime:
                return {"ime": "Trening s tem imenom že obstaja"}

    
    def ustvari_vajo(self, vaja):
        self.vaje.append(vaja)
        # return len(self.treningi) - 1

    def izbrisi_vajo(self, vaja):
        self.vaje.remove(vaja)

    def preveri_podatke_nove_vaje(self, nova_vaja):
        for vaja in self.vaje:
            if vaja.ime == nova_vaja.ime:
                return {"ime": "Vaja s tem imenom že obstaja"}





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
    def __init__(self, ime, vaje):
        self.ime = ime
        self.vaje = vaje

    # def stevilo_neopravljenih(self):
    #     neopravljena = 0
    #     for opravilo in self.opravila:
    #         if not opravilo.opravljeno:
    #             neopravljena += 1
    #     return neopravljena

    def dodaj_vajo(self, vaja):
        self.vaje.append(vaja)

    def odstrani_vajo(self, vaja):
        self.vaje.remove(vaja)

    # def stevilo_zamujenih(self):
    #     zamujena = 0
    #     for opravilo in self.opravila:
    #         if opravilo.zamuja():
    #             zamujena += 1
    #     return zamujena

    def v_slovar(self):
        return {
            "ime": self.ime,
            "vaje": [vaja.v_slovar() for vaja in self.vaje],
        }

    @staticmethod
    def iz_slovarja(slovar):
        return Trening(
            slovar["ime"],
            [Vaja.iz_slovarja(sl_vaje) for sl_vaje in slovar["vaje"]],
       )


class Vaja:
    def __init__(self, ime, opis):
        self.ime = ime
        self.opis = opis



    # def opravi(self):
    #     self.opravljeno = True

    # def zamuja(self):
    #     rok_pretekel = self.rok and self.rok < date.today()
    #     return not self.opravljeno and rok_pretekel

    def v_slovar(self):
        return {
            "ime": self.ime,
            "opis": self.opis,
            #"rok": self.rok.isoformat() if self.rok else None,
            #"opravljeno": self.opravljeno,
        }

    @staticmethod
    def iz_slovarja(slovar):
        return Vaja(
            slovar["ime"],
            slovar["opis"],
            #date.fromisoformat(slovar["rok"]) if slovar["rok"] else None,
            #slovar["opravljeno"],
        )
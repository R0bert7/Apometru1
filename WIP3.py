class AdministrareCitiriApa:
    def __init__(self):
        self.citiri = {}

    def adauga_citire(self, an, luna, apa_rece, apa_calda):
        cheie = (an, luna)

        if cheie in self.citiri:
            print("Eroare: Citirea pentru această lună există deja.")
            return

        if self.validare_citire(an, luna, apa_rece, apa_calda):
            self.citiri[cheie] = {'apa_rece': apa_rece, 'apa_calda': apa_calda}
            print("Citire adăugată cu succes.")
        else:
            print("Eroare: Datele introduse nu sunt valide.")

    def sterge_citire(self, an, luna):
        cheie = (an, luna)

        if cheie in self.citiri:
            del self.citiri[cheie]
            print("Citire ștearsă cu succes.")
        else:
            print("Eroare: Nu există o citire pentru această lună.")

    def afiseaza_consum(self, an, luna):
        cheie_curenta = (an, luna)
        cheie_precedenta = self.calculeaza_luna_precedenta(an, luna)

        if cheie_precedenta in self.citiri and cheie_curenta in self.citiri:
            consum_apa_rece = self.citiri[cheie_curenta]['apa_rece'] - self.citiri[cheie_precedenta]['apa_rece']
            consum_apa_calda = self.citiri[cheie_curenta]['apa_calda'] - self.citiri[cheie_precedenta]['apa_calda']

            print(f"{luna} {an}")
            print(f"Apa calda {self.citiri[cheie_precedenta]['apa_calda']}")
            print(f"Apă rece {self.citiri[cheie_precedenta]['apa_rece']}")
            print(f"{luna} {an} consum")
            print(f"{self.citiri[cheie_curenta]['apa_calda']} {consum_apa_calda}")
            print(f"{self.citiri[cheie_curenta]['apa_rece']} {consum_apa_rece}")
        else:
            print("Eroare: Nu există citiri pentru luna curentă și/luna precedentă.")

    def validare_citire(self, an, luna, apa_rece, apa_calda):
        if an < 0 or luna not in ['ian', 'feb', 'mar', 'apr', 'mai', 'iun', 'iul', 'aug', 'sep', 'oct', 'noi', 'dec']:
            return False

        if (an, luna) in self.citiri:
            return False

        if apa_rece < 0 or apa_calda < 0:
            return False

        cheie_precedenta = self.calculeaza_luna_precedenta(an, luna)
        if cheie_precedenta in self.citiri:
            if apa_rece < self.citiri[cheie_precedenta]['apa_rece'] or apa_calda < self.citiri[cheie_precedenta][
                'apa_calda']:
                return False

        return True

    def calculeaza_luna_precedenta(self, an, luna):
        luni = ['ian', 'feb', 'mar', 'apr', 'mai', 'iun', 'iul', 'aug', 'sep', 'oct', 'noi', 'dec']
        index_luna = luni.index(luna)

        if index_luna == 0:
            an_precedent = an - 1
            luna_precedenta = luni[-1]
        else:
            an_precedent = an
            luna_precedenta = luni[index_luna - 1]

        return (an_precedent, luna_precedenta)


# Exemplu de utilizare
admin_citiri_apa = AdministrareCitiriApa()

# Adăugare citire
admin_citiri_apa.adauga_citire(an=2018, luna='ian', apa_rece=10, apa_calda=10)
admin_citiri_apa.adauga_citire(an=2018, luna='feb', apa_rece=20, apa_calda=20)
admin_citiri_apa.adauga_citire(an=2018, luna='mar', apa_rece=30, apa_calda=30)
admin_citiri_apa.adauga_citire(an=2018, luna='apr', apa_rece=40, apa_calda=40)
admin_citiri_apa.adauga_citire(an=2018, luna='mai', apa_rece=50, apa_calda=50)
admin_citiri_apa.adauga_citire(an=2018, luna='iun', apa_rece=60, apa_calda=60)
admin_citiri_apa.adauga_citire(an=2018, luna='iul', apa_rece=70, apa_calda=70)

# Afișare consum pentru luna curentă
admin_citiri_apa.afiseaza_consum(an=2018, luna='ian')
admin_citiri_apa.afiseaza_consum(an=2018, luna='feb')
admin_citiri_apa.afiseaza_consum(an=2018, luna='mar')
admin_citiri_apa.afiseaza_consum(an=2018, luna='apr')

# Ștergere citire
#admin_citiri_apa.sterge_citire(an=2018, luna='ian')
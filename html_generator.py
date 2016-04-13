from datetime import *
from time import *
from math import *

class html_generator():
    def __init__(self):
        self.vorne = ""
        self.hinten = ""
        self.datum = strftime("%A, %x", localtime())
        self.lade_html()

    def lade_html(self):
        """speichert den Inhalt der Vorlagen in zwei Variablen"""
        with open('rumpfdatei_vorne.htm', 'r') as inf:
            self.vorne = inf.read()
        with open('rumpfdatei_hinten.htm', 'r') as inf:
            self.hinten = inf.read()

    def korrigiere_daten(self, html, nummer):
        korrigierter_code = html.replace("SUBSTITUIEREN_NUMMER", str(nummer+1))
        korrigierter_code = korrigierter_code.replace("SUBSTITUIEREN_DATUM", self.datum)
        return korrigierter_code

    def erzeuge_html(self, regelungen, zeilenzahl=10):
        # Es werden 'seitenzahl' viele Seiten werden
        seitenzahl = ceil(len(regelungen) / zeilenzahl)
        print(seitenzahl)
        counter = 1
        dateinummer = 1
        html_code = self.korrigiere_daten(self.vorne, dateinummer)

        for r in regelungen:
            rest = len(regelungen)-counter
            html_code += self.erzeuge_html_zeile(r, counter)

            # Erzeuge die Datei denn die vorgebene maximale zeilenzahl
            # wurde erreicht. Die and-Bedinung ist noetig weil sonst
            # bei %10 die erste Seite nur einen Eintrag hat
            if counter % zeilenzahl is 0 and counter > 0 or rest is 0:
                html_code += self.hinten
                self.schreibe_html(html_code, dateinummer)
                dateinummer += 1
                html_code = self.korrigiere_daten(self.vorne, dateinummer)

            counter += 1

        # print("Regel {} wurde geschrieben".format(counter))

    def schreibe_html(self, html_code, nummer):
        """Schreibt den gegebene HTML_Code in die Datei mit der
        angegeben Nummer"""
        print("Schreibe Datei Nummer "+str(nummer))
        dateiname = "test_"+str(nummer)+".htm"
        with open(dateiname, 'w') as outf:
            outf.write(html_code)

    def erzeuge_html_zeile(self, regel, counter):
        """Erzeugt eine HTML-Code Zeile entsprechend der Regel"""
        if(counter % 2 == 0):
            string = "<tr class=\'list odd\'><td class=\"list\" align=\"center\">"
        else:
            string = "<tr class=\'list even\'><td class=\"list\" align=\"center\">"
        string += "<b>{}</b></td><td class=\"list\" align=\"center\"><b>{}</b></td><td class=\"list\" align=\"center\"><b>{}</b></td><td class=\"list\" align=\"center\"><b>{}</b></td><td class=\"list\" align=\"center\"><b>{}</b></td><td class=\"list\" align=\"center\">{}</td></tr>".format(regel.k, regel.s, regel.l, regel.kurs, regel.r, regel.v)
        string += "\n"
        # regel.debug()
        # print(string)
        return string

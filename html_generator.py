# -*- coding: utf8 -*-
"""
License: GPL 3
Author: Carsten Niehaus
"""

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

    def korrigiere_daten(self, html, nummer, ueberschrift=""):
        """ An zwei Stellen in der Vorlage muss der HTML-Code
        nachgebessert werden:
        SUBSTITUIEREN_NUMMER muss die korrekte naechste Seitenzahl
          enthalten fuer den zeitgesteuerten Wechsel
        SUBSTITUIEREN_DATUM muss dass aktuelle Datum erhalten,
          zum Beispiel im Format Mittwoch, 13.04.2016
        """
        print("Korrigiere das HTML mit der Ueberschrift", ueberschrift)
        print("Korriere Datei Nummer", nummer)

        korrigierter_code = html.replace(
            "SUBSTITUIEREN_NUMMER", str(nummer + 1))
        korrigierter_code = korrigierter_code.replace(
            "SUBSTITUIEREN_DATUM", ueberschrift)
        return korrigierter_code

    def erzeuge_html(self, regelungen, zeilenzahl=10):
        """Diese Methode geht alle Regelungen durch
        alle 'seitenzahl' Regelungen wird eine neue Datei geschrieben."""
        # Es werden 'seitenzahl' viele Seiten werden
        # seitenzahl = ceil(len(regelungen_heute) / zeilenzahl) + \
        #    ceil(len(regelungen_folgetag) / zeilenzahl)
        seitenzahl = 8
        counter = 1
        dateinummer = 1
        # lt = localtime()

        r_heute = []
        r_folgetag = []

        for r in regelungen:
            datum = r.datum

            if datum == regelungen[1].datum:
                r_heute.append(r)
            else:
                r_folgetag.append(r)

        print("..................................................")
        print("Anzahl Regeln heute/Folgetag {} und {}".format(len(r_heute),
            len(r_folgetag)))
        print("..................................................")

        self.erzeuge_zeilen(r_heute, zeilenzahl)
        self.erzeuge_zeilen(r_folgetag, zeilenzahl)


    def erzeuge_zeilen(self, regelungen, zeilenzahl=10):
        counter = 1
        seitenzahl = 8
        dateinummer = 1
        html_code = self.korrigiere_daten(self.vorne, dateinummer, "")

        for r in regelungen:
            # Anzahl verbleibender Elemente
            rest = len(regelungen) - counter
            html_code += self.erzeuge_html_zeile(r, counter)

            # Erzeuge die Datei denn die vorgebene maximale zeilenzahl
            # wurde erreicht. Die and-Bedingung ist noetig, weil sonst
            # bei %10 die erste Seite nur einen Eintrag hat
            # Die or-Bediungung ist notwendig fuer die letzte Seite
            # falls diese nicht ganz voll ist
            if counter % zeilenzahl is 0 and counter > 0 or rest is 0:
                html_code += self.hinten
                self.schreibe_html(html_code, dateinummer, seitenzahl)
                dateinummer += 1
                html_code = self.korrigiere_daten(
                    self.vorne, dateinummer, "fff")

            counter += 1

    def schreibe_html(self, html_code, nummer, seitenanzahl):
        """Schreibt den gegebene HTML_Code in die Datei mit der
        angegeben Nummer"""
        print("Schreibe Datei Nummer {}".format(nummer))

        code = html_code

        # Trick 17 bei der letzten Datei...
        # Bei der letzten Seite muss auf die erste Seite verwiesen werden
        if nummer == seitenanzahl:
            s = "URL=test_{}.htm".format(nummer + 1)
            code = html_code.replace(s, "URL=test_1.htm")

        dateiname = "test_" + str(nummer) + ".htm"
        with open(dateiname, 'w') as outf:
            outf.write(code)

    def erzeuge_html_zeile(self, regel, counter):
        """Erzeugt eine HTML-Code Zeile entsprechend der Regel"""
        farbe_entfall = "FF0000"
        farbe_normal = "010101"
        farbe_raum = "199A35"
        farbe = ""

        if(counter % 2 == 0):  # jede zweite Zeile andersfarbig
            string = "<tr class=\'list even\'><td class=\"list\" align=\"center\">"
        else:
            string = "<tr class=\'list odd\'><td class=\"list\" align=\"center\">"

        regelzeile = "<b><span style=\"color: #FARBE\">{}</span></b></td><td class=\"list\" align=\"center\"><b><span style=\"color: #FARBE\">{}</span></b></td><td class=\"list\" align=\"center\"><b><span style=\"color: #FARBE\">{}</span></b></td><td class=\"list\" align=\"center\"><b><span style=\"color: #FARBE\">{}</span></b></td><td class=\"list\" align=\"center\"><b><span style=\"color: #FARBE\">{}</span></b></td><td class=\"list\" align=\"center\"><span style=\"color: #FARBE\">{}</span></td><td class=\"list\" align=\"center\"><span style=\"color: #FARBE\">{}</span></td></tr>".format(
            regel.k, regel.s, regel.f, regel.l, regel.r, regel.s_f, regel.s_l)

        if regel.l == "---":
            farbe = farbe_entfall
        elif regel.s_l == "":
            farbe = farbe_raum
        else:
            farbe = farbe_normal

        farbige_zeile = regelzeile.replace("FARBE", farbe)
        string += farbige_zeile
        #string += "<b>{}</b></td><td class=\"list\" align=\"center\"><b>{}</b></td><td class=\"list\" align=\"center\"><b>{}</b></td><td class=\"list\" align=\"center\"><b>{}</b></td><td class=\"list\" align=\"center\"><b>{}</b></td><td class=\"list\" align=\"center\">{}</td></tr>".format(regel.k, regel.s, regel.f, regel.l, regel.r, regel.s_f)
        string += "\n"

        return string

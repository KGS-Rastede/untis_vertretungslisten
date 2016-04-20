# -*- coding: utf8 -*-
"""
License: GPL 3
Author: Carsten Niehaus
"""

from datetime import *
from time import *
from math import *

from enum import Enum


class Typ(Enum):
    feldbreite = 1
    sek1 = 2
    sek2 = 3


class html_generator():

    def __init__(self, verzeichnis, t):
        self.vorne = ""
        self.hinten = ""
        self.datum = strftime("%A, %x", localtime())
        self.lade_html()

        self.verzeichnis = verzeichnis
        self.typ = t

    def lade_html(self):
        """speichert den Inhalt der Vorlagen in zwei Variablen"""
        with open('rumpfdatei_vorne.htm', 'r') as inf:
            self.vorne = inf.read()
        with open('rumpfdatei_hinten.htm', 'r') as inf:
            self.hinten = inf.read()

    def korrigiere_daten(self, html, nummer, stand, ueberschrift=""):
        """ An zwei Stellen in der Vorlage muss der HTML-Code
        nachgebessert werden:
        SUBSTITUIEREN_NUMMER muss die korrekte naechste Seitenzahl
          enthalten fuer den zeitgesteuerten Wechsel
        SUBSTITUIEREN_DATUM muss dass aktuelle Datum erhalten,
          zum Beispiel im Format Mittwoch, 13.04.2016
        """
        print("Korrigiere das HTML mit der Ueberschrift", ueberschrift)
        # print("Korriere Datei Nummer", nummer)

        korrigierter_code = html.replace(
            "SUBSTITUIEREN_NUMMER", str(nummer + 1))
        korrigierter_code = korrigierter_code.replace(
            "SUBSTITUIEREN_DATUM", ueberschrift)
        korrigierter_code = korrigierter_code.replace(
            "SUBSTITUIEREN_STAND", stand)
        return korrigierter_code

    def erzeuge_html(self, regelungen, zeilenzahl=10):
        """Diese Methode geht alle Regelungen durch
        alle 'seitenzahl' Regelungen wird eine neue Datei geschrieben."""
        counter = 1
        dateinummer = 1
        # lt = localtime()

        # print("erzeuge_html Anzahl an Regeln:",len(regelungen))

        r_heute = []
        r_folgetag = []

        for r in regelungen:
            datum = r.datum

            if datum == regelungen[0].datum:
                r_heute.append(r)
            else:
                r_folgetag.append(r)

        # Es werden 'seitenzahl' viele Seiten werden
        seitenzahl_heute = ceil(len(r_heute) / zeilenzahl)
        seitenzahl_folgetag = ceil(len(r_folgetag) / zeilenzahl)
        gesamtseiten = seitenzahl_heute + seitenzahl_folgetag

        print("")
        print("")
        print("")
        print("............erzeuge_html..........................")
        print("Anzahl Regeln HEUTE: {} FOLGETAG: {} GESAMT: {}".format(len(r_heute),
                                                              len(r_folgetag),
                                                              len(r_heute)+len(r_folgetag)))
        print("..................................................")

        if len(r_heute) > 0:
            self.erzeuge_zeilen(r_heute, 1, gesamtseiten, zeilenzahl)
        if len(r_folgetag) > 0:
            self.erzeuge_zeilen(r_folgetag, seitenzahl_heute+1, gesamtseiten, zeilenzahl)

    def erzeuge_zeilen(self, regelungen, startseite, gesamtseitenzahl, zeilenzahl=10):
        """gehe alle 'regelungen' durch und erzeuge pro Regelung eine Zeile. alle 'zeilenzahl'
        Regeln wird eine neue HTML-Seite erzeugt."""
        print("erzeuge_zeilen Anzahl an Regeln:",len(regelungen))
        counter = 1

        dateinummer = startseite

        html_code = self.korrigiere_daten(self.vorne, dateinummer, regelungen[0].stand, self.erstelle_ueberschrift(regelungen[0].datum, dateinummer, gesamtseitenzahl))

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
                self.schreibe_html(html_code, dateinummer, gesamtseitenzahl)
                dateinummer += 1
                html_code = self.korrigiere_daten(
                    self.vorne, dateinummer, r.stand, self.erstelle_ueberschrift(r.datum, dateinummer, gesamtseitenzahl))

            counter += 1

    def erstelle_ueberschrift(self, datum, seite, gesamtseiten):
        """Die Uberschrift soll aus Datum, Wochentag und (x von y) bestehen"""
        s = " ({} von {})".format(seite, gesamtseiten)
        d = datum.split(" ")
        korrigierte_ueberschrift = "{} ({})\t({}/{})".format(
            d[1], d[0], seite, gesamtseiten)
        return korrigierte_ueberschrift

    def schreibe_html(self, html_code, nummer, gesamtseiten):
        """Schreibt den gegebene HTML_Code in die Datei mit der
        angegeben Nummer"""
        # print("Schreibe Datei Nummer {} in Verzeichnis {}".format(nummer, self.verzeichnis))

        code = html_code
        pfad = "./vertretungsplan/" + self.verzeichnis

        # Trick 17 bei der letzten Datei...
        # Bei der letzten Seite muss auf die erste Seite verwiesen werden
        if nummer == gesamtseiten:
            s = "URL=test_{}.htm".format(nummer + 1)
            code = html_code.replace(s, "URL=test_1.htm")

        dateiname = "test_" + str(nummer) + ".htm"
        with open(pfad + "/" + dateiname, 'w') as outf:
            outf.write(code)

    def erzeuge_html_zeile(self, regel, counter):
        """Erzeugt eine HTML-Code Zeile entsprechend der Regel"""
        #farbe_entfall = "c0392b"
        #farbe_normal = "010101"
        #farbe_raum = "27ae60"
        farbe_class = ""

        if(counter % 2 == 0):  # jede zweite Zeile andersfarbig
            string = "<tr class=\'list even\'><td class=\"list\">"
        else:
            string = "<tr class=\'list odd\'><td class=\"list\">"

        if regel.l == "---":
            farbe_class = "entfall"
        elif regel.s_l == "":
            farbe_class = "raum"
        else:
            farbe_class = "normal"

        regelzeile = self.regelzeile_generieren(regel, "schueler")

        farbige_zeile = regelzeile.replace("CLASS", farbe_class)
        string += farbige_zeile

        string += "\n"

        return string

    def regelzeile_generieren(self, regel, form):
        """generiert die einzelnen zeilenzahl. Je nach Vertreutungsplan-Form
        kommen verschiedene Vorlagen zum Einsatz
        """
        if form == "schueler":
            regelzeile  = "<b><span class=\"CLASS\">{}</span></b></td><td class=\"list\">".format(regel.k)
            regelzeile += "<b><span class=\"CLASS\">{}</span></b></td><td class=\"list\">".format(regel.s)
            regelzeile += "<b><span class=\"CLASS\">{}</span></b></td><td class=\"list\">".format(regel.f)
            regelzeile += "<b><span class=\"CLASS\">{}</span></b></td><td class=\"list\">".format(regel.l)
            regelzeile += "<b><span class=\"CLASS\">{}</span></b></td><td class=\"list\">".format(regel.r)
            regelzeile += "<span class=\"CLASS\">{}</span></td><td class=\"list\">".format(regel.s_f)
            regelzeile += "<span class=\"CLASS\">{}</span></td></tr>".format(regel.s_l)

        return regelzeile

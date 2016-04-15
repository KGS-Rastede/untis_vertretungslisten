# -*- coding: utf8 -*-
"""
License: GPL 3
Author: Carsten Niehaus
"""

from bs4 import BeautifulSoup
from time import *
from datetime import *
import os

from regelungen import *
from html_generator import *

# Deutsche Sprache einstellen, das ist fuer
# die Datumsdarstellung wichtig (Mittwoch statt Wednesday)
import locale
locale.setlocale(locale.LC_ALL, '')

regelungen_5_6 = []
regelungen_7_10 = []
regelungen_11_12 = []

zeilenzahl = 8


def aktuelle_stunde():
    # heutiges Datum
    heute = datetime.today()

    # Heute morgen, 08:00:00 Uhr (Beginn erste Stunde
    n0 = datetime(heute.year, heute.month, heute.day, 8, 0)
    # Aktuelle Zeit
    n1 = datetime.now()

    # Berechne die vergangen Zeit seit Beginn der ersten Stunde
    dauer = n1 - n0
    # Konvertiere in Sekunden
    d = dauer.seconds

    print("Schule laeuft seit: " + str(d) + " Sekunden")

    aktuelle_unterrichtsstunde = 0

    # Variable die das Konvertieren in Minuten etwas einfacher macht
    m = 60
    if(d < 45 * m):
        aktuelle_unterrichtsstunde = 1
        print("erste Stunde")
    elif(d < 55 * m):
        aktuelle_unterrichtsstunde = 2
        print("zweite Stunde")
    elif(d < 120 * m):
        aktuelle_unterrichtsstunde = 3
        print("dritte Stunde")
    elif(d < 165 * m):
        aktuelle_unterrichtsstunde = 4
        print("vierte Stunde")
    elif(d < 230 * m):
        aktuelle_unterrichtsstunde = 5
        print("fuenfte Stunde")
    elif(d < 285 * m):
        aktuelle_unterrichtsstunde = 6
        print("sechste Stunde")
    elif(d < 390 * m):
        aktuelle_unterrichtsstunde = 7
        print("siebte Stunde")
    elif(d < 435 * m):
        aktuelle_unterrichtsstunde = 8
        print("achte Stunde")

    # zum Testen
    aktuelle_unterrichtsstunde = 1

    return aktuelle_unterrichtsstunde


def dateneinlesen(verzeichnis="07-10"):
    """
    """
    pfad = "./vertretungsplan/" + verzeichnis

    # TODO Es muss hier 5-6 und 11-12 noch austauschbar sein
    for f in ["subst_001.htm", "subst_002.htm"]:
        with open(pfad + "/" + f, 'r') as inf:
            #  print("Oeffne Datei {}".format(inf))
            soup = BeautifulSoup(inf, 'html.parser')

            # Datum fuer die Ueberschrift herausfinden
            title = soup.find('div', attrs={'class': 'mon_title'}).string

            # Gesucht wird der letzte Stand der Synchronisierung
            # In der Ursprungsdatei sieht das so aus:
            # <h2>Stand: <!--12.04.2016 -->22:19 Uhr</h2>

            table = soup.find('table', attrs={'class': 'mon_list'})
            for row in table.findAll("tr"):
                cells = row.findAll("td")
                if len(cells) == 7:
                    klasse = cells[0].find(text=True)
                    stunde = cells[1].find(text=True)
                    kurs = cells[2].find(text=True)
                    lehrer = cells[3].find(text=True)
                    raum = cells[4].find(text=True)
                    s_f = cells[5].find(text=True)
                    s_l = cells[6].find(text=True)

                    neue_regelung = regelung(
                        klasse, stunde, kurs, lehrer, raum, s_f, s_l, title)

                    regelungen_7_10.append(neue_regelung)


def vergangene_regelungen_entfernen(regeln):
    """loescht in der Vergangenheit liegende Regelungen"""
    stunde = aktuelle_stunde()

    restliche_regelungen = []

    for reg in regeln:
        if not reg.in_vergangenheit(stunde):
            restliche_regelungen.append(reg)

    return restliche_regelungen


def zeige_entfernte_regelungen(r1, r2):
    """Schaut nach, welche Regelungen in r1 NICHT in r2 sind
    r1 muss also die groessere Liste sein

    Nur wichtig zum Debugen
    """
    for reg in r1:
        if reg not in r2:
            print("Regelung (Klasse {} in der Stunde {}) entfernt".format(reg.k, reg.s))
        else:
            # print("Regelung (Klasse {} in der Stunde {}) bleibt".format(reg.k, reg.s))
            pass


dateneinlesen()

generator = html_generator()
generator.erzeuge_html(vergangene_regelungen_entfernen(regelungen_7_10),
    zeilenzahl)

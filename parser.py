# -*- coding: utf8 -*-
"""
License: GPL 3
Author: Carsten Niehaus
"""

from bs4 import BeautifulSoup
from time import *
from datetime import *
import shutil
import os

from regelungen import *
from html_generator import *
from nachrichten_des_tages import *

# Deutsche Sprache einstellen, das ist fuer
# die Datumsdarstellung wichtig (Mittwoch statt Wednesday)
import locale
locale.setlocale(locale.LC_ALL, '')

regelungen_5_6 = []
regelungen_7_10 = []
regelungen_11_13 = []
lehrer = []

zeilenzahl_schueler = 10
zeilenzahl_lehrer = 22

ndt = NachrichtenDesTages()


def aktuelle_stunde():
    """Berechnet die aktulle Schulstunde nach folgende Vorgabe:
        Std    Beginn  Ende    Minuten
        1		 8:00	 8:45	 45
        2		 8:55	 9:40	100
        3		10:00	10:45	165
        4		10:30	11:15	195
        5		11:50	12:35	275
        6		12:45	13:30	330
        7		14:30	15:15	435
        8		15:15	16:00	480
    """
    # heutiges Datum
    heute = datetime.today()

    # Heute morgen, 08:00:00 Uhr (Beginn der ersten Stunde)
    n0 = datetime(heute.year, heute.month, heute.day, 8, 0)

    # Aktuelle Zeit
    n1 = datetime.now()

    # Zum testen kann man die folgende Zeile auskommentieren.
    # So kann man so tun, all wenn es jetzt gerade eine andere Zeit
    # wäre
    n1 = datetime(heute.year, heute.month, heute.day, 7, 45)

    # Berechne die vergangen Zeit seit Beginn der ersten Stunde
    dauer = n1 - n0

    # Konvertiere in Sekunden
    d = dauer.seconds

    if n1 < n0:
        d = 0

    print("Schule laeuft seit: " + str(d) + " Sekunden")

    aktuelle_unterrichtsstunde = 0

    # Variable die das Konvertieren in Minuten etwas einfacher macht
    m = 60
    if(d < 45 * m):
        aktuelle_unterrichtsstunde = 1
        print("erste Stunde")
    elif(d < 100 * m):
        aktuelle_unterrichtsstunde = 2
        print("zweite Stunde")
    elif(d < 165 * m):
        aktuelle_unterrichtsstunde = 3
        print("dritte Stunde")
    elif(d < 195 * m):
        aktuelle_unterrichtsstunde = 4
        print("vierte Stunde")
    elif(d < 275 * m):
        aktuelle_unterrichtsstunde = 5
        print("fuenfte Stunde")
    elif(d < 330 * m):
        aktuelle_unterrichtsstunde = 6
        print("sechste Stunde")
    elif(d < 435 * m):
        aktuelle_unterrichtsstunde = 7
        print("siebte Stunde")
    elif(d < 480 * m):
        aktuelle_unterrichtsstunde = 8
        print("achte Stunde")
    else:
        # Das bedeutet Schulschluss
        aktuelle_unterrichtsstunde = 9

    # zum Testen
    # aktuelle_unterrichtsstunde = 1

    # print(aktuelle_unterrichtsstunde)

    return aktuelle_unterrichtsstunde

def lehrerregelungen_nzt():
    """list die Nachrichten zum Tag (nzt) eine"""
    pfad = "./vertretungsplan/lehrerzimmer"

    for f in ["subst_001.htm", "subst_002.htm"]:
        with open(pfad + "/" + f, 'r') as inf:
            soup = BeautifulSoup(inf, 'html.parser')

            a = []

            table = soup.find('table', attrs={'class': 'info'})
            for row in table.findAll("tr"):
                for c in row.findAll("td"):
                    a.append(c.string)

            if f == "subst_001.htm":
                ndt.fuegeNDThinzu(a, "heute")
            else:
                ndt.fuegeNDThinzu(a, "folgetag")




def dateneinlesen(verzeichnis, regelungen):
    """Die 'regelungen' im 'verzeichnis' werden eingelesen
    Eine Besonderheit bei Python ist, dass die 'regelungen'
    keine Kopie sondern eine Referenz sind. Daher muss ich
    sie NICHT zurueck geben (das gilt fuer alle Listen und
    ist anders als z.B. bei c++)
    """
    pfad = "./vertretungsplan/" + verzeichnis
    shutil.copy2("vorlage_keine_regelungen.htm", pfad+"/test_1.htm")

    for f in ["subst_001.htm", "subst_002.htm"]:
        with open(pfad + "/" + f, 'r') as inf:
            print("Oeffne Datei {}".format(inf))
            soup = BeautifulSoup(inf, 'html.parser')

            # Datum fuer die Ueberschrift herausfinden
            title = soup.find('div', attrs={'class': 'mon_title'}).string

            # Gesucht wird der letzte Stand der Synchronisierung
            # In der Ursprungsdatei sieht das so aus:
            # <div style="text-align: right">
            # <h2>Stand: <!--12.04.2016 -->22:19 Uhr</h2>
            # </div>
            # Bei Lehrern hingegen so:
            # <body>
            # <table class="mon_head">
            # <tr>
	        # <td align="right"><h2>Stand: 15.05.2016 16:49</h2></td>

            stand = soup.find( 'div', attrs={'style': 'text-align: right'}).h2.text

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

                    neue_regelung = regelung_schueler(
                        klasse, stunde, kurs, lehrer, raum, s_f, s_l, title, stand)
                    #print("##########################")
                    #print(neue_regelung.debug())
                    #print("##########################\n")
                    regelungen.append(neue_regelung)

def nicht_relevante_regelungen_entfernen(regeln, debug="False"):
    print("ooooooooonicht_relevante_regelungen_entfernenooooooooooooooooo")
    nach_zeit_gefiltert = vergangene_regelungen_entfernen(regeln, debug)
    nach_klassenarbeiten_gefiltert = entferne_klassenarbeiten(nach_zeit_gefiltert, debug)
    print("ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo")
    return nach_klassenarbeiten_gefiltert

def entferne_klassenarbeiten(regeln, debug="False"):
    print("xxxxxxxxxxxxxxxxxxxxxxentferne_klassenarbeitenxxxxxxxxxxxxxxxxxxxxxxxx")
    restliche_regelungen = []   
    temp_liste = []
        
    for reg in regeln:
        if(reg.f is "ENTF"):
            temp_liste.append(reg)
    
    print("Es gibt {} ENTF-Regelungen".format(len(temp_liste)))
    print("Es gibt {} Regelungen".format(len(regeln)))

    for entf_regelung in temp_liste:        
        for r in regeln:
            # Wenn diese 3-fach-Bedingung erfuellt ist gibt es
            # zur gleichen Zeit in der gleichen Klasse einen Alternativunterricht
            # und das kann nur eine Klassenarbeit sein!
            if(r.k == entf_regelung.k           # gleiche Klasse?
                and r.s == entf_regelung.s      # gleiche Stunde?
                and r.l == entf_regelung.s_l):    # gleicher Lehrer?
                
                #print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                #print(entf_regelung.l)
                #print(entf_regelung.s_l)
                #print(r.l)
                #print(r.s_l)

                print("\n\n\n||||||||||||||||gefundenes Paar|||||||||||||||||||||||||||||")
                print(r.debug())
                print(entf_regelung.debug())
                print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n")
        
                r.art = "entfernen"             # Regelung als zur entfernen markieren
                entf_regelung.art= "entfernen"
            
#    for entf_regelung in temp_liste:
#        if entf_regelung.art == "entfernen":
#            print("pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp")
#            print(entf_regelung.debug())
#            print("pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp")
            
            #print("r:            (Stunde:{})  f ist {} und s_f ist {}.".format(r.s, r.f, r.s_f))
            #print("entf_regelung (Stunde:{})  f ist {} und s_f ist {}.".format(entf_regelung.s, entf_regelung.f, entf_regelung.s_f))
            #if(r.f == entf_regelung.s_f):
            #    print("BINGO                           ------123123123123")
            #    print(r.debug())


    print("\n\n\nAM ENDE FLIEGEN RAUS:")
    for reg in regeln:
        if reg.art == "entfernen":
            print(reg.debug())
        else:
            restliche_regelungen.append(reg)
    
    print("Es gibt am Ende {} Regelungen".format(len(restliche_regelungen)))   
        
    return restliche_regelungen
    
def vergangene_regelungen_entfernen(regeln, debug="False"):
    """loescht in der Vergangenheit liegende Regelungen
    Gibt debug-Output wenn 'debug' auf 'True' gesetzt ist
    """
    stunde = aktuelle_stunde()

    restliche_regelungen = []

    for reg in regeln:
        datum = reg.datum
        # print("Datum der Regel: {}, Datum regel[0]: {}".format(datum, regeln[0].datum))

        if datum != regeln[0].datum:
            restliche_regelungen.append(reg)
        elif not reg.in_vergangenheit(stunde):
            restliche_regelungen.append(reg)
        else:
            if debug is True:
                print("Gefiltert", reg.debug(debug=True))

    if debug is True:
        print("")
        print("")
        print("")
        print("- - - - - - - -F I L T E R U N G- - - - - - - - - -")
        print("Anzahl Regeln VORHER: {} NACHHER: {}".format(len(regeln),
                                                            len(restliche_regelungen)))
        print("- - - - - - - - - - - - - - - - - - - - - - - - - -")

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

#generator_feldbreite = html_generator( "05-06", Typ.feldbreite)
#dateneinlesen("05-06", regelungen_5_6)
#generator_feldbreite.erzeuge_html(
#    nicht_relevante_regelungen_entfernen(regelungen_5_6), zeilenzahl_schueler)

generator_sek1 = html_generator( "07-10", Typ.sek1)
dateneinlesen("07-10", regelungen_7_10)
generator_sek1.erzeuge_html(
    nicht_relevante_regelungen_entfernen(regelungen_7_10), zeilenzahl_schueler)

#generator_sek2 = html_generator( "11-13", Typ.sek2)
#dateneinlesen("11-13", regelungen_11_13)
#generator_sek2.erzeuge_html(
#    nicht_relevante_regelungen_entfernen(regelungen_11_13), zeilenzahl_schueler)

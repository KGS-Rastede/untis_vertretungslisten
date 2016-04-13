from bs4 import BeautifulSoup
from time import *
from datetime import *

from regelungen import *

regelungen = []


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


    #zum Testen
    aktuelle_unterrichtsstunde = 2

    return aktuelle_unterrichtsstunde


def lies_tabelle(soup):
    """Gute Anleitung
    http://chrisalbon.com/python/beautiful_soup_scrape_table.html"""
    table = soup_heute.find('table', attrs={'class': 'mon_list'})
    for row in table.findAll("tr"):
        cells = row.findAll("td")
        if len(cells) == 6:
            klasse = cells[0].find(text=True)
            stunde = cells[1].find(text=True)
            kurs = cells[2].find(text=True)
            lehrer = cells[3].find(text=True)
            raum = cells[4].find(text=True)
            vertreter = cells[5].find(text=True)

            r = regelung(klasse, stunde, kurs, lehrer, raum, vertreter)
            regelungen.append(r)


def erste_soups():
    html_doc_heute = open("subst_001.htm", 'r').read()
    html_doc_morgen = open("subst_002.htm", 'r').read()

    s1 = BeautifulSoup(html_doc_heute, 'html.parser')
    s2 = BeautifulSoup(html_doc_morgen, 'html.parser')
    return s1, s2

def regelungen_filtern():
    stunde = aktuelle_stunde()

    restliche_regelungen = []

    for reg in regelungen:
        if not reg.in_vergangenheit(stunde):
            restliche_regelungen.append(reg)

    return restliche_regelungen

def gefilterte_regelungen( r ):
    for reg in regelungen:
        if reg not in r:
            print("Regelung (Klasse {} in der Stunde {}) entfernt".format(reg.k, reg.s))
        else:
            #print("Regelung (Klasse {} in der Stunde {}) bleibt".format(reg.k, reg.s))
            pass


soup_heute, soup_morgen = erste_soups()


lies_tabelle(soup_heute)
stunde = aktuelle_stunde()
gefilterte_regeln = regelungen_filtern()
gefilterte_regelungen(gefilterte_regeln)



#for r in regelungen:
#    if r.in_vergangenheit(stunde):
#        print("Die Stunde {} ist schon vergangen".format(stunde))
#        print("Aktuelle Stunde: {}".format(stunde))
    #if stunde in r.zeitfenster():
    #    print("{} ist in {}".format(stunde,r.zeitfenster()))

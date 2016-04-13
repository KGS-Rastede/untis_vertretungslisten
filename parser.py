from bs4 import BeautifulSoup
from time import *
from datetime import *

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
        print("erste Stunde")
    elif(d < 55 * m):
        print("erste Pause")
    elif(d < 100 * m):
        print("zweite Stunde")
    elif(d < 120 * m):
        print("zweite Pause")
    elif(d < 165 * m):
        print("dritte Stunde")
    elif(d < 210 * m):
        print("vierte Stunde")
    elif(d < 230 * m):
        print("dritte Pause")
    elif(d < 230 * m):
        print("fuenfte Stunde")
    elif(d < 240 * m):
        print("Pause 5/6")
    elif(d < 285 * m):
        print("sechste Stunde")
    elif(d < 345 * m):
        print("Mittagspause")

    return aktuelle_unterrichtsstunde


def erste_soups():
    html_doc_heute = open("subst_001.htm", 'r').read()
    html_doc_morgen = open("subst_002.htm", 'r').read()

    s1 = BeautifulSoup(html_doc_heute, 'html.parser')
    s2 = BeautifulSoup(html_doc_morgen, 'html.parser')
    return s1, s2

soup_heute, soup_morgen = erste_soups()


aktuelle_stunde()
print(soup_heute.head.contents[1])
print(soup_morgen.head.contents[1])

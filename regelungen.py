# -*- coding: utf8 -*-
"""
License: GPL 3
Author: Carsten Niehaus
"""
from datetime import *
from time import *

import nachrichten_des_tages

class regelung():
    """Basisklasse für Regelungen"""

    def __init__(self, klasse, stunde, fach, lehrer, raum, statt_fach, statt_lehrer, datum, stand, art = "vertretung"):
        self.k = klasse
        self.s = stunde
        self.f = fach
        self.l = lehrer
        self.r = raum
        self.s_f = statt_fach
        self.s_l = statt_lehrer
        self.stand = stand
        self.datum = datum
        self.art = art

        self.zf = self.zeitfenster()

    def debug(self):
        """Einfache Debugausgabe um Fehler zu finden
        """
        debugtext = "({}): Klasse {} in {}. Stunde. -- Typ: {} mit dem Fach {}.".format(
            self.datum, self.k, self.s, self.art, self.f)

        return debugtext

    def zeitfenster(self):
        """mögliches Format ist '2' oder '3-6'
        Sinn der Methode ist es, im Fall von '3-6'
        auch die 4. und 5. Stunde zu identifizieren"""
        stunden = []

        # print("in Zeitfenster()", self.s)

        # Test, ob es eine Stunde betrifft oder mehr als eine
        if "-" not in self.s and "/" not in self.s:
                # print("im doppelten if mit", self.s)
                stunden.append(int(self.s))  # nur eine Stunde
        else:  # mehr als eine Stunde
            startstunde = self.s[:1]  # nur das erste Zeichen
            endstunde = self.s[-1]  # nur das letzte Zeichen
            # print("Im else. Startstunde: {}, Endstunde: {}".format(startstunde, endstunde))

            if endstunde == "/":
                endstunde = startstunde

            # Jede betroffene Stunde an die Liste anhaengen
            for i in range(int(startstunde), int(endstunde) + 1):
                stunden.append(i)

        return stunden

    def in_zukunft(self, stunde):
        """gibt zurueck, ob die Regelung noch in
        der Zukunft liegen"""
        erste_betroffene_stunde = self.zf[:1]
        # print("-.-.-.-.-.-.-.-.-.-.-")
        # print("Zeitfenster: {}".format(self.zf))
        # print("Erste Stunde im Zeitfenster: {}".format(self.zf[:1]))
        return erste_betroffene_stunde < stunde

    def in_vergangenheit(self, stunde):
        """gibt zurueck, ob die Regelung in der getesteten Stunde
        schon vergangen ist"""
        # print("-.-.-.-.-.-.-.-.-.-.-")
        # print("Zeitfenster: {}".format(self.zf))
        letzte_betroffene_stunde = self.zf[-1]
        # print("Letzte Stunde im Zeitfenster: {}".format(letzte_betroffene_stunde))

        return letzte_betroffene_stunde < stunde

    def in_gegenwart(self, stunde):
        """gibt zurueck, ob die getestete Stunde von der
        Regelung betroffen ist"""
        erste_betroffene_stunde = self.zf[:1]
        letzte_betroffene_stunde = self.zf[-1]

        if erste_betroffene_stunde <= stunde <= letzte_betroffene_stunde:
            return True
        else:
            return False


class regelung_schueler(regelung):
    """Ein Objekt dieser Klasse entspricht einer Vertretungsregelung"""

    def __init__(self, klasse, stunde, fach, lehrer, raum, statt_fach, statt_lehrer, datum, stand, art = "vertretung"):
        regelung.__init__(self, klasse, stunde, fach, lehrer,
                          raum, statt_fach, statt_lehrer, datum, stand, art)
        self.aufbereitung()
        #print(self.debug(True))

    def aufbereitung(self):
        #  Entfall
        if self.f == "---":
            self.f = "ENTF"
            #print("Es liegt ENTFALL vor")

        #  Bei Raumtausch in den letzten beiden Zeilen
        #  nichts angezeigt werden
        if self.l == self.s_l:
            self.s_l = ""
            self.s_f = ""

        #  Bei Vertretung ohne Lehrer wird
        #  der Raum zum Forum
        if self.l == "+":
            self.l = "---"
            self.r = "FORUM"
            
        if self.art == "Klausur":
            print("Klausur liegt vor ---")
            print("({}): Klasse {} in {}. Stunde im Fach {} bei {} in Raum {} statt {} durch Kollegen {}".format(
                self.datum, self.k, self.s, self.f, self.l, self.r, self.s_f, self.s_l))
            print("Klausur liegt vor +++")
            self.s_f = "Klassenarbeit"

    def debug(self, debug=False):
        """Einfache Debugausgabe um Fehler zu finden
        Gibt debug-Output wenn 'debug' auf 'True' gesetzt ist
        """
        debugtext = ""

        if(debug is False):
            debugtext = "({}): Klasse {} in {}. Stunde im Fach {} bei {} in Raum {} statt {} durch Kollegen {}".format(
                self.datum, self.k, self.s, self.f, self.l, self.r, self.s_f, self.s_l)
        else:
            debugtext = "({}): Klasse {} in {}. Stunde. -- Typ: {}.".format(
                self.datum, self.k, self.s, self.art)

        return debugtext

# -*- coding: utf8 -*-
"""
License: GPL 3
Author: Carsten Niehaus
"""
from datetime import *
from time import *

class regelung():
    """Ein Objekt dieser Klasse entspricht einer Vertretungsregelung"""

    def __init__(self, klasse, stunde, fach, lehrer, raum, statt_fach, statt_lehrer, datum, stand):
        self.k = klasse
        self.s = stunde
        self.f = fach
        self.l = lehrer
        self.r = raum
        self.s_f = statt_fach
        self.s_l = statt_lehrer
        self.stand = stand

        self.datum = datum

        self.zf = self.zeitfenster()

        #  Entfall
        if self.f == "---":
            self.f = "ENTF"

        #  Bei Raumtausch in den letzten beiden Zeilen
        #  nichts angezeigt werden
        if self.l == self.s_l:
            self.s_l = ""
            self.s_f = ""

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
        letzte_betroffene_stunde = self.zf[-1]
        # print("-.-.-.-.-.-.-.-.-.-.-")
        # print("Zeitfenster: {}".format(self.zf))
        # print("Letzte Stunde im Zeitfenster: {}".format(letzte_betroffene_stunde))
        return letzte_betroffene_stunde < stunde

    def in_gegenwart(self, stunde):
        """gibt zurueck, ob die getestete Stunde von der
        Regelung betroffen ist"""
        pass

    def zeitfenster(self):
        """mögliches Format ist '2' oder '3-6'
        Sinn der Methode ist es, im Fall von '3-6'
        auch die 4. und 5. Stunde zu identifizieren"""
        stunden = []

        # Test, ob es eine Stunde betrifft oder mehr als eine
        if "-" not in self.s:
            stunden.append(int(self.s))  # nur eine Stunde
        else:  # mehr als eine Stunde
            startstunde = int(self.s[:1])  # nur das erste Zeichen
            endstunde = int(self.s[4:])  # ab dem 4. Zeichen

            # Jede betroffene Stunde an die Liste anhaengen
            for i in range(startstunde, endstunde + 1):
                stunden.append(i)

        return stunden

    def debug(self, kurz = False):
        """Einfache Debugausgabe um Fehler zu finden"""
        debugtext = ""

        if(kurz is False):
            debugtext = "({}): Klasse {} in {}. Stunde im Fach {} bei {} in Raum {} statt {} durch Kollegen {}".format(
            self.datum, self.k, self.s, self.f, self.l, self.r, self.s_f, self.s_l)
        else:
            debugtext= "({}): Klasse {} in {}. Stunde".format(self.datum, self.k, self.s)

        return debugtext

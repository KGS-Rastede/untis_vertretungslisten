# -*- coding: utf8 -*-
"""
License: GPL 3
Author: Carsten Niehaus
"""


class NachrichtenDesTages():
    """Fuer die Lehreransicht gibt es die Nachrichten das Tages. Dies sind 0
    bis 4 Zeilen mit jeweils zwei Spalten
    """
    def __init__(self):
        self.nachrichten_heute = []
        self.nachrichten_folgetag = []


    def ndt_aufbereiten(self, NachrichtenDesTages):
        """
        Macht aus dem Originalformat (zwei Zellen) ein einfacheres
        Layout. Das spart Platz. Statt |Betroffene Lehrer|x,y,z,...|
        wird einfach |Betroffene Lehrer: x,y,z| in einer Zelle dargestellt.
        """
        i = 0
        nachrichten = []

        for n in NachrichtenDesTages:
            nachricht = "<b>" + NachrichtenDesTages[i][0] + ": </b>"
            nachricht += NachrichtenDesTages[i][1]

            nachrichten.append(nachricht)
            i = i+1

        return nachrichten

    def fuegeNDThinzu(self, zeilen, tag):
        i = 0

        # print("ZEILEN:",zeilen)
        # print("TAG", tag)
        while i < len(zeilen):
            zeile = []
            zeile.append(zeilen[i])
            zeile.append(zeilen[i+1])

            if tag == "heute":
                self.nachrichten_heute.append(zeile)
            else:
                self.nachrichten_folgetag.append(zeile)

            # print("Generierte Zeile: **********************")
            # print(zeile)
            # print("*****************************************")
            # print()

            i += 2

    def generiere_zeilen(self, tag):
        """
        Diese Methode erzeugt die Zeilen für den 'Kopf'. Hier werden die
        betroffenen Lehrer, Räume, Klassen und abwesenden Lehrer dargstellt.
        """
        html_code = "<tr class=\"info\"><th class=\"info\" align=\"center\" colspan=\"4\">Nachrichten zum Tag</th></tr>"

        ndt = []

        if tag == "heute":
            ndt = self.nachrichten_heute
        else:
            ndt = self.nachrichten_folgetag


        nachrichten = self.ndt_aufbereiten(ndt)

        anzahl_regelungen = 4

        html_code += "<tr class=\"info\">"

        html_code += "<td class=\"info\" align=\"left\">"
        html_code += nachrichten[0]
        html_code += "</td>"

        html_code += "<td class=\"info\" align=\"left\">"
        html_code += nachrichten[1]
        html_code += "</td>"


        html_code += "</tr>"
        html_code += "<tr class=\"info\">"


        html_code += "<td class=\"info\" align=\"left\">"
        html_code += nachrichten[3]
        html_code += "</td>"


        html_code += "<td class=\"info\" align=\"left\">"
        html_code += nachrichten[2]
        html_code += "</td>"

        html_code += "</tr>"


        return html_code

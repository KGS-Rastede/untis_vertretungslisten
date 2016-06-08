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

        """
        html_code = "<tr class=\"info\"><th class=\"info\" align=\"center\" colspan=\"4\">Nachrichten zum Tag</th></tr>"

        ndt = []

        if tag == "heute":
            ndt = self.nachrichten_heute
        else:
            ndt = self.nachrichten_folgetag

        i = 0

        anzahl_regelungen = len(ndt)

        for zeile in ndt:
            html_code += "<tr class=\"info\"><td class=\"info\" align=\"left\">"
            html_code += ndt[i][0]
            html_code += "</td>"
            html_code += "<td class=\"info\" align=\"left\">"
            html_code += ndt[i][1]
            html_code += "</td>"

            if i < anzahl_regelungen:
                html_code += "<td class=\"info\" align=\"left\">"
                html_code += ndt[i][0]
                html_code += "</td>"

                html_code += "<td class=\"info\" align=\"left\">"
                html_code += ndt[i][1]
                html_code += "</td>"



            html_code += "</tr>"

            i += 1

        return html_code


class regelung():
    """Ein Objekt dieser Klasse entspricht einer Vertretungsregelung
    <tr class='list odd'><td class="list" align="center"><b>07C3</b></td><td class="list" align="center"><b>5</b></td><td class="list" align="center"><b>MA</b></td><td class="list" align="center"><b>TB</b></td><td class="list" align="center"><b>111</b></td><td class="list" align="center">TB</td></tr>

    """
    def __init__(self, klasse, stunde, kurs, lehrer, raum, vertreter):
        self.k = klasse
        self.s = stunde
        self.kurs = kurs
        self.l = lehrer
        self.r = raum
        self.v = vertreter

        self.debug()

    def debug(self):
        """Einfache Debugausgabe um Fehler zu finden"""
        print("Klasse {} in {}. Stunde im Kurs {} bei {} in Raum {} durch Kollegen {}".format(self.k, self.s, self.kurs, self.l, self.r, self.v))

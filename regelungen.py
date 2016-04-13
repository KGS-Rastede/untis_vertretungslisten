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

        self.zeit()
        #self.debug()

    def zeit(self):
        """mögliches Format ist '2' oder '3-6'
        Sinn der Methode ist es, im Fall von '3-6'
        auch die 4. und 5. Stunde zu identifizieren"""
        stunden = []

        if "-" not in self.s:
            return self.s
            #print("nur eine Stunde: {}".format(self.s) )
        else:
            startstunde = 3
            endstunde = 6
            for i in range(startstunde,endstunde+1):
                stunden.append(i)
            print(stunden)
            return stunden

    def debug(self):
        """Einfache Debugausgabe um Fehler zu finden"""
        print("Klasse {} in {}. Stunde im Kurs {} bei {} in Raum {} durch Kollegen {}".format(
            self.k, self.s, self.kurs, self.l, self.r, self.v))

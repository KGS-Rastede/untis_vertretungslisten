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

        #print(self.zeit())
        #self.debug()

    def zeit(self):
        """mögliches Format ist '2' oder '3-6'
        Sinn der Methode ist es, im Fall von '3-6'
        auch die 4. und 5. Stunde zu identifizieren"""
        stunden = []

        # Test, ob es eine Stunde betrifft oder mehr als eine
        if "-" not in self.s:
            stunden.append(int(self.s))
        else:
            startstunde = int( self.s[:1] ) #nur das erste Zeichen
            endstunde = int( self.s[4:] ) #ab dem 4. Zeichen

            for i in range(startstunde,endstunde+1):
                stunden.append(i)

        return stunden

    def debug(self):
        """Einfache Debugausgabe um Fehler zu finden"""
        print("Klasse {} in {}. Stunde im Kurs {} bei {} in Raum {} durch Kollegen {}".format(
            self.k, self.s, self.kurs, self.l, self.r, self.v))

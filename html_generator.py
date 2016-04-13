class html_generator():
    def __init__(self):
        self.vorne = ""
        self.hinten = ""
        self.lade_html()

    def lade_html(self):
        """speichert den Inhalt der Vorlagen in zwei Variablen"""
        with open('rumpfdatei_vorne.htm', 'r') as inf:
            self.vorne = inf.read()
        with open('rumpfdatei_hinten.htm', 'r') as inf:
            self.hinten = inf.read()

    def erzeuge_html(self, regelungen, zeilenzahl = 10):
        html_code = self.vorne
        counter = 0
        dateinummer = 1
        for r in regelungen:
            html_code += self.erzeuge_html_zeile(r)

            if counter % zeilenzahl is 0 and counter > 0:
                html_code += self.hinten
                self.schreibe_html(html_code, dateinummer)
                dateinummer += 1
                html_code = self.vorne # für neue Datei vorbereiten

            counter += 1

        # print("Regel {} wurde geschrieben".format(counter))

    def schreibe_html(self, html_code, nummer):
        """Schreibt den gegebene HTML_Code in die Datei mit der
        angegeben Nummer"""
        print("Schreibe Datei Nummer "+str(nummer))
        dateiname = "test_"+str(nummer)+".htm"
        with open(dateiname, 'w') as outf:
            outf.write(html_code)

    def erzeuge_html_zeile(self, regel):
        """Erzeugt eine HTML-Code Zeile entsprechend der Regel"""
        string = "<tr class=\'list odd\'><td class=\"list\" align=\"center\"><b>{}</b></td><td class=\"list\" align=\"center\"><b>{}</b></td><td class=\"list\" align=\"center\"><b>{}</b></td><td class=\"list\" align=\"center\"><b>{}</b></td><td class=\"list\" align=\"center\"><b>{}</b></td><td class=\"list\" align=\"center\">{}</td></tr>".format(regel.k, regel.s, regel.l, regel.kurs, regel.r, regel.v)
        # regel.debug()
        # print(string)
        return string

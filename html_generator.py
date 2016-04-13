class html_generator():
    def __init__(self):
        self.vorne = ""
        self.hinten = ""
        self.lade_html()

    def lade_html(self):
        with open('rumpfdatei_vorne.htm', 'r') as inf:
            self.vorne = inf.read()
        with open('rumpfdatei_hinten.htm', 'r') as inf:
            self.hinten = inf.read()

    def erzeuge_html(self, regelungen):
        html_code = self.vorne
        counter = 0
        for r in regelungen:
            counter += 1
            html_code += self.erzeuge_html_zeile(r)
            # print("drucke Regel")

        #print(html_code)
        html_code += self.hinten
        self.schreibe_html(html_code, 2)

    def schreibe_html(self, html_code, nummer):
        dateiname = "test"+str(nummer)+".htm"
        with open(dateiname, 'w') as outf:
            outf.write(html_code)

    def erzeuge_html_zeile(self, regel):
        string = "<tr class=\'list odd\'><td class=\"list\" align=\"center\"><b>{}</b></td><td class=\"list\" align=\"center\"><b>{}</b></td><td class=\"list\" align=\"center\"><b>{}</b></td><td class=\"list\" align=\"center\"><b>{}</b></td><td class=\"list\" align=\"center\"><b>{}</b></td><td class=\"list\" align=\"center\">{}</td></tr>".format(regel.k, regel.s, regel.l, regel.kurs, regel.r, regel.v)
        regel.debug()
        print(string)
        return string

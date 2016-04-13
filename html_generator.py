class html_generator():
    def __init__(self):
        self.vorne = ""
        self.hinten = ""
        self.lade_html()

    def lade_html(self):
        with open('rumpfdatei_vorne.htm', 'r') as f:
            self.vorne = f.read()
        with open('rumpfdatei_hinten.htm', 'r') as f:
            self.hinten = f.read()

    def erzeuge_html(self, regelungen):
        pass
        # print(self.vorne)

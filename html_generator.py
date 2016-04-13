class html_generator():
    def __init__(self):
        self.lade_html()

    def lade_html(self):
        with open('rumpfdatei_vorne.htm', 'r') as f:
            vorne = f.read()
        with open('rumpfdatei_hinten.htm', 'r') as f:
            hinten = f.read()

from bs4 import BeautifulSoup

html_doc_heute = open("subst_001.htm", 'r').read()
html_doc_morgen = open("subst_002.htm", 'r').read()


soup_heute  = BeautifulSoup(html_doc_heute, 'html.parser')
soup_morgen = BeautifulSoup(html_doc_morgen, 'html.parser')

print(soup_heute.head.contents[1])

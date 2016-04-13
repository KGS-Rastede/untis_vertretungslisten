from bs4 import BeautifulSoup

def erste_soups():
    html_doc_heute = open("subst_001.htm", 'r').read()
    html_doc_morgen = open("subst_002.htm", 'r').read()

    s1 = BeautifulSoup(html_doc_heute, 'html.parser')
    s2 = BeautifulSoup(html_doc_morgen, 'html.parser')
    return s1, s2

soup_heute, soup_morgen = erste_soups()


print(soup_heute.head.contents[1])
print(soup_morgen.head.contents[1])

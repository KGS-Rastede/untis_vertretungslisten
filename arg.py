from time import *
import locale

locale.setlocale(locale.LC_ALL, '')

lt = localtime()
print(strftime("%A, %x", lt))

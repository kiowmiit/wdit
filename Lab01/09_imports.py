# Pierwszy sposób na importowanie modułu
# import [module_name]
import math

# użycie modułu math i dostępnej w niej funkcji sqrt
print(math.sqrt(16))

# Drugi sposób importowania modułu
# import [module_name] as [alias]
import random as rd
print(rd.random())

# Trzeci sposób importowania modułu
# wczytuje podjedyncze elementy:
# from [module_name] import [element1, element2,...]
# lub wszystkie elementy z modułu:
# from [module_name] import *

from math import pi
print(pi)

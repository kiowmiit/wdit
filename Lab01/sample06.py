'''
Docstring do danego wcięcia. Jest nim zawsze pierwszy
komentarz wielolinijkowy z danym wcięciem
'''
'''
Normalny komentarz wielolinijkowy. Nie będzie
wyświetlony jako __doc__
'''

# Przykład komentarza jednolinijkowego

# __doc__ jest polem zawierającym opis zawarty w docstringu danego wcięcia (w tym przypadku pliku)
print(__doc__)

a = 8
b = 4
some_string = "Sample string"

# Podanie długości stringa
print(f"Lenght of string: {len(some_string)}")

# Przykład escape character
print(f"Is string starting with \"Sam\"? {some_string.startswith("Sam")}")

print(f"a is equal to b: {a == b}")
print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"b - a = {b - a}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b}")
print(f"a // b = {a // b}")
print(f"a % b = {a % b}")
print("AAstring" > "DString")
print("ZZString" >= "ZString")
print("zzString" >= "ZString")
#print(a + some_string)
print("First", end=", ")
print("second", end=",")
print("third", end=",")

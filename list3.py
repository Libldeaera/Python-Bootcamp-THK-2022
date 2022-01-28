"""
TUPLE: Demet sadece bir kere yaratılır ve
sonrasında değiştirilemezler, insert,append,delete eleman yapılamaz
"""
mytuple = ("apple", "banana", "cherry")
print(len(mytuple))
print(mytuple.index("banana"))

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)

"""
DICTIONARY:Sözlük, ekleme yapabilirsiniz, listeler gibidir,
key(anahtar) : value(değer) şeklinde elemanlarasahiptir.
her eleman arasında , kullanılır.
"""
thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
print(thisdict["brand"])

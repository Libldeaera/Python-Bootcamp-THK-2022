iste1=["merhaba", 'deneme','merhaba',"234",45,32,34.56]
liste2=[34,2,45,'merhaba']

z=liste1+liste2

#z listesindeki tüm 'merhabaları' silelim
sil=input("silinecek değeri giriniz")
sil=sil.lower()
print(z.count(sil))
if z.count(sil)==0:
print("Silmek istediğiniz kelime listede yok")
else:
  for i in z:
    if(i==sil):
      z.remove(sil)
      print(z)

z.clear()
print(z)
del z
print(z)

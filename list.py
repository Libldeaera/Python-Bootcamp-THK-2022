liste1=["merhaba", 'deneme','merhaba',"234",45,32,34.56]
liste2=[34,2,45,'merhaba']

z=liste1+liste2

#z listesindeki tüm 'merhabaları' silelim
sil=input("silinecek değeri giriniz")
sil=sil.lower
for i in z:
if(i==sil):
z.remove(sil)
print(z)

while True:
  if sil in z:
    z.remove(sil)
    else:
      break
      print(z)

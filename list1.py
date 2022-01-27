liste1=["merhaba", 'deneme','merhaba',"234",45,32,34.56]
liste2=[34,2,45,'merhaba']
z=liste1+liste2

# delete all the 'merhaba' in the z-list
sil=input("silinecek değeri giriniz")
sil=sil.lower()
print(z.count(sil))

# for i in z:
# if(i==sil):
if z.count(sil) == 0
  print("Silmek istediğiniz kelime listede yok!")
# z.remove(sil)
# print(z)
else:
  for i in z
    if(i == sil)
        z.remove(sil)
  print(z)
  
# while True:
#  if sil in z:
#    z.remove(sil)
#    else:
#      break
#      print(z)

z.clear()
print(z)
del z
print(z)

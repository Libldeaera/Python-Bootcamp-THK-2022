#FONKSIYONLARdef topla(a,b):
return a+b

#Main Programı
s=int(input("X Giriniz= "))
t=int(input("Y Giriniz= "))
isim=input("Adınızı Giriniz= ")
print(isim, topla(t,s), "yaşındadır")

#Recursion
def yenile(k):
  if k<=1:
    return 1
  else:
    result = k * yenile(k - 1)
    return result

print("\n\nRecursion Example Results")
print(yenile(6))


print("-------------HARNE HESAPLAMA-------------")
kullanıcı='berkay cubukcu'
ad=input("ad\nsoyad:")
if ad != kullanıcı:
   print("kullanıcı adınız yanlış!")

s='10184437288'
s1=input("TC numaranızı giriniz:")

if s1 != s:
   print("numarayı yanlış girdiniz!")

if (ad == kullanıcı) and (s1 == s):
   print("===========SİSTEME HOŞ GELDİNİZ============")
print("           1. DÖNEM YAZILI NOTLARI  ")
print("           TÜRKÇE")
not1=int(input("1. yazılı:"))
not2=int(input("2. yazılı:"))
not3=int(input("3. yazılı:"))
not4=int(input("4. yazılı:"))

ort=(not1+not2+not3+not4)/4
print("TÜRKÇE ortalamanız:",ort)

if ort >= 90 or ort == 100:
   print("_AA ortalama_ ")

elif ort >= 80 or ort <90:
     print("_BA ortalama_")

elif ort  >= 70 or ort < 80:
     print("BB ortalama")

else:
   print("FF ORTALAMA(DERS TEKRARI)")

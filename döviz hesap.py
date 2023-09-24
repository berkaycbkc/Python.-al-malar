import requests

import sys
url = "http://data.fixer.io/api/latest?access_key=3c68051bdc3e029df1818d7d6223867b&format=1"
print("===============EURO DÖVİZ İŞLEMİ================")

birinci_doviz = "EUR"
ikinci_döviz = input("(Çevirilecek) DÖVİZ KURU:")
miktar = float(input("BÜTÇE:"))


response = requests.get(url + birinci_doviz)

json_verisi = response.json()
try:
    print(json_verisi["rates"][ikinci_döviz] * miktar)
except KeyError:
    sys.stderr.write("Lütfen para birimlerini doğru girin")
    sys.stderr.flush()

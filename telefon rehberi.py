import menuler
import os

menuler.anamenuler()


##import kayıtmodulu
import kisi_ekle

rehberisimleri=[]

def anamenuler():
    secim =""
    while secim!="x":
        print("REHBER PROGRAMI")
        print("===============")
        print("1-Rehbere ekleme")
        print("2-Rehberi listeleme")
        print("x-çakış")
        secim = input("seçiminiz:")
        if secim == "1": kisi_ekle.ekle()
        if secim == "2": listelememenusu()

def listelememenusu():
    print("LİSTELEME MENÜSÜ")
    print("================")
    print("1-Listeleme")
    print("2-ada göre göre listeleme")
    print("X-anamenüye dön")
    secim = input("seçiminiz:")
    if secim == "1": listele.duzlistele()
    if secim == "2": listele.sıralılistele()
    if secim.lower() == "x": anamenu()

##import kayıtmodulu
import kisi_ekle

rehberisimleri=[]

def anamenuler():
    secim =""
    while secim!="x":
        print("REHBER PROGRAMI")
        print("===============")
        print("1-Rehbere ekleme")
        print("2-Rehberi listeleme")
        print("x-çakış")
        secim = input("seçiminiz:")
        if secim == "1": kisi_ekle.ekle()
        if secim == "2": listelememenusu()

def listelememenusu():
    print("LİSTELEME MENÜSÜ")
    print("================")
    print("1-Listeleme")
    print("2-ada göre göre listeleme")
    print("X-anamenüye dön")
    if secim == "1": duzlisteleme()
    if secim == "2": sıralılistele()
    if secim.lower() == "x": anamenu()

def duzlistele():
    print("\nREHBER KAYIT LİSTESİ")
    print("======================")
    dosya = open("rehber.txt","r")
    okunan = dosya.read()
    print(okunan)

    
def sıralılistele():
    print("\nREHBER KAYIT LİSTESİ")
    print("======================")
    dosya = open("rehber.txt","r")
    okunan = dosya.readlines()
    for a in okunan:
        print(a.strip())   

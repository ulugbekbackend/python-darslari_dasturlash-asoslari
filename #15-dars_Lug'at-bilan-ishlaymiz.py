# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 10:01:58 2022

@author: Ulug'bek
"""
talaba_0={
    'ism':'alijon',
    'familiya':'shamsiyev',
    'yosh':22,
    'fakultet':'matemtika',
    'kurs':4
    }
print(talaba_0.items())

for kalit,qiymat in talaba_0.items():
    print(f"Kalit:{kalit}")
    print(f"Qiymat:{qiymat}\n")

telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310'
    }
for k,q in telefonlar.items():
    print(f"{k.title()}ning telefoni {q}")

mahsulotlar = {
    'olma':10000,
    'anor':20000,
    'uzum':40000,
    'anjir':25000,
    'shaftoli':30000
    }
print(mahsulotlar.keys())

print("Do\'kondagi mahsulotlar")
for mahsulot in mahsulotlar.keys():
    print(mahsulot.title())

bozorlik = ['anor','uzum','non','baliq']
for mahsulot in mahsulotlar:
    if mahsulot in bozorlik:
        print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so\'m")

for buyum in bozorlik:
    if buyum not in mahsulotlar:
        print(f"Iltimos do\'koningizga {buyum} ham olib keling.")
 
print("Do\'konimizdagi mahsulotlar:")
for mahsulot in sorted(mahsulotlar):
    print(mahsulot.title())
    
print(telefonlar.values())

print("Foydalanuvchilar quyidagi telefonlar ishlatishadi:")
for telefon in telefonlar.values():
    print(telefon)

telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310',
    'hamida':'galaxy s9',
    'maryam':'huawei p30',
    'tohir':'iphone x',
    'umar':'iphone x'    
    }
print("Foydalanuvchilar quyidagi telefonlar ishlatishadi:")
for telefon in telefonlar.values():
    print(telefon)

print("Foydalanuvchilar quyidagi telefonlar ishlatishadi:")
for telefon in set(telefonlar.values()):
    print(telefon)

# set
toys={"ball","car","lamp","car",'bear'}
print(toys)

#  # AMALIYOT

python_words={
    'boolean':'mantiqiy qiymat',
    'integer':'butun son',
    'float':'o\'nlik son',
    'for':'takrorlanuvchi tskil',
    'if':'shart operatori'
    }
for key,value in sorted(python_words.items()):
    print(f"{key.title()}-{value}")

davlatlar = {
    "o'zbekiston":'toshkent',
    'aqsh':'washington d.c.',
    'rossiya':'moskva',
    'tojikiston':'dushanbe',
    "qirg'iziston":'bishkek',
    'qozog\'iston':'nursulton',
    'malayziya':'kuala-lumpur',
    'singapur':'sungapur',
    'italiya':'rim'}
for davlat in sorted(davlatlar.keys()):
    print(davlat.title())
for poytaxt in sorted(davlatlar.values()):
    print(poytaxt.title())

# davlat_1=input("Istalgan davlat nomini kiriting. ")
# poytaxt_1=davlatlar.get(davlat_1.lower(),"Bizda bunday malumot yo'q.")
# print(poytaxt_1)

menu = {
        'osh':20000,
        "lag'mon":22000,
        'non':4000,
        'choy':5000,
        'shashlik':12000,
        'somsa':6000,
        'tabaka':15000
        }
buyurtmalar=[]
print("3 ta taom buyurtma bering. ")
for n in range(3):
    buyurtmalar.append(input(f"{n+1}- taom: ").lower())
for buyurtma in buyurtmalar:
    if buyurtma in menu:
        print(f"{buyurtma.title()} {menu[buyurtma]} so\'m")
    else:
        print(f"Kechirasiz bizda {buyurtma.title()} yoq.")
















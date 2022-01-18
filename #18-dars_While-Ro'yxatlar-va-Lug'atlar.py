# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 05:37:49 2022

@author: Ulug'bek
"""

# ismlar=[]
# print("Yaqin do\'stlaringiz ro\'yxatini tuzamiz.")
# n=1
# while True:
#     savol=f"{n}-do\'stingizni ismini kiriting. "
#     ism=input(savol)
#     ismlar.append(ism)
#     javob = input("Yana ism qo'shasizmi? (ha/yo'q)")
#     if javob.lower()=='ha':
#         n+=1
#         continue
#     else:
#         break
# print("Do'stlaringiz ro'yxati:")
# for ism in ismlar:
#     print(ism.title())

# print("Do'stlaringiz yoshini saqlaymiz.")
# dostlar={}
# ishora=True
# while ishora:
#     ism=input("Do'stingizni ismni kiriting. ")
#     yosh=input(f"{ism.title()}ning yoshini kiriting/ ")
#     dostlar[ism]=int(yosh)
#     javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q) ")
#     if javob == "yo'q":
#         ishora = False
# for ism,yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")

cars = ['lacetti','nexia','toyota','nexia','audi','malibu','nexia']
car='nexia'
while car in cars:
    cars.remove(car)
print(cars)

# talabalar = ['hasan', 'husan', 'olim', 'botir']
# baholangan_talabalar = {}
# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f"{talaba.title()}ning bahosini kiriting: ")
#     print(f"{talaba.title()} baholandi")
#     baholangan_talabalar[talaba] = baho
# print(baholangan_talabalar)

# savat=[]
# while True:
#     mahsulot = input("Savatga mahsulot qo'shing:")
#     savat.append(mahsulot.lower())
#     javob = input("Yana mahsulot qo\'shasizmi?(ha/yo\'q)")
#     if javob.lower()!='ha':
#         break

# mahsulotlar={}
# while True:
#     mahsulot=input("Mahsulot nomini kiriting: ")
#     narx=input(f"{mahsulot.title()} mahsulot narxini kiriting")
#     mahsulotlar[mahsulot]=narx
#     javob=input("Yana mahsulot qo\'shasizmi? (ha/yo\'q') ")
#     if javob.lower()!='ha':
#         break

buyurtmalar = ['olma','anjir','uzum','qovun']
mahsulotlar = {'olma':20000,
               'shaftoli':25000,
               'tarvuz':18000,
               'uzum':22000}
while buyurtmalar:
    buyurtma=buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        narx=mahsulotlar[buyurtma]
        print(f"{buyurtma.title()} {narx} so\'m")
    else:
        print(f"Bizda {buyurtma.title()} yo\'q.")





# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 10:50:53 2022

@author: Ulug'bek
"""

# yosh=int(input("Yoshingiz nechchida? "))
# if yosh<=4:
#     print("Sizga kirish bepul.")
# elif yosh<=12:
#     print("Sizga kirish 5000 so\'m")
# elif yosh<=18:
#     print("Sizga kirish 8000 so\'m.")
# else:
#     print("Sizga kirish 10000 so\m.")

# yosh=int(input("Yoshingiz nechchida? "))
# if yosh<4:
#     narx=0
# elif yosh<=12:
#     narx=5000
# elif yosh<=18:
#     narx=8000
# else:
#     narx=10000
# print(f"Sizga kirish {narx} so\'m.")

# kun =input("Bugun nnima kun? ")
# if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#     print("Bugun dam olish kuni.")
# else:
#     print("Bugun ish kuni.")

# kun=input("Bugun qanday kun? ")
# harorat=float(input("Havo harorati qanday? "))
# if kun.lower()=='yakshanba' and harorat>=30:
#     print("Kittik cho\'milgani")
# else:
#     print("Uyda dam olamiz.")
 
# kun =input("Bugun qanday kun? ")
# harorat=float(input("Havo harorati qanday? ")
# if (kun.lower()=='shanba' or kun.lower()=='yakshanba') and harorat>30:
#     print("Kettik cho\'milgani.")
# else:
#     print("Uyda dam olamiz.")

#  # BOOLEAN

narx=15000
choy=True
salat=False
if choy and salat:
    narx=narx+10000
elif choy or salat:
    narx=narx+5000
print(f"Jami {narx} so\'m")

narx=15000
choy=True
salat=False
non=1
kampot=1
assorti=0
if choy:
    print("Mijoz choy oldi")
    narx=narx+3000
if salat:
    print("Mijoz salat oldi.")
    narx=narx+5000
if non:
    print("Mijoz non oldi.")
    narx=narx+2000
if kampot:
    print("Mijoz kampot oldi.")
    narx=narx+5000
if assorti:
    print("Mijoz assorti oldi")
    narx=narx+15000
print(f"Jami {narx} so\'m ")

menu = ['osh','qazonkabob','shashlik','norin','somsa']
print('manti' in menu) # menu da manti bormi?

# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# ovqat =input("Nima ovqat yeysiz? ")
# if ovqat.lower() in menu:
#     print("Buyurtma qabul qilindi.")
# else:
#     print("Afsuski bunday ovqat yo\'q.")

menu = ['osh','qazonkabob','shashlik','norin','somsa']
print('manti' not in menu) # menu da manti yoqmi?

# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# ovqat = input('Nima ovqat yeysiz?>>>')
# if ovqat.lower() not in menu:
#     print('Afsuski bizda bunday ovqat yo\'q')
# else:
#     print('Buyurtma qabul qilindi.')

#  # IKKI RO'YXATNI SOLISHTIRISH
menu = ['osh','qazonkabob','shashlik','norin','somsa']
buyurtmalar = ["osh","somsa","manti", "shashlik"]
for taom in buyurtmalar:
    if taom in menu:
        print(f"Menuda {taom} bor.")
    else:
        print(F"Kechirasiz menuda {taom} yo\'q.")

menu = ['osh','qazonkabob','shashlik','norin','somsa']
buyurtmalar = ["osh","somsa","manti", "shashlik"]

if buyurtmalar: # ro'yxatda biror element bo'lsa bu ifoda TRUE qaytaradi
    for taom in buyurtmalar:
        if taom in menu:
            print(f"Menuda {taom} bor")
        else:
            print(f"Kechirasiz, menuda {taom} yo'q")
else: # agar ro'yxat bo'sh bo'lsa
    print("Savatchangiz bo'sh!")

#  # AMALIYOT

# son=float(input("Juft son kiriting "))
# if son%2:
#     print("Bu juft son emas")
# else:
#     print("Rahmat")

# yosh=int(input("Yoshingiz nechchida "))
# if yosh<4 or yosh>60:
#     print("Sizga kirish bepul.")
# elif yosh<18:
#     print("Sizga kirish 10000 so\'m.")
# else:
#     print("Sizga kirish 20000 so\'m.")

# x=float(input("Birinchi sonni kiriting "))
# y=float(input("Ikkinchi sonni kiriting "))
# if x==y:
#     print(f"{x}={y}")
# elif x>y:
#     print(f"{x}>{y}")
# else:
#     print(f"{x}<{y}")

# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz','kartoshka', 'olma', 'banan', 'uzum', 'qovun']
# savat=[]
# for n in range(5):
#     savat.append(input(f"{n+1} mahsulot nomini kiriting ").lower())
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print("Mahsulot do\'konimizda bor")
#     else:
#         print("Mahsulot do\'konimizda yo\'q")


# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz','kartoshka', 'olma', 'banan', 'uzum', 'qovun']
# savat=[]
# for n in range(5):
#     savat.append(input(f"{n+1} mahsulot nomini kiriting ").lower())
# bor_mahsulotlar=[]
# mavjud_emas=[]
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)
# if mavjud_emas:
#     print("Do\'konimizda quyidagi mahsulotlar yo\'q:")
#     for mahsulot in mavjud_emas:
#         print(mahsulot)
# else:
#     print("Siz so\'ragan barcha mahsulotlar do\'konimizda bor")

# users = ['alisher','aziza','yasina','umar']
# login=input("Yangi login tanlang. ").lower()
# if login in users:
#     print("Login band, yangi login tanlang!")
# else:
#     print(f"Xush kelibsiz {login.title()} ")

son=int(input("Istalgan butun son kiriting "))
for n in range(2,11):
    if not son%n:
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")



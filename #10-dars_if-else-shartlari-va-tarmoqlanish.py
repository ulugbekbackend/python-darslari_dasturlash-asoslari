# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 05:29:58 2022

@author: Ulug'bek
"""

avtolar = ['audi','bmw','volvo','kia','hyundai']
for avto in avtolar:
    if avto=='bmw':
        print(avto.upper())
    else:
        print(avto.title())

ism='Ali'
if ism.lower()=='ali':
    print('ha')

#  # == ->tengmi?
#  # != ->teng emasmi?
#  # Kichik: a<b
#  # Kichik yoki teng: a<=b
#  # Katta: a>b
#  # Katta yoki teng: a>=b

# ism=input("ismingizni kiriting \n>>>")
# if ism.lower()!='ali':
#     print(f"Uzr {ism.title()} biz Alini kutayotgan edik.")    
# else:
#     print("Salom Ali")


# javob=input("6x12 nechchiga teng?")
# if javob!=72:
#     print("Bu xato javob!")

# yosh=int(input("Yoshingiz nechchida?"))
# if yosh>=18:
#     print("Xush kelibsiz")
# else:
#     print("Kirish mumkin emas!")

# login=input("Yangi login tanlang: \n")
# if len(login)<=5:
#     print("Login 5 harfdan ko\'proq bo\'lishi kerak.")

# yil=int(input("Tug\'ilgan yilingizni kiriting: "))
# if 2022-yil<18:
#     print(f"Siz {2022-yil} yoshda ekansiz!")
#     print("Kirish mumkin emas!")
# else:
#     print("Xush kelibsiz!")

# yosh=int(input("Yoshingiz nechchida \n"))
# if yosh>65:print("Siz COVID-19 risk guruhida ekansiz")

x,y =50,25
print('x>y') if x>y else print('x<y')

#  # AMALIYOT

cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car.lower()=='gm':
        print(car.upper())
    else:
        print(car.title())

cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars :
    if car.lower()!='gm':
        print(car.title())
    else:
        print(car.upper())

# login=input("Login kiriting: \n>>>")
# if login.lower()=='admin':
#     print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:    
#     print(f"xush kelibsiz {login.title()} !")

# a=float(input("a sonini kiriting "))
# b=float(input("b sonini kiriting "))
# if a==b:
#     print("a soni b soniga teng. ")

# son=float(input("Istalgan sonni kiriting "))
# if son>0:
#     print("Bu musbat son.")
# else:
#     print("Bu manfiy son.")
    
son=float(input("Son kiriting "))
if son>=0:
    print(f"{son} sonining ildizi {son**0.5} ga teng.")
else:
    print("Musbat son kiriting")



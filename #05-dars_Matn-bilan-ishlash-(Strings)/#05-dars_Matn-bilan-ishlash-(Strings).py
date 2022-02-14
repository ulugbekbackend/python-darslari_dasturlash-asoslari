# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 05:25:50 2021

@author: Ulug'bek
"""

# shaxar = "Қўқон"
# viloyat = "Фарғона"
# print(shaxar,viloyat)

# matn = "Men yangi 📱 oldim"
# print(matn)

# # STRING USTIDA AMALLAR

# ism = "Ahad"
# print("Mening ismim "+ism)

# ism = "Ahad"
# familiya = "Qayum"
# print(ism+familiya)
# print(ism+' '+familiya)

#  # f-sting

# ism = "Ahad"
# familiya = "Qayum"
# ism_sharif = f"{ism} {familiya}"
# print(ism_sharif)

# ism = "James"
# familiya = "Bond"
# ism_sharif = f"Mening ismim {ism}, {ism} {familiya}"
# print(ism_sharif)


# # MAXSUS BELGILAR

# print("Hello World")
# print("Hello \tworld")
# print("Hello \nWorld")

#  # STING METODLARI  # matn.string_nomi()

#  # upper() metodi har bir harfni katta harfga o'zgartiradi.

# ism = "ahad"
# familiya = "qayum"
# ism_sharif = f"{ism} {familiya}"
# print(ism_sharif.upper())

#  # lowr() metodi har bir harfni kichik harfga o'gartiradi.

# ism = "Ahad"
# familiya = "Qayum"
# ism_sharif = f"{ism} {familiya}"
# print(ism_sharif.lower())

#  # title() metodi har bir so'zni 1-harfini katta harfga o'zgartiradi.

# ism = "ahad"
# familiya = "qayum"
# ism_sharif = f"{ism} {familiya}"
# print(ism_sharif.title())

#  # capitalize() metodi faqatgina eng 1-so'zning 1-harfini katta harfga o'zgartiradi.

# ism = "ahad"
# familiya = "qayum"
# ism_sharif = f"{ism} {familiya}"
# print(ism_sharif.capitalize())

#  # strip()  rstrip() lstrip()  METODLARI
#  # lstrip() matnni chap tomonidagi,
#  # rstrip() matnni o'ng tomonidagi,
#  # strip() matnni chap va o'ng tomonidagi bosh joyni olib tashlaydi.

# meva = "    olma    "
# print("Men " + meva.lstrip() + " yaxshi ko\'raman.")
# print("Men " + meva.rstrip() + " yaxshi ko\'raman.")
# print("Men " + meva.strip() + " yaxshi ko\'raman.")
# print("Men "+meva+" yaxshi ko\'raman")

#  # INPUT METODI

# ism = input("Ismingizni nima:")
# print("Assalomu alaykum "+ism)

# ism = input("Ismingizni nima: \n>>>")
# print("Assalomu alaykum "+ism.title())

#  # AMALIYOT

# kocha = "Bog'bon"
# mahalla = "Sog'bon"
# tuman = "Bodomzor"
# viloyat = "Samarqand"
# manzil = f"{viloyat} viloyati, {tuman} tumani, {mahalla} mahallasi, {kocha} ko\'chasi."
# print(manzil)

# kocha = input("Ko\'cha nomini kiriting \n>>>")
# mahalla = input("Mahalla nomini kiriting \n>>>")
# tuman = input("Tuman nomini kiriting \n>>>")
# viloyat = input("Viloyat nomini kiriting \n>>>")
# manzil = f"{viloyat} viloyati, {tuman} tumani, {mahalla} mahallasi, {kocha} ko\'chasi."
# print(manzil)

# kocha = "Bog'bon"
# mahalla = "Sog'bon"
# tuman = "Bodomzor"
# viloyat = "Samarqand"
# print(kocha + " ko'chasi,\n" + mahalla + " mahallasi,\n" + \
#       tuman + " tumani,\n" + viloyat + " viloyati")

kocha = "Bog'bon"
mahalla = "Sog'bon"
tuman = "Bodomzor"
viloyat = "Samarqand"
manzil = f"{viloyat} viloyati, {tuman} tumani, {mahalla} mahallasi, {kocha} ko\'chasi."
print(manzil.title())
print(manzil.upper())
print(manzil.lower())
print(manzil.capitalize())



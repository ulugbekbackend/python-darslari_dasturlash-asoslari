# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 18:34:02 2022

@author: Ulug'bek
"""

# def toliq_ism_yasa(ism, familiya):
#     """To'liq ismni qaytaruvchi dastur."""
#     toliq_ism=f"{ism.title()} {familiya.title()}" # Mahalliy o'zgaruvchi(local variables)
#     return toliq_ism
# talaba1=toliq_ism_yasa('olim','hakimov')
# talaba2=toliq_ism_yasa('hakim','olimov')
# print(f"Darsga kelmagan talabalar {talaba1}, {talaba2}.")

# def toliq_ism_yasa(ism,familiya,otasining_ismi=''):
#     """To'liq ismni qaytaruvchi dastur."""
#     if otasining_ismi:
#         toliq_ism=f"{ism} {familiya} {otasining_ismi}"
#     else:
#         toliq_ism=f"{ism} {familiya}"
#     return toliq_ism.title()
# talaba1=toliq_ism_yasa('olim','hakimov')
# talaba2=toliq_ism_yasa('hakim', 'olimov', 'abrorovich')
# print(f"Darsga kelmagan talabalar {talaba1}, {talaba2}.")

# def avto_info(kompaniya,model,rangi,karobka,yili,narxi=None):
#     avto={
#         'kompaniya':kompaniya,
#         'model':model,
#         'rang':rangi,
#         'karobka':karobka,
#         'yil':yili,
#         'narx':narxi
#         }
#     return avto
# avto1=avto_info('gm','malibu','qora','avtomat',2018)
# avto2=avto_info('gm','gentra','qora','avtomat',2016,15000)
# avtolar=[avto1,avto2]
# print("Onlayn bozordagi mavjud avtomashinalar:")
# for avto in avtolar:
#     if avto['narx']:
#         narx=avto['narx']
#     else:
#         narx='Nomalum'
#     print(f"{avto['rang']} {avto['model']} Narxi:{narx}.")

# def oraliq(min,max):
#     sonlar=[]
#     while min<max:
#         sonlar.append(min)
#         min += 1
#     return sonlar
# print(oraliq(1,11))

# print("Saytimizdagi avtolar royxatini shakllantiramiz")
# avtolar=[]
# while True:
#     print("\nQuyidagi malumotlarni kiriting.", end='')
#     kompaniya=input("Ishlab chiqaruvchi: ")
#     model=input("Modeli: ")
#     rangi=input("Rangi: ")
#     korobka=input("Korobka: ")
#     yili=input("Ishlab chiqarilgan yili: ")
#     narxi=input("Narhi: ")
#     avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
#     javob = input("Yana avto qo'shasizmi? (yes/no): ")
#     if javob=='no':
#         break
# print("Salonimizdadi avtolar")
# for avto in avtolar:
#     if avto['narx']:
#         narx=avto['narx']
#     else:
#         narx='Nomalum'
# print(f"{avto['rang'].title()} {avto['model'].title()} {korobka} korobka narxi: {narx}")

#  # AMALIYOT
def oraliq_qadam(min,max,qadam=1):
    sonlar=[]
    while min<max:
        sonlar.append(min)
        min += qadam
    return sonlar
print(oraliq_qadam(10, 15))
print(oraliq_qadam(10, 101,5))

# def mijoz_info(ism,familiya,tyil,tjoy,email='',tel='None'):
#     """Mijoz haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
#     mijoz={
#         'ism':ism,
#         'familiya':familiya,
#         'tyil':tyil,
#         'tjoy':tjoy,
#         'email':email,
#         'telefon':tel
#         }
# print("Mijoz haqida ma'lumotlarni kiriting.")
# mijozlar=[]
# while True:
#     ism = input("Ismi: ")
#     familiya = input("Familiyasi: ")
#     tyil = int(input("Tug'ilgan yili: "))
#     tjoy = input("Tug'ilgan joyi: ")
#     email = input("Email: ")
#     telefon = input("Telefon raqami: ")
#     mijozlar.append(mijoz_info(ism, familiya, tyil, tjoy, email, telefon))
#     javob = input("Davom etasizmi? (ha/yo'q)")
#     if javob.lower()!='ha':
#         break
# print("Mijozlar:")
# for mijoz in mijozlar:
#     print(f"{mijoz['ism'].title()} {mijoz['familiya'].title()}," 
#           f"{mijoz['yoshi']} yoshda, telefoni: {mijoz['telefon']}")

# def kattasi(x,y,z):
#     max=x
#     if y>=max:
#         max=y
#     if z>=max:
#         max=z
#     return max
# print(kattasi(12,15,19))









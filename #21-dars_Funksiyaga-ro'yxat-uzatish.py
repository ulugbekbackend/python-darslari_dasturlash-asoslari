# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 19:25:27 2022

@author: Ulug'bek
"""

# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism=ismlar.pop()
#         baho=int(input(f"Talaba {ism.title()}ning bahosini kiriting: "))
#         baholar[ism]=baho
#     return baholar
# # talabalar = ['ali', 'vali', 'hasan', 'husan']
# # baholar = bahola(talabalar)
# # print(baholar)

# talabalar = ['ali', 'vali', 'hasan', 'husan']
# baholar = bahola(talabalar[:])  # !!! Royxatdan nusxa kochirish
# print(baholar)
# print(talabalar)

def katta_harf(matnlar):
    for i in range(len(matnlar)):
        matnlar[i]=matnlar[i].title()
ismlar=['ali','vali','hasan','husan']
katta_harf(ismlar)
print(ismlar)

def katta_harflar(matnlar):
    matnlar=matnlar[:]
    for i in range(len(matnlar)):
        matnlar[i]=matnlar[i].title()
    return matnlar
ismlar=['ali','vali','hasan','husan']
yangi_ismlar=katta_harflar(ismlar)
print(ismlar)
print(yangi_ismlar)
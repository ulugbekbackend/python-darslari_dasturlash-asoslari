# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 11:37:22 2022

@author: Ulug'bek
"""

def salom_ber():
    """Salom beruvchi funksiya"""
    print("Assalomu alaykum!")
salom_ber()

def salom_ber(ism):
    """Fodyalanuvchi ismini qabul qilib, unga salom beruvchi funksiya"""
    print(f"Assalomu alaykum, hurmatli {ism.title()}!")
salom_ber('olim')

def toliq_ism(ism, familiya):
    """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
    print(f"Foydalanuvchi ismi: {ism.title()}\n"
          f"Foydalanuvchi familiyasi: {familiya.title()}")
toliq_ism('olim','hakimov')
toliq_ism(familiya='hakimjonov', ism='salim')

def yosh_hisobla(ism, tugilgan_yil):
    """Foydalanuvchi yoshini hisoblaydigan dastur"""
    print(f"{ism.title()} {2020-tugilgan_yil} yoshda")
yosh_hisobla('olim',1997)

def yosh_hisobla(tugilgan_yil, joriy_yil=2022):
    """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
    print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
yosh_hisobla(2004)

def tyiltop(ism, yosh):
    print(f"{ism.title()} {2020-yosh} yoshda")
tyiltop('olim',2002)

def kv_kub(son):
    """Kiritilgan sonning kvadrati va kubini konsolga chiqaruvchi funksiya"""
    print(f"{son} ning kvadrati {son**2} ga, kubi {son**3} ga teng")
kv_kub(-4)

def juftmi(son):
    """Kiritilgan son juft yoki toqligini konsolga chiqaruvchi funksiya"""
    if son%2:
        print(f"{son} toq son")
    else:
        print(f"{son} juft son")
juftmi(20)
juftmi(123)

def solishtir(x,y):
    """Ikki sonni solishtiruvchi funksiya"""
    if x>y:
        print(f"{x}>{y}")
    elif x<y:
        print(f"{y}>{x}")
    else:
        print(f"{x}={y}")
solishtir(10,20)
solishtir(-9,12)
solishtir(1223*5,5**4)

def daraja(x,y=2):
    print(f"{x} ning {y}-darajasi {x**y} ga teng")
daraja(5,2)
daraja(3,3)
daraja(94,4)
daraja(6)

def bolinish_alomatlari(son):
    for n in range(2,11):
        if not son%n:
            print(f"{son} {n} ga qoldiqsiz bo'linadi")
bolinish_alomatlari(20)









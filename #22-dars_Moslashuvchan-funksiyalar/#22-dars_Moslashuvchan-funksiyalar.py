# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 04:20:09 2022

@author: Ulug'bek
"""

def summa(*sonlar):
    yigindi=0
    for son in sonlar:
        yigindi+=son
    return yigindi
print(summa(1,2))
print(summa(1,2,3,4,5))
print(summa(55,66,42,88))


def sonlar_yigindisi(x,y,*sonlar):
    return x+y+sum(sonlar)
print(sonlar_yigindisi(8,6))
print(sonlar_yigindisi(5,3,8,6,4,1))


def avto_info(kompaniya,model,**malumotlar):
    malumotlar['kompaniya']=kompaniya
    malumotlar['model']=model
    return malumotlar
print(avto_info("GM", "malibu", rang='qora', yil=2018))
print(avto_info("Kia", "K5", rang='qizil', narh=35000))

#  # AMALIYOT

def sonlar_kopaytmasi(*sonlar):
    kopaytma=1
    for son in sonlar:
        kopaytma*=son
    return kopaytma
print(sonlar_kopaytmasi(5,2,3,6,8))

def talaba_info(ism,familiya,**malumotlar):
    malumotlar['ism']=ism
    malumotlar['familiya']=familiya
    return malumotlar
print(talaba_info('olim','olimov',tyil=1995,fakultet='IT',yonalish='AT'))




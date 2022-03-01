# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 15:07:22 2022

@author: Ulug'bek
"""


import random as r

print("1 dan 10 gacha son o'yladim. Topa olasizmi?")
x=r.randint(1,10)
t=0
while True:
    a=int(input(">>>"))
    t+=1
    if a==x:
        print(f"Topdingiz! Men {a} sonini o'ylagandim.{t} ta taxmin bian topdingiz. Tabriklayman!")
        break
    if x>a:
        print("Xato. Men o'ylagan son bundan kattaroq. Yana harakat qilib koring.")
    if x<a:
        print("Xato. Men o'ylagan son bundan kichikroq. Yana harakat qilib qoying.")

print("1 dan 10 gacha son o'ylang. Men topishga harakat qilaman.")
input("Son o'ylagan bo'lsaniz 'Enter' tugmasini bosing.")
t1=0
quyi=1
yuqori=10
while True:
    b=r.randint(quyi,yuqori)
    t1+=1
    c=str(input(f"Siz {b} sonini o'yladingiz:\n To'g'ri(T), men o'ylagan son bundan kattaroq(+), yoki kichikroq(-) \n>>>".lower()))
    if c=='t':
        print(f"Siz {b} sonini o'ylabsiz. Men {t1} ta taxminda topdim ")
        break
    if c=='+':
        quyi=b+1
    if c=='-':
        yuqori=b-1    
    

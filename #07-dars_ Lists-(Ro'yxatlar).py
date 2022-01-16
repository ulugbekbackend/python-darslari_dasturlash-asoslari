# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 14:04:18 2021

@author: Ulug'bek
"""

mevalar = ["olma", "anor", "o'rik", "shaftoli"]
narxlar=[12000,15000,10000,20500]
sonlar=['bir','ikki',3,4,5]
ismlar=[]


print("Birinchi meva:",mevalar[0])
print("Ikkinchi meva:",mevalar[1])
print("Oxirgi meva:",mevalar[-1])


mevalar = ["olma", "anor", "o'rik", "shaftoli"]
print("Birrinchi meva:",mevalar[0].upper())
print("Ikkinchi meva",mevalar[1].title())

narxlar=[12000,15000,10000,20500]
print(narxlar[2]+narxlar[3])

#  # Elementlarni o'zgartirish
narxlar=[12000,15000,10000,20500]
narxlar[0]=13000
narxlar[1]=14000
narxlar[2]=narxlar[2]+2000
print(narxlar)

#  # Oxiriga yangi element qo'shish 
mevalar = ["olma", "anor", "o'rik", "shaftoli"]
mevalar.append("tarvuz")
print(mevalar)

cars=[]
cars.append('Lasetti')
cars.append('Nexia')
cars.append('Malibu')
print(cars)

#  # Istalgan joyga yangi element qo'shish
cars=['Lasetti', 'Nexia', 'Malibu']
cars.insert(0,'Cobalt')
print(cars)

cars.insert(1, 'Damas')
print(cars)


#  # Elementlarni o'chirish
mevalar = ["olma", "anor", "o'rik", "shaftoli"]
del mevalar[1]
print(mevalar)

mevalar = ["olma", "anor", "o'rik", "shaftoli"]
mevalar.remove('shaftoli')
print(mevalar)


#  # Elementlarni sug'urib olish
bozorlik=['un','go\'sht','piyoz','kartoshka']
mahsulot=bozorlik.pop(1)
print("Men "+mahsulot+" sotib oldim.")
print("Olinmagan mahsulotlar:",bozorlik)


#  # AMALIYOT

ismlar=['Ali','Hasan','Husan','G\'ani']
print("Salom "+ismlar[0]+" qalesan")
print(f"{ismlar[1]} va {ismlar[2]} egizaklar")
print(ismlar[-1]+" g\'ildirakni g\'zillatib g\'ildiratdi")

sonlar=[1,5,3.2,-5,2]
print(sonlar)

sonlar=[1,5,3.2,-5,2]
sonlar[0]=8
sonlar[-1]=sonlar[-1]+8
del sonlar[3]
print(sonlar)


t_shaxslar = ['Amir Temur','Imom Buxoriy', 'Napoleon']
z_shaxslar = ['Bill Gates', 'Elon Musk', 'Doasnald Trump']
print(f"\nMen tarixiy shaxslardan {t_shaxslar.pop(1)} bilan,\n\
zamonaviy shaxslardan esa {z_shaxslar.pop(0)} bilan\n\
suhbat qilishni istar edim\n")

friends=[]
friends.append("Ali")
friends.append('Vali')
friends.append("G\'ani")
print(friends)

friends.remove("G\'ani")
print(friends)

friends.append('Hasan')
friends.insert(0, 'Husan')
friends.insert(2, 'Ivan')
print(friends)

mehmonlar=[]
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(-1))
mehmonlar.append(friends.pop(2))
print("Kelgan mehmonlar:",mehmonlar)







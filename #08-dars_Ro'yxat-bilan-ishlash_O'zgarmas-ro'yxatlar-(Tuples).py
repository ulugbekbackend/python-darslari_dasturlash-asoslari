# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 19:39:44 2022

@author: Ulug'bek
"""

cars=['bmw','tesla','audi','volvo','ferrari','general motors']
cars.sort()
print(cars)

cars=['bmw','Tesla','audi','volvo','ferrari','general motors']
cars.sort() 
print(cars)

# # Teskari tartibda tartiblash
cars=['bmw','tesla','audi','volvo','ferrari','general motors']
cars.sort(reverse=True)  
print(cars)

cars=['bmw','tesla','audi','volvo','ferrari','general motors']
print("sorted() qaytargan ro\'yxat:",sorted(cars))
print("Asl ro\'yxat o\'zgarmas qoldi':",cars)
print("Teskari tartibdagi ro\'yxat: ",sorted(cars,reverse=True))

ages = [12, 98, 34, 65, 34, 76, 11]
ages.sort()
print(ages)
print(sorted(ages,reverse=True))

#  # Royxatni aylantirish
fruits = ['pear','banana','apple','watermelon','lemon']
fruits.reverse()
print(fruits)

fruits = ['pear','banana','apple','watermelon','lemon']
print("Elementlar soni:",len(fruits))

sonlar = list(range(0,10)) 
print(sonlar)

juft_sonlar = list(range(0,20,2)) # 0 dan 20 gacha 2 qadam bilan
toq_sonlar = list(range(1,20,2))  # 1 dan 20 gacha 2 qadam bilan
print("Juft sonlar: ", juft_sonlar)
print("Toq sonlar: ", toq_sonlar)

narhlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
arzon = min(narhlar)
qimmat = max(narhlar)
jami = sum(narhlar)
print("Eng arzon narh ", arzon, ". Eng qimmati ", qimmat, ". Jami: ", jami)


cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
my_cars = cars[0:3] # 0-indeskdan boshlab 3 ta element ajratib olamiz
print(my_cars) 
print(cars[2:5]) # 2-3-4-elementlarni ajratib olamiz (5 kirmaydi)
print(cars[:4]) # Ro'yxat boshidan 4-gacha kesadi (0,1,2,3)
print(cars[2:]) # 2-elementdan boshlab ro'yxat oxirigacha kesib oladi

sonlar = [1, 2, 3, 4, 5] 
sonlar2 = sonlar[:] # [:] ro'yxatni to'liq ko'chirib oladi 
# # # !!! sonlar2=sonlar deb nusxa ko'chirib bo'lmaydi!
sonlar2.append(6) 
sonlar2.append(7) 
print("Bu sonlar ro'yxati:", sonlar)
print("Bu sonlar2 ro'yxati:", sonlar2)


#  # O'zgarmas qiymat
tomonlar = (20, 30, 55.2)
print(tomonlar)

toys = ('bus','car','bear','dino','snake','lizard')
print(toys[0])
print(toys[-1])
print(toys[2:5])

toys = ('bus','car','bear','dino','snake','lizard')
toys=list(toys)
toys.append('dragon')
toys.remove('bus')
toys=tuple(toys)
print(toys)


#  # AMALIYOT
#O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
davlatlar = ["O'zbekiston","Qozog'iston", "Rossiya", "Malayziya", "Singapur", "AQSh"]
print(davlatlar)
print(len(davlatlar))
print(sorted(davlatlar))
print(sorted(davlatlar,reverse=True))

davlatlar.reverse()
print(davlatlar)

davlatlar = ["O'zbekiston","Qozog'iston", "Rossiya", "Malayziya", "Singapur", "AQSh"]
davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)

sonlar=list(range(120,1200))
print(sum(sonlar))
print(max(sonlar)-min(sonlar))
print(len(sonlar))
print(sonlar[:20])
print(sonlar[-20:])
print(sonlar[530:550])

taomlar = ['osh','somsa','norin','shashlik','qozonkabob']
nonushta=taomlar[:]
nonushta.remove('norin')
nonushta.remove('shashlik')
nonushta.remove('qozonkabob')
nonushta.append('non va qaymoq')
nonushta.append('issiq non')
print(taomlar)
print(nonushta)
nonushta=tuple(nonushta)
print(type(nonushta))
print(nonushta)
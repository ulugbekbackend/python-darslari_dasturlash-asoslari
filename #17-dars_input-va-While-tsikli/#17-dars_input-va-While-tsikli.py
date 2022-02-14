# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 19:58:25 2022

@author: Ulug'bek
"""

# ism = input("Ismingiz nima: ")
# print(f"Salom {ism.title()}.")

# ism = input("Ismingiz nima? ")
# savol=f"Salom {ism.title()} Yoshing nechida? "
# yosh=input(savol)
# yosh=int(yosh)
# height=input("Bo\'yingiz necha metr? ")
# height=float(height)

son=1
while son<=5:
    print(son,end=' ')
    son+=1
print("Dastur tugadi.")

# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol="Istalgan sonni kiriting"
# savol+="(dasturni to'xtatish uchun exit deb yozing.')\n"
# qiymat=''
# while qiymat!='exit':
#     qiymat=input(savol)
#     if qiymat!='exit':
#         print(float(qiymat)**2)

# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol="Istalgan sonni kiriting"
# savol+="(dasturni to'xtatish uchun exit deb yozing.')\n"
# ishora=True
# while ishora:
#     qiymat=input(savol)
#     if qiymat=='exit':
#         ishora=False
#     else:
#         print(float(qiymat)**2)

# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol="Istalgan sonni kiriting"
# savol+="(dasturni to'xtatish uchun exit deb yozing.')\n"

# while True: # abadiy tsikl
#     qiymat=input(savol)
#     if qiymat=='exit':
#         break
#     else:
#         print(float(qiymat)**2)

# sonlar = list(range(1,11))
# for son in sonlar: 
#     if son == 5: # son 5 ga teng bo'lsa kod to'xtaydi
#         break
#     print(f"{son} ning kvadrati {son**2} ga teng")

# sonlar = list(range(1,11))
# for son in sonlar: 
#     if son == 5: # son 5 ga teng bo'lsa kod to'xtaydi
#         continue
#     print(f"{son} ning kvadrati {son**2} ga teng")

son=0
while son<=10:
    son+=1
    if son%2!=0:
        continue
    else:
        print(son)

#  # ABADIY TSIKL TUZOG'I
# infinite loop
# son = 0
# while son<10:
#     if son%2!=0:
#         continue
#     else:
#         print(son)

# son = 1
# while son>0: 
#     son += 1
#     if son%2!=0:
#         continue
#     else:
#         print(son)

#  # AMALIYOT

savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat=='Exit':
#         break
#     elif qiymat=='exit':
#         break
#     elif float(qiymat)<0:
#         print("Faqat Musbat son kiriting.")
#         continue
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")
# print("Dastur tugadi.")


# savol = "Sevgan kitobingizni kiriting"
# savol += "(barcha kitoblarni kiritib bo'lgach 'exit' deb yozing): "

# while True:
#     kitob=input(savol)
#     if kitob.lower()=='exit':
#         break
# print("Rahmat")

savol="Yoshingizni kiriting"
savol += "(barcha kitoblarni kiritib bo'lgach exit quit deb yozing): "
while True:
    qiymat=input(savol)
    if qiymat.lower()=='exit' or qiymat.lower()=='quit':
        break
    yosh=int(qiymat)
    if yosh<7:
        narx=2000
    elif 7<=yosh<18:
        narx=3000
    elif 18<=yosh<65:
        narx=1000
    else:
        narx=0
    if narx==0:
        print("Sizga chipta bepul")
    else:
        print(f"Sizga chipta {narx} so\'m")





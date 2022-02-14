# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 18:39:54 2022

@author: Ulug'bek
"""
mehmonlar=['Ali','Vali','Hasan','Husan','Olim']
for mehmon in mehmonlar:
    print("Qalesan ",mehmon)
    print("xayr,",mehmon)

mehmonlar=['Ali','Vali','Hasan','Husan','Olim']
for mehmon in mehmonlar:
    print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz")
    print("Hurmat bilan, Palonchiyevlar oilasi")

sonlar=list(range(1,11))
for son in sonlar:
    print(f"{son} ning kvadrati {son**2} ga teng.")

sonlar=list(range(1,11))
sonlar_kvadrati=[]
for son in sonlar:
    sonlar_kvadrati.append(son**2)
print(sonlar)
print(sonlar_kvadrati)

# dostlar=[]
# print("5 ta do\'stingizni kiriting.")
# for n in range(5):
#     dostlar.append(input(f"{n+1} do\'stingizni ismini kiriting:"))
# print(dostlar)


#  # AMALIYOT

ismlar = ['Ali','Vali','Hasan','Husan','Olim']
for ism in ismlar:
    print(f"Salom {ism} qalesan?")

print(f"Kodlar {len(ismlar)} marta takrorlandi.")

sonlar=list(range(11,100,2))
for son in sonlar:
    print(f"{son} sonining kubi {son**3} ga teng.")

# kinolar=[]
# for n in range(5):
#     kinolar.append(input(f"{n+1}- kino nomini kiriting."))
# print(kinolar)



n_odamlar=int(input("Bugun nech kishi bilan uchrashdiz: "))
ismlar=[]
for n in range(n_odamlar):
    ismlar.append(input(f"{n+1}- uchrashgan odamiz ismini kiriting:"))
print(ismlar)






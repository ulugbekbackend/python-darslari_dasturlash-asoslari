# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 21:14:30 2022

@author: Ulug'bek
"""

car_0={'model':'Ferrari','rang':'qizil'}
print(car_0['model'])
print(car_0['rang'])

talaba_0={'ism':'murod olimov','yosh':20,'t_yil':2000}
print(f"{talaba_0['ism'].title()},\
 {talaba_0['t_yil']}- yilda tug\'ilgan,\
 {talaba_0['yosh']} yoshda.")

talaba_0['kusr']=4
talaba_0['fakultet']='informatika'
print(talaba_0)

talaba_1={}
talaba_1['ism']='qobil rasulov'
talaba_1['kurs']=3
talaba_1['yosh']=20
print(talaba_1)
print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")

talaba_0={'ism':'murod olimov','yosh':20,'t_yil':2000}
print(talaba_0)
del talaba_0['yosh']
print(talaba_0)

telefonlar={
    'ali':'IphoneX',
    'vali':'galaxy s9',
    'olim':'mi 10',
    'orif':'nokia'
    }
phone=telefonlar.get('hasan','Bunday ism mavjud emas')
print(phone)
phone_1=telefonlar.get('husan')
print(phone_1)

#  # AMALIYOT

otam = {'ism':'mavlutdin', 'tyil':1954,'viloyat':'samarqand'}
ism=otam['ism']
tyil=otam['tyil']
vil=otam['viloyat']
print(f"Otamning ismi {ism.title()} {tyil}-yilda {vil.title()} viloyatida tug\'ilgan.")

taomlar={
    'ali':'osh',
    'vali':'shashlik',
    'hasan':'lag\'mon',
    'husan':'mastava',
    'olim':'somsa'
    }
print(f"Alining sevimli taomi {taomlar['ali']}")

# python_izohli_lugati={
#     'integer':'Butun son',
#     'float':'O\'nlik son',
#     'string':'Matn',
#     'list':'Ro\'yxat',
#     'tuple':'O\'zgarmas ro\'yxat'
#     }
# kalit=input("Kalit so\'z kiriting. ").lower()
# print(python_izohli_lugati.get(kalit,'Bunday kalit so\'z mavjud emas'))


python_izohli_lugati={
    'integer':'Butun son',
    'float':'O\'nlik son',
    'string':'Matn',
    'list':'Ro\'yxat',
    'tuple':'O\'zgarmas ro\'yxat'
    }
kalit=input("Kalit so\'z kiriting. ").lower()
tarjima=python_izohli_lugati.get(kalit)
if tarjima==None:
    print("Bunday so\'z mavjud emas")
else:
    print(f"{kalit.title()} so\'zi {tarjima} deb tarjima qilinadi")




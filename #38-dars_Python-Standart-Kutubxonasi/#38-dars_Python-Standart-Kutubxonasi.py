import datetime as dt


hozir = dt.datetime.now()
print(hozir)

# sanani ajratib olish
print(hozir.date())
# vaqtni ajratib olish
print(hozir.time())
# soatni ajratib olish
print(hozir.hour)
# minutni ajratib olish
print(hozir.minute)
# sekundni ajratib olish
print(hozir.second)

bugun = dt.date.today()
print(f"Bugungi sana: {bugun}")
ertaga = dt.date(2023, 1, 14)
print(f"Ertangi sana: {ertaga}")

hozir = dt.datetime.now()
vaqtHozir = hozir.time()
print(f"Hozir soat: {vaqtHozir}")
vaqtKeyin = dt.time(23,45,00)
print(vaqtKeyin)

bugun = dt.date.today()
qurbonHayit = dt.date(2023, 3, 19)
farq = qurbonHayit-bugun
print(farq)
print(f"Qurbon Hayitiga {farq.days} kun qoldi")

hozir = dt.datetime.now()
futbol = dt.datetime(2023, 1, 22, 23, 45, 00)
farq= futbol-hozir
sekundlar = farq.seconds
minutlar = int(sekundlar/60)
soatlar = int(minutlar/60)
print(f"Futbol boshlanishiga {sekundlar} sekund qoldi")
print(f"Futbol boshlanishiga {minutlar} minut qoldi")
print(f"Futbol boshlanishiga {soatlar} soat qoldi")

# vaqtni millisekundsiz chiqaramiz
vaqt = hozir.strftime("%H:%M:%S")
print(f"Hozir soat: {vaqt}")
# sanani kun-oy-yil koʻrinishida chiqaramiz
sana = hozir.strftime("%d-%m-%Y")
print(f"Bugun sana: {sana}")
# sanani kun/oy/yil koʻrinishida chiqaramiz
sana_vaqt = hozir.strftime("%d.%m.%Y, %H:%M")
print(sana_vaqt)

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
import math
PI = math.pi
print(f"PI ning qiymati: {PI}")
E = math.e
print(f"e ning qiymati: {E}")
print(math.sin(math.pi/2))
print(math.cos(0))
print(math.tan(PI))
print(math.degrees(math.pi/2))
print(math.radians(90))
# natural logarifm
print(math.log(5))
# 10 asosli logarifm
print(math.log10(100))
# son;arni yaxlitlash
x = 4.6
print(math.ceil(x))
print(math.floor(x))

x = 81

# Kvadrat ildiz
print(math.sqrt(x))
# Darajaga oshirish
print(math.pow(x,3)) # x ning kubi
print(math.pow(x,1/3)) # x dan kub ildiz

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
from pprint import pprint
import json

filename = 'bemor.json'
with open(filename) as f:
    bemor = json.load(f)

pprint(bemor)

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
import re

word1 = "темир"
word2 = "томир"
word3 = "тулпор"

andoza = "^т...р$"

print(re.match(andoza, word1))
print(re.match(andoza, word2))
print(re.match(andoza, word3))

from uzwords import words
andoza = "^т...р$"

matches = []
for word in words:
    if re.match(andoza,word):
        matches.append(word)
print(matches)

matn = """Maqolalar  2020-yilning 20-martiga qadar rtmkonferensiya2021@mail.ru elektron pochtasida qabul qilinadi.
Quyidagi yo'nalishdagi maqolalar qabul qilinadi:
👉 Aniq va tabiiy fanlarni zamonaviy pedagogik texnologiyalar asosida o‘qitish  metodikasi.
👉 Umumta’lim  fanlarini o‘qitishda  STEAM yondashuvning o’rni va ahamiyati. """

andoza = '[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
email = re.findall(andoza,matn)
print(email)

# Kuchli parolni tekshirish
# Quyidagi andoza ham ihateregex.io sahifasidan olindi
andoza = '^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$'
msg = "Yangi parol kiriting"
msg += '(kamida 8 belgidan iborat, kamida 1 ta lotin bosh harf, 1 ta kichik harf, '
msg += '1 ta son va 1 ta maxsus belgi boʻlishi kerak): '

while True:
    password = input(msg)
    if re.match(andoza,password):
        print("Maxfiy so'z qabul qilindi")
        break
    else:
        print("Maxfiy so'z talabga javob bermadi")










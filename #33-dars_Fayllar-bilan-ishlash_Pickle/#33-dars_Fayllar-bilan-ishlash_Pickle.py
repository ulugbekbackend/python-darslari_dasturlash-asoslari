# fayl=open('pi.txt')
# Pi=fayl.read()
# print(Pi)
# fayl.close()


# with open('pi.txt') as fayl:
#     pi = fayl.read()
# print(pi)
# pi = pi.rstrip()
# pi=pi.replace('\n','')
# print(pi)


# file='data/talabalar.txt'
# with open(file) as fayl:
#     # for line in fayl:
#         # print(line)
#     talabalar=fayl.readlines()
#     talabalar=[talaba.rstrip() for talaba in talabalar]
#     print(talabalar)

# faylnomi = 'ustozlar.txt'# ochilayotgan (yaratilayotgan) fayl nomi
# with open(faylnomi,'w') as fayl:
#     fayl.write('anvar narzullaev') # faylga yozilayotgan ma'lumot

# faylnomi = 'new_file.txt'
# ism = 'Olimjon Hasanov'
# tyil = 2004
# with open(faylnomi,'w') as fayl:
#     fayl.write(ism)
#     fayl.write(tyil)

# faylnomi = 'new_file.txt'
# ism = 'Olimjon Hasanov'
# tyil = 2004
# with open(faylnomi,'w') as fayl:
#     fayl.write(ism)
#     fayl.write(str(tyil))

# faylnomi = 'new_file.txt'
# ism = 'Olimjon Hasanov'
# tyil = 2004
# with open(faylnomi,'w') as fayl:
#     fayl.write(ism+'\n')
#     fayl.write(str(tyil)+'\n')

# faylnomi = 'new_file.txt'
# with open(faylnomi,'a') as fayl:
#     fayl.write('Alijon Valiyev\n')
#     fayl.write('2000')


import pickle

talaba1 = {'ism':'hasan', 'familiya':'husanov', 'tyil':2003, 'kurs': 2}
talaba2 = {'ism':'alijon', 'familiya':'valiyev', 'tyil':2004, 'kurs': 1}

# with open('info','wb') as file:
#     pickle.dump(talaba1,file)
#     pickle.dump(talaba2,file)

with open('info','rb') as file:
    talaba1 = pickle.load(file)
    talaba2 = pickle.load(file)
print(talaba1)
print(talaba2)


while True:
    book = input("Yaxshi koʻrgan kitobingizni kiriting (to'xtash uchun Enter bosing): ")
    if not book: break
    with open('books.txt','a') as file:
        file.write(book+'\n')

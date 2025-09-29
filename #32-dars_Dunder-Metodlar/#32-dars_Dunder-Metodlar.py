from uuid import uuid4

class Avto:
    """Avtomobil klasi"""
    __num_avto=0
    def __init__(self,make,model,rang,yil,narx,km=0):
        self.make=make
        self.model=model
        self.rang=rang
        self.yil=yil
        self.narx=narx
        self.__km=km
        self.__id=uuid4()
        Avto.__num_avto+=1
        
    def __repr__(self):
        return f"{self.rang} {self.make} {self.model}"

    def __eq__(self, avto):
        """Tenglik"""
        return self.narx==avto.narx
        
    def __lt__(self,avto):
        """Kichik"""
        return self.narx<avto.narx
    
    def __le__(self,avto):
        """Kichik yoki teng"""
        return self.narx<=avto.narx
    
    @classmethod
    def get_num_avto(cls):
        return cls.__num_avto
        
    def get_km(self):
        return self.__km
    
    def get_id(self):
        return self.__id

    def add_km(self,km):
        if km>=0:
            self.__km+=km
        else:
            return "Mashina km kamaytirib bo\'lmaydi"

class AvtoSalon:
    """Avtosalon klassi"""
    def __init__(self,name):
        self.name = name
        self.avtolar = []

    def __repr__(self):
        return f"{self.name} avtosaloni"

    def add_avto(self,*qiymat):
        for avto in qiymat:
            if isinstance(avto,Avto): # agar avto Avto klassidan bo'lsa
                self.avtolar.append(avto)
            else:
                print("Avto obyketini kiriting")

    def __len__(self):
        return len(self.avtolar)
    
    def __getitem__(self,index):
        return self.avtolar[index]
    
    def __setitem__(self,index,value):
        if isinstance(value,Avto):
            self.avtolar[index]=value
    
    def __add__(self,qiymat):
        if isinstance(qiymat,AvtoSalon):
            yangi_salon=AvtoSalon(f"{self.name} {qiymat.name}")
            yangi_salon.avtolar=self.avtolar+qiymat.avtolar
            return yangi_salon
        elif isinstance(qiymat,Avto):
            self.add_avto(qiymat)
        else:
            print(f"AvtoSalon ga {type(qiymat)} qo`shib bo`lmaydi")
            
    def __call__(self,*parametr):
        if parametr:
            for avto in parametr:
                self.add_avto(avto)
        else:
            return [avto for avto in self.avtolar]
            
        
# avto1=Avto("GM","Malibu","qora",2020,35000,1000)
# avto2 = Avto("GM","Lacetti","Oq",2020,20000)
# print(avto1)

# # Avto obyektlarini yaratamiz
# avto1 = Avto("GM","Malibu","Qora",2020,40000)
# avto2 = Avto("GM","Lacetti","Oq",2020,20000)
# avto3 = Avto("Toyota",'Carolla',"Silver",2018, 45000)

# # Yuqoridagi obyektlarni salon1 ga qo'shamiz
# for avto in [avto1, avto2, avto3]: 
#     salon1.add_avto(avto)
# print(salon1)


# 2 ta avtosalon yaratamiz
salon1 = AvtoSalon("MaxAvto")
salon2 = AvtoSalon("Avto Lider")

# 6 ta avto obyektini yaratamiz
avto1 = Avto("GM","Malibu","Qora",2020,40000)
avto2 = Avto("GM","Lacetti","Oq",2020,20000)
avto3 = Avto("Toyota",'Carolla',"Silver",2018, 45000)
avto4 = Avto("Mazda", "6", 'Qizil',2015,35000)
avto5 = Avto("Volkswagen","Polo",'Qora',2015,30000)
avto6 = Avto("Honda","Accord","Oq",2017,42000)

# Birinchi uchta avtoni birinchi salonga, keyingi uchtasini 2-salonga qo'shamiz.
salon1.add_avto(avto1, avto2, avto3)
salon2.add_avto(avto4, avto5, avto6)

newAvto = Avto("BMW", 'X7','Qora',2015,75000)
# salon1 + newAvto
# print(salon1[:])
avto_new = Avto("Mercedes-Benz", 'E200','Silver',2015,80000)
# Obyektni chaqiramiz:
salon1(avto_new) # Yangi avto qo'shamiz
salon1() # salondagi mashinalarni ko'ramiz


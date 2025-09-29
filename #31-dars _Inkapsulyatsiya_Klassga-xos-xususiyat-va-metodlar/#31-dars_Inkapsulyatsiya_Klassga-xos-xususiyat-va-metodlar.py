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
            return "Moshina km kamaytirib bo\'lmaydi"

class Shaxs:
    """Shaxslar haqida ma'lumot"""
    __odamlar_soni=0
    def __init__(self,ism,familiya,passport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.__tyil = tyil
        Shaxs.__odamlar_soni+=1
    
    @classmethod
    def odamlar_soni(cls):
        return cls.__odamlar_soni
        
        
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info
        
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.__tyil

avto1=Avto("GM","Malibu","qora",2020,35000,1000)
shaxs =Shaxs("Valijon","Aliyev","FA112299",2000)


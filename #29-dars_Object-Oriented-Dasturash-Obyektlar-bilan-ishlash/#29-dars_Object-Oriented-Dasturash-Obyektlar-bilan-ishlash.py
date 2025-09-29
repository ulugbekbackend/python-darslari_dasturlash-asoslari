class Talaba:
    def __init__(self,ism,familiya,tyil):
        self.ism=ism
        self.familiya=familiya
        self.tyil=tyil
        self.bosqich=1
    
    def get_info(self):
        return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi."
    
    def set_bosqich(self,bosqich):
        self.bosqich=bosqich
    
    def update_bosqich(self):
        self.bosqich+=1
    
    def get_name(self):
        return self.ism
    
    def get_lastname(self):
        return self.familiya
    
    def get_fullname(self):
        return f"{self.ism} {self.familiya}"
    
    def get_age(self,yil):
        return yil-self.tyil
    
    
class Fan():
    def __init__(self,nomi):
        self.nomi=nomi
        self.talabalar_soni=0
        self.talabalar=[]
        
    def add_student(self,talaba):
        self.talabalar.append(talaba)
        self.talabalar_soni+=1
    
    def get_students(self):
        return [talaba.get_info() for talaba in self.talabalar]
    
    def get_name(self):
        return self.nomi
    
    def get_students_num(self):
        return self.talabalar_soni
    
def see_methods(klass):
    return [method for method in dir(klass) if method.startswith('__') is False]
# print(see_methods(Talaba))

# print(talaba1.__dict__)
# print(talaba1.__dict__.keys())

# talaba1 = Talaba("Alijon","Valiyev",2000)
# talaba1.set_bosqich(3)
# print(talaba1.get_info())    

matematika = Fan("Oliy Matematika")
talaba1 = Talaba("Alijon","Valiyev",2000)
talaba2 = Talaba("Hasan","Alimov",2001)
talaba3 = Talaba("Akrom","Boriyev",2001)
matematika.add_student(talaba1)
matematika.add_student(talaba2)
matematika.add_student(talaba3)


class Avto():
    def __init__(self,model,rang,karobka,narx):
        self.model=model
        self.rang=rang
        self.karobka=karobka
        self.narx=narx
        self.kilometr=0
        
    def get_info(self):
        return f"Modeli: {self.model}, Rangi: {self.rang}, {self.karobka} karobka, Narxi: {self.narx}, Yurgan kilometri:{self.kilometr}"

    def update_km(self,yangi_km):
        self.kilometr=yangi_km
        return f"Yurgan kilometri: {self.kilometr}"
    
class Avtosalon():
    def __init__(self,Salon_nomi,manzil):
        self.salon_nomi=Salon_nomi
        self.manzil=manzil
        self.avtomobil=[]
        self.avtomobil_soni=0
        
    def get_info(self):
        return f"Avto Salon nomi: {self.salon_nomi}, Manzili: {self.manzil}."
   
    def add_avto(self,avtomobil):
        self.avtomobil.append(avtomobil)
        self.avtomobil_soni+=1
        
    def get_avto(self):
        return [avto.get_info() for avto in self.avtomobil]
    
    
        
avto1=Avto("Malibu", "Qora", "Avtomat", 33000)
avto2=Avto("Malibu", "Oq", "Avtomat", 30000)

uzavto=Avtosalon("Uzavto Andijon","Andijon")
uzavto.add_avto(avto1)
uzavto.add_avto(avto2)











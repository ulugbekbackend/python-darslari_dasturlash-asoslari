# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 21:40:51 2022

@author: Ulug'bek
"""

class Talaba:
    def __init__(self,ism,familiya,tyil):
        self.ism=ism
        self.familiya=familiya
        self.tyil=tyil
        
    def tanishtir(self):
        print(f"Ismim {self.ism} {self.familiya}. {self.tyil}-yil tug\'ilganman.")

    def get_name(self):
        return self.ism
    
    def get_lastname(self):
        return self.familiya
    
    def get_fullname(self):
        return f"{self.ism} {self.familiya}"
    
    def get_age(self,yil):
        return yil-self.tyil
    
class Login:
    def __int__(self,name,username,email):
        self.name = name
        self.uname = username
        self.mail = email
    
    def describe():
        pass
    
    def get_email():
        pass

talaba1 = Talaba("Alijon","Valiyev",2000)  
talaba2 = Talaba("Olim","Olimov",1995)
talaba3 = Talaba("Husan","Akbarov",2004)
talaba4 = Talaba("Hasan","Akbarov",2004)


class User:
    def __init__(self,login,name,lastname,email,tyil):
        self.login=login
        self.name=name
        self.lastname=lastname
        self.email=email
        self.tyil=tyil
    
    def get_info(self):
        return f"Foydalanuvchi: {self.login}, Foydalanuvchi ismi: {self.name} {self.lastname}, Email: {self.email}, Tug\'ilgan yili: {self.tyil}."

user=User("developer","Ulug'bek","Yo'ldoshev","ulugbek@gmail.com",2004)












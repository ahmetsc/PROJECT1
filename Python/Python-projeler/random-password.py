#Burada Random şifre oluşturma kodu yazıcağız.

from calendar import c
from random import *
from re import X

secim = input("Parola Oluşturmak için y/n:")

if secim == "y" or secim == "Y":
    Chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()"
    password =  "".join(choice(Chars) for x in range(randint(7, 14)))
    print("Şifreniz: ",password)
else:
    print("Programdan Çıkılıyor...")

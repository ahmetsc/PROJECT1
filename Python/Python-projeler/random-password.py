#Burada Random şifre oluşturma kodu yazıcağız.

from random import *

secim = input("Parola Oluşturmak için y/n:")

if secim == "y" or secim == "Y":
    Chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()"
    password =  "".join(choice(Chars) for x in range(randint(7, 14)))
    print("Şifreniz: ",password)
else:
    print("Programdan Çıkılıyor...")
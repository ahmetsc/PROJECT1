#Çok satırlı if-else koşullu durumdan tek satırlı olarak kullanılır.


#örnek1
cevap = input("x'in değeri 2 olsun mu? y/n: ")

if cevap == "y":
    x = 2
else:
    x = 0

print(x)

#örnek2
cevap = input("toplama yapılsın mı? y/n: ")
if cevap == "y" or cevap == "Y":
    num1 = input("1. Sayıyı gir: ")
    num2 = input("2. Sayıyı gir: ")
    secim =input("Toplama İşlemi ondalık olarak mı gösterisin y/n")
    if secim == "y" or secim == "Y":
        sum = float(num1) + float(num2)
        print(sum)
    else:
        sum = int(num1) + int(num2)
        print(sum)
else:
    print("Programdan Çıkılıyor...") 




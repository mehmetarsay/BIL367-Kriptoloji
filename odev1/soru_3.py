'''
3. RSA sisteminin nasıl hesaplandığını gördünüz, p q, e değerlerini 2 şer basamaklı 
sayılar şeklinde konsoldan yada ekrandan girdirtip, ardından verilen bir sayıyı önce
şifreleyen, ardından çözen, ve bu süreçte işlemleri yaparken bütün değerleri, 
hesaplamaları vs. satır satır açıklama şeklinde konsola yada ekrana yazan bir program 
oluşturun. çalıştırıp ekranlarını yazın.  ( bu işlemler sınavda gelecek büyük ihtimal
haberiniz olsun) . Sistem hata kontrolü yapıyorsa ekstra puan vereceğim, örneğin e 
değeri p-1*q-1 den fazla olamaz vs. gibi , bu tarz kontrolleri eklediyseniz ayrıca yazın. 

19-17-11
'''
import re


#Sayının Asal olup olmadığını kontrol etme
def IsPrime(a):
    if(a==2):
        return True
    elif((a<2) or ((a%2)==0)):
        print('Sayı asal değil')
        return False
    elif(a>2):
        for i in range(2,a):
            if not(a%i):
                print('Sayı asal değil')
                return False
    return True

#Sayıların aralarında asal olup olmadığını kontrol etme
def aralarindaAsal(a,b):
    number = 0
    if(a>b):
        number = b
    else:
        number = a
    if number > 1:
        for i in range(2,number+1):
            if (a % i) == 0 and (b % i) == 0:
                print(a,b," Aralarında Asal  Değildir.")
                return False
                break
            else:
                continue
        return True
 
    else:
        print(number," Sayılar uygun değil")
        return False

#RSA algoritması hesaplama
def Rsan(n1,n2,n3,sifrelenecekSayi):
    number = sifrelenecekSayi
    print('p değeri: ',n1)
    print('q değeri: ',n2)
    print('e değeri: ',n3)
    n = n1 * n2
    print('{n = ( n1 * n2 )} n değeri: ',n)
    totient = (n1 - 1) * (n2 - 1)
    print('{totient = (n1 - 1) * (n2 - 1)} totient değeri: ',totient)
    e = n3
    d = 0
    for i in range(1,999):
        d = (i * totient + 1)
        if(d%e!=0):
            continue
        else:
            d = (i * totient + 1) / e
            print('{d = (i * totient + 1) / e} d değeri: ',d,'   i: ',i)
            break
    sendPasswordValue = pow(number, e) % n
    receiverPAsswordValue = pow(sendPasswordValue, int(d)) % n
    print("Gerçek  Sayı: ", number)    
    print("Göndrln Şifre: ", sendPasswordValue)
    print("Çözülen Şifre: ", receiverPAsswordValue)



n1=int(input("İki basamaklı bir asal sayı girin : "))
while n1/10<1 or n1/10>10 or IsPrime(n1)==False:
    print('İki basamaklı bir sayı giriniz ')
    n1=int(input("İki basamaklı bir sayı girin : "))

n2 = int(input("İki basamaklı bir asal sayı girin : "))
while n2/10<1 or n2/10>10 or IsPrime(n2)==False:
    if n2<10 or n2>99:
        print('İki basamaklı bir sayı giriniz')
    n2=int(input("İki basamaklı bir asal sayı girin : "))

totientTemp = (n1 - 1) * (n2 - 1)
print(totientTemp,' ile aralarında asal ve ',totientTemp,'den küçük',' bir iki basamaklı sayı girin : ')
n3 = int(input())
while n3/10<1 or n3/10>10 or n3<1 or (aralarindaAsal(totientTemp,n3)==False) or n3>totientTemp:
    if n2<10 or n2>99:
        print('İki basamaklı bir sayı giriniz')
    elif n3>totientTemp:
        print('Girilen sayı ',totientTemp,'büyük olamaz')
    print(totientTemp,' ile aralarında asal ve ',totientTemp,'den küçük',' bir iki basamaklı sayı girin : ')
    n3=int(input())

sifrelenecekSayi = int(input('Sifrelenecek sayiyi giriniz: '))

if n1!=None and n2 != None and n3 != None:
    Rsan(n1,n2,n3,sifrelenecekSayi)

else:
    print('hata')

'''
2. 9 basamaklı 2 büyük asal sayı seçin. 
(Eğer bölme işleminin hesaplanması 5 dakikadan fazla sürüyorsa basamak sayısını 
küçültebilir yada 1 dakikanın altındaysa büyütebilirsiniz ) bu sayıları önce çarpan,
sonra çarpanlarına ayıran kod yazın. çarpanlarına ayırma algoritmasını düşünüp 
kendiniz tasarlayacaksınız, internetten fikirlere bakabilirsiniz. 
çalıştırın ve öncesine sonrasına timestamp koyup, geçen zamanı ölçüp kaydedin raporlayın.
programlama dili serbest, kodlara sunum şeklinde de anlattıracağım, kendiniz yazın.
bir kaç cümle ile ne öğrendiğinizi ve süreleri yazın, kodu da ekleyin. 


'''
import math
import time


sayi1 = 1558444061
sayi2 = 600000001

carpmaST = time.time()
sayi = sayi1*sayi2
carpmaET = time.time()

print('Çarpa tamamlanma süresi: ', carpmaET-carpmaST)


startTime = time.time()
sqrtSayi = math.sqrt(sayi)
for i in range(1,int((sqrtSayi))):
    if sayi % i == 0:
        print(str(i) + " * " + str(sayi//i) + " = " + str(sayi))

endTime = time.time()

print('Çarpanlarına ayırma tamamlanma süresi: ', endTime-startTime)







'''
1. Bazı işlemleri tek yönlü yapmak kolay ama tersini alması çok zordur. 
Örneğin boyayı karıştırınca geri döndüremezsiniz. Yada çarpma işleminin
 tersi zor diye derste bahsetmiştik. Aklınıza gelen 1 tane yaratıcı, 
 bilgisayar üstünde tek yönlü hızlı, tersi çok zor olan birşey düşünüp 
 bir kaç cümle ile kriptolojide nasıl kullanılabileceğini yazınız. 

'''


primaryKey = 13

def func(string):
    newString =''
    for i in string:
        newString += chr(int(ord(i))%primaryKey+ord(i))
    return newString

print(func(''))
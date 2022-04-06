import hashlib


def encrypt(password):
    plaintext = password.encode()
    d = hashlib.sha256(plaintext)
    hash = d.hexdigest()
    return hash

def signIn():
    print('\nKayıt olma menüsü\n')

    f_search = open("deneme2.txt", "r")

    username = input('Kullanıcı adı: ')

    data_list = []
    data = f_search.read()
    data_s = data.split('\n')
    for value in data_s:
        data_list.append(value.split('\\'))
    user_control = False
    for val_s in data_list:
        if val_s[0] == username:
            user_control = True
        
    if user_control:
        print('\nKullanıcı Var Yeniden dene\n')
        splash()
        return

    f_search.close()
    password = input('Şifre: ')

    password_encrypt = encrypt(password)

    f_write = open("deneme2.txt", "a")
   
    string = username+'\\'+password_encrypt+'\n'

    f_write.write(string)
    print('Kayıt Başarılı\n')



def login():
    print('\nLogin menüsü\n')
    f_read = open("deneme2.txt", "r")
    data_list = []

    data = f_read.read()
    data_s = data.split('\n')
    for value in data_s:
        data_list.append(value.split('\\'))

    username = input('Kullanıcı adı: ')
    user_control = True
    user_password=''
    for val_s in data_list:
        if val_s[0] == username:
            user_password = val_s[1]
            user_control = False

    if user_control:
        print('Kullanıcı Bulunamadı')
        login()
        return

    password = input('Şifre: ')
    password_encrypt = encrypt(password)

    while user_password != password_encrypt:
        print('Şifre Yanlış')
        password = input('Şifre: ')
        password_encrypt = encrypt(password)
    
    print('Sisteme Hoşgeldiniz ',username)

def splash():
    print('Kayıt Ol (1)')
    print('Giriş Yap (2)')
    input_d = input('Seçiminiz: ')
    print(input_d)
    while input_d != '1' and input_d != '2':
        input_d = input('Hatalı Seçim Yeniden Seç: ')
        print(input_d)
    if(input_d=='1'):
        signIn()
    elif(input_d=='2'):
        login()

#main
splash()
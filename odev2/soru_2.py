import hashlib
import random
import string


def get_random_string():
    result_str = ''.join(random.choice(string.ascii_letters) for i in range(500))
    return result_str
    
def func(text_result):
    print(text_result)
    md5 = hashlib.md5(text_result.encode())
    print('md5 encrypt: ', md5.hexdigest())


text = get_random_string()

func(text)

for i in range(50):
    random_str = random.choice(string.ascii_letters)
    print(i,':',text[0],'-->',random_str)
    text_l = list(text)
    text_l[i] = random_str
    text = ''.join(text_l)
    func(text)
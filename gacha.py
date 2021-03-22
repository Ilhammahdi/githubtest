x = input(" masukkan kata: ")

import random

bintang = ("bintang 1","bintang 2","bintang 3","bintang 4","bintang 5")
a = random.choice(bintang)
print(a)

import random
for i in range(100):
    a = random.randrange(100) 
    if a <= 40 : 
        print("Bintang 1")
    elif a >= 41 and a <= 70 :
        print("Bintang 2")
    elif a >= 71 and a <= 87 :
        print("Bintang 3")
    elif a >= 88 and a <= 99  :
        print("Bintang 4")
    elif a == 100 :
        print("Bintang 5 MANTAP")
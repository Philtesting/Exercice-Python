from random import *

def list_aleat(n):
    s = [0]*n
    for i in range(n):
        s[i] = random()
    return s

n=int(input("donner moi la taille de votre liste aléatoire: "))
print(list_aleat(n))
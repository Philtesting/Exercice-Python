from Ex34 import *
#Ceci est correct :
matrice = [[combinaisons(n,p)
            for p in range(n+1)] for n in range(1,5)]
print(matrice)
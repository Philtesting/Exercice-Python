from time import time
t1 = time()
s = "Ce programme a affiche {0} lignes "
s += "en {1:.6f} secondes"
for i in range(1,101):
    print (s.format(i,time()-t1))
import math
import os

f = open('dm.txt', 'r+')
l = f.readlines()
dm = 0
r = open('dm2.txt', 'r+')
for a in range(len (l)):
    dm = float(l[a])
    vol = (1/6) * math.pi * (dm**3)
    sur = math.pi * (dm**2)
    sec = math.pi * (dm/2)**2
    r.write("Diam. %.2f cm Section = %.2f cm Surf. = %.2f cm. Vol. = %.2f cm\n"%(dm,sec,sur,vol))

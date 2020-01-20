from decimal import Decimal

f = open('toto.txt', 'r+')
l = f.readlines()
dm = 0
for a in range(len (l)):
    dm = float(l[a])
    dm = round(dm,1)
    if (round(dm,0) > dm):       
        dm = round(dm,0) - 0.5
    else:
        dm = round(dm,0)
    
    print(dm)


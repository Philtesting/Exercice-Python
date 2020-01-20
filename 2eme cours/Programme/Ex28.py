from math import log
m = 7293041
l2 = int(log(m)/log(2))
binaire = [m%2**(i+1)//2**i for i in range(l2+1)]
print(binaire)
from math import sqrt

n = [i for i in range (1,100)]

for i in range(1,61):
    x = i * sqrt(2)
    n.insert(int(x)+i-1,x)
print(n)

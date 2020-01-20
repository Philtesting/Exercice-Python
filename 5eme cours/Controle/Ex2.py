def reste(x):
    f = x % 2
    return f

x=int(input("Donner moi un entier: "))
print(reste(x))

liste1 = [1,2,3,4,5,6]
liste2 = [7,8,9,10,1,2]
liste3 = []
for i in liste1:
    if i in liste2:
        liste3.append(i)
print(liste3)

from numpy import *
a = [[1, 0], [0, 1]]
b = [[4, 1], [2, 2]]
print(np.matmul(a, b))
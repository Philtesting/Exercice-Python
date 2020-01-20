n=[]
Z,U,D,T,Q,C=0,0,0,0,0,0

for i in range(10):
    x = float(input("Nb entre 0 et 5:"))
    
    while x < 0 or x > 5:
        x = float(input("Nb entre 0 et 5:"))
    
    n.insert(i,x)
    
print(n)

for a in range(10):

        if n[a] == 0:
            Z += 1
        if n[a] == 1:
            U += 1           
        if n[a] == 2:
            D += 1
        if n[a] == 3:
            T += 1
        if n[a] == 4:
            Q += 1
        if n[a] == 5:
            C += 1

print ("Nb de 0:",Z,"avec une fréquence de :",Z/10)
print ("Nb de 1:",U,"avec une fréquence de :",U/10)
print ("Nb de 2:",D,"avec une fréquence de :",D/10)
print ("Nb de 3:",T,"avec une fréquence de :",T/10)
print ("Nb de 4:",Q,"avec une fréquence de :",Q/10)
print ("Nb de 5:",C,"avec une fréquence de :",C/10)


n=[]
i=0
a = 'a'

while a == 'a':
    
    x = float(input("Nb entre 0 et 5:"))
    
    while x < 0 or x > 5:
        x = float(input("Nb entre 0 et 5:"))
    
    n.insert(i,x)
    i += 1
    a = str(input("Taper 'a' pour continuer:"))
    
    
print(n)

print ("Nb de 0:",n.count(0),"avec une fréquence de :",n.count(0)/len(n))
print ("Nb de 1:",n.count(1),"avec une fréquence de :",n.count(1)/len(n))
print ("Nb de 2:",n.count(2),"avec une fréquence de :",n.count(2)/len(n))
print ("Nb de 3:",n.count(3),"avec une fréquence de :",n.count(3)/len(n))
print ("Nb de 4:",n.count(4),"avec une fréquence de :",n.count(4)/len(n))
print ("Nb de 5:",n.count(5),"avec une fréquence de :",n.count(5)/len(n))


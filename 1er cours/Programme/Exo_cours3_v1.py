n=[]


for i in range(10):
    x = float(input("Nb entre 0 et 5:"))
    
    while x < 0 or x > 5:
        x = float(input("Nb entre 0 et 5:"))
    
    n.insert(i,x)
    
print(n)

print ("Nb de 0:",n.count(0),"avec une fréquence de :",n.count(0)/10)
print ("Nb de 1:",n.count(1),"avec une fréquence de :",n.count(1)/10)
print ("Nb de 2:",n.count(2),"avec une fréquence de :",n.count(2)/10)
print ("Nb de 3:",n.count(3),"avec une fréquence de :",n.count(3)/10)
print ("Nb de 4:",n.count(4),"avec une fréquence de :",n.count(4)/10)
print ("Nb de 5:",n.count(5),"avec une fréquence de :",n.count(5)/10)

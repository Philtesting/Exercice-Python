def calculX(x):
    for i in range(1,x):
        l =[ i * f for f in range (1,x)]
        affX(l)
def affX(l):
    print ("\t".join(str(e) for e in l))

x = int (input("Donner moi in entier: "))
calculX(x+1)


    
    



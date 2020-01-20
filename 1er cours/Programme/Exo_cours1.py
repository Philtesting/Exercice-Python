n=[]
H=[]
m,M,N,S=0,0,0,0

for i in range(10):
    x = str(input("Caractere: "))
    n.insert(i,x)
print(n)

for a in range(10):
    
    for b in range(len(n[a])):
        if n[a][b].isdigit():
            N += 1
        if n[a][b].isspace():
            S+= 1           
        if n[a][b].isupper():
            M+= 1
            H.append(n[a][b])
        if n[a][b].islower():
            m+= 1

print("Nb de chiffres:",N)
print("Nb de espace:",S)
print("Nb de majuscule:",M)
print("Nb de minuscule:",m)
print("Liste des majuscule:",H)
    
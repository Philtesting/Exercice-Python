i = 0
f = open("lol.txt","r+")
n = f.readlines()
max = len(n)
N, NB = 0, 0
for a in range(max):
    for b in range(len(n[a])):
        if n[a][b].isdigit():
            N += 1
    if (N != 0):
        N = 0
        NB += 1 

print("On a %s lignes contenant des caractères numériques" %(NB))
f.close()

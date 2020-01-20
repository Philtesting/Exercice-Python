f = open('lol.txt', 'r')
l = f.readlines()


for a in range(len (l)):
        if l[a][0].islower():
            l[a] = l[a].capitalize()

print("".join(l))



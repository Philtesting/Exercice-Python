f = open('lol.txt', 'r')
p = f.read()
nbMot = p.count(' ') + p.count('\n')
print ("Ce fichier a", nbMot,"mots")
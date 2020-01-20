## EXERCICES DE PYTHON DEVELOPPEZ

# Exercice 10.2:

ch ="erodslqazrdsa212309"

n = 5

a= 0
b = n             
lt = []                
while a < len(ch):
	if b > len(ch): 
		b = len(ch)
	dec = ch[a:b]     
	lt.append(dec)       
	a = b
	b = b + n      
print(lt)

ch = ""              
i = len(lt)            
while i > 0 :
	i = i - 1        
	ch = ch + lt[i]
print(ch)

# Exercice 10.3:

def trouve(a,b) :

    for i in range(0,len(a)) :
        if a[i] == b :
            return i
    return -1

print (trouve("Juliette &  Roméo", "&"))

# Exercice 10.4:

def trouve(a,b,c=0) :
    for i in range(c,len(a)) :
        if a[i] == b :
            return i
    return -1

print (trouve("César & Cléopâtre", "r", 5))

# Exercice 10.5:

def compteCar(a,b) :
    n = 0
    for x in a :
        if x == b :
            n += 1
    return n

print (compteCar("ananas au jus","a"))

# Exercice 10.6:

prefixes = 'JKLMNOP'
suffixe = 'ack'
for x in prefixes :
    print (x + suffixe)

# Exercice 10.7:

def compteMots(cara):
    if len(cara) == 0:
        return 0
    one = 1 
    for i in cara:
        if i == " ": 
            one = one + 1
    return one

print (compteMots("Recherche du nombre de mots donnés dans une phrase"))

# Exercice 10.8:

def majuscule(cara):
    return (cara in u"ABCDEFGHIJKLMNOPQRSTUVWXYZ")

print (majuscule('e'), majuscule('E'))

# Exercice 10.9:

def chiffre(chif):
    return (chif in "0123456789")

print (chiffre('a'), chiffre('9'))

# Exercice 10.10:

def phrase(chaine):

    chaine = chaine.split(" ")
    return chaine


print(phrase("Je mets des mots dans des listes"))

# Exercice 10.12:

def majuscule(ch):
    return ('A' <= ch <= 'Z')


print(majuscule("a"),majuscule("B"))

# Exercice 10.13:

def majmin(ch):
        if 'A' <= ch <= 'Z' or 'a' <= ch <= 'z':
          return ("vrai")
        else:
          return ("faux")

print(majmin("a"),majmin("B"),majmin("1"))

# Exercice 10.14:

def chiffre(chiff):
    return (chiff in "0123456789")
 
print (chiffre('d'), chiffre('7'))

# Exercice 10.15:

ch1 = "Nombre de Majuscules Dans une Phrase"
cpt = 0

for i in ch1:
    if i.isupper():
        cpt += 1
        
print ("Nombre de Majuscules Dans une Phrase:", cpt)

# Exercice 10.17:

ch = "BONJOUR JE CONVERTIS"
print("Convertis la phrase en minuscule: ", ch.lower(), "\n")

# Exercice 10.18:

ch2 = "JE CONVERTIS LES MAJUSCULES en minscules et idem pour les minuscules"

print("Convertis les mots majuscules en minuscules et vice-versa: ", ch2.swapcase(), "\n")

# Exercice 10.19:

def caractere(cara):
       ch2 = 'Long'
       return "Le caractère 'long' a été répété: ", cara.count(ch2)

print(caractere("Long est le temps qui passe"))


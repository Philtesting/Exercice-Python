v = 'oui'
l = []
i = 0
N,M,m = 0,0,0

while v == 'Oui' or v == 'oui':
    a = str(input("Entrer 1 caractere: "))
    b = ord(a)
    print("Code ASCII de",a,"est: ",b)
    
    l.insert(i,a)
    
    if l[i].isdigit():
        N += 1
    if l[i].isupper():
        M += 1
    if l[i].islower():
        m += 1
    i += 1
    
    v = str(input("Voulez vous continuer [Oui|Non]? "))

print("Vous avez entrer:",N,"chiffres,",M,"lettres majuscules et",m,"lettres minuscules")
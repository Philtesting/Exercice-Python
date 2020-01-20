v = 'oui'
while v == 'Oui' or v == 'oui':
    a = str(input("Entrer 1 caractere: "))
    b = ord(a)
    print("Code ASCII de",a,"est: ",b)
    v = str(input("Voulez vous continuer [Oui|Non]? "))
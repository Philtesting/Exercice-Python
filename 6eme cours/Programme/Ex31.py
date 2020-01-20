def maj(liste):
    return all(ord(c) in range(65,91)
               for c in liste)

l1 = ['A','H','Z','T']
l2 = ['B','v','R','?']
print(maj(l1))
print(maj(l2))
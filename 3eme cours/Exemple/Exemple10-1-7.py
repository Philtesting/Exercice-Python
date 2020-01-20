def minuscule(ch):
    if 'a' <= ch <= 'z' :
        return 1
    else:
        return 0

mot = str(input("Entrez un mot quelconque : "))
print(minuscule(mot))

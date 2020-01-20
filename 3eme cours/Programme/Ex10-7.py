def compteMots(cara):
    if len(cara) == 0:
        return 0
    one = 1 
    for i in cara:
        if i == " ": 
            one = one + 1
    return one

print (compteMots("Recherche du nombre de mots donnés dans une phrase"))

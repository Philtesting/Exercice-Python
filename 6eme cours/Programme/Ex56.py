def comptage(l):
    dico = {}
    for m in l:
        dico[m] = len(m)
    return dico
print(comptage(['Debout', 'vieux','revolutionnaire']))
def lignes(s):
    mots = s.split()
    lignes = ['']
    for m in mots:
        m += " "
        if len(lignes[-1])+len(m)<24:
            lignes[-1] += (m)
        else:
            lignes.append(m)
    return lignes
s = "Onze ans deja que cela passe vite Vous "
s += "vous etiez servis simplement de vos armes la "
s += "mort n'eblouit pas les yeux des partisans Vous "
s += "aviez vos portraits sur les murs de nos villes"
print(lignes(s))
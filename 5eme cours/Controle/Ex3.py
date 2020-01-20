def remove(p):
    p.pop(len(p)-1)
    return p
p = [1,2,3]
print(remove(p))


def Somme(X,Y):
    resultat = [[0,0],
                [0,0]]
    for i in range(len(X)):
       for j in range(len(X[0])):
           resultat[i][j] = X[i][j] + Y[i][j]
    return resultat

arbre= ['A',[
            ['B',[
                ['E',[]],
                ['F',[]],
                ]
            ]
            ['C',[]],
            ['D',[
                ['G',[]]
                ]
            ]
           ]
        ]
def ParcourIternactif(racine):
    while file_sommets == arbre:
        arbre_courrant=fiche_sommet.pop(0)
        sommet_courrant=arbre_courrant[0]
        enfant_courrant=arbre_courrant[1]
        print(sommet_courrant)
        for enfant in enfant_courant:
            if enfant:
                fiche_sommets.append(enfant)
filesommets = [arbre]
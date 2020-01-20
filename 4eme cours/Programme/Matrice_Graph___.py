#Tableau(vecteur)->liste / Matrices --> liste de liste
#Pile et File --> liste
#Arbre/GRAphes --> liste de liste
#Dictionnaire --> liste de liste
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
#1 (Arbre)
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

ParcourIternactif(arbre)

#2 (Arbre)
def ParcourRecursif(racine):
    sommet= racines [0]
    enfant= racines[1]
    print(sommet)
    for noeud in enfant:
        ParcourRecursif(racine)

ParcourIternactif(arbre)   

#3 (Graphes)
def voisi(u,g):
    liste=[]
    for i in range (len(g)):
        element_a_etudier = g[i]
        if element_a_etudier [0] == u or element_a_etudier [1] == u:
            liste.append(element_a_etudier)
    return liste

dico_graph={"A":["B"], "B":["A","C","D"],"C":["B","D"], "D":["B","C"]}

def TraverserRecursif(graph,sommet):
    sommets_visites.append(sommet)
    print(sommet)
    for voisin in graph[sommet]:
        if(not voisin in sommet_visites):
            TraverserRecursif(graph,sommet)
sommet_visites = []
TraverserRecursif(dico_graph,'A')
def TranverserInterractif(graph,sommet):
    sommets_a_visiter =[sommet]
    while sommets_a_visiter:
        sommet_courrant=sommets_a_visiter.pop(0)
        if(not sommet_courrant in sommets_visites):
            sommet_visites.append(somet_courant)
            print(sommet_courant)
            
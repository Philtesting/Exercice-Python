### D/ Dictionnaire => liste de listes

# Exercice: Representer en Python sous forme d'un dictionnaire le graphe suivant:

dico_graphe = {'A':['B'],'B':['A','C','D'], 'C': ['B','D'], 'D':['B','C']}

# Chaque association du dictionnaire est une paire (sommet, liste).
# Les clés sont les noms des sommets ce qui permet un accès direct au travers du dictionnaire.

# Exercice:
# 1 => Faire une fonction qui fait un parcours récursif en profondeur
# 2 => Faire une fonction qui fait un parcours itératif en longeur


# Solution 1:

def TraverserDepuisRecursive(graphe,sommet):
   sommets_visites.append(sommet)
   print (sommet)
   for voisin in graphe[sommet]:
      if (not voisin in sommets_visites):
         print(TraverserDepuisRecursive(graphe, voisin))
sommets_visites = []
print(TraverserDepuisRecursive(dico_graphe, "A"))


# Solution 2:

def TraverseIteratif(graphe,sommet):
    sommets_a_visiter = [sommet]
    while sommets_a_visiter:
        sommet_courant = sommets_a_visiter.pop(0)
        if(not sommet_courant in sommets_visites):
            sommets_visites.append(sommet_courant)
            print (sommet_courant)
            print(sommets_a_visiter.extend(graphe[sommet_courant]))
            
sommets_visites = []
print(TraverseIteratif(dico_graphe, 'A'))

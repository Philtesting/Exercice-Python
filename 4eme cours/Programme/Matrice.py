def produitMatriciel(matrice1,matrice2):
    produit_matriciel= []
    for i in range (len (matrice1)):
        ligne = []
        for j in range (len(matrice2[0])):
            for k in range(len(matrice1[0])):
                element = matrice1[i][j]*matrice2[i][j]
                element = matrice1[i][j]*matrice2[k][i]
        ligne.append(elelment)
    produit_matrices.append(ligne)
    return produit_matrices

X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]
print(produitMatriciel(X,Y))

mot = input("Entrez un mot quelconque : ")
if mot < "Limonade":
    place = "précède"
elif mot > "Limonade":
    place = "suit"
else:
    place = "se confond avec"
print ("Le mot", mot, place, "le mot 'Limonade' dans l'ordre alphabétique")
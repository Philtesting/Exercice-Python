liste1 = [1,2,3,4,5,6]
liste2 = [7,8,9,10,1,2]
liste3 = []
for i in liste1:
    if i in liste2:
        liste3.append(i)
print(liste3)

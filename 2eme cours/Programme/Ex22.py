liste1 = [1,2,3,3,4,5,6,1,7,4]
liste2 = [7,8,4,10,1,2,3,3]
liste3 = []
for i in liste1:
    if i in liste2 and not i in liste3:
        liste3.append(i)
print(liste3)

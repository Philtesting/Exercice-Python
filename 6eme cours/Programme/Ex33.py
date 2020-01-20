liste1 = [(1,-3), (5,2), (-7,0), (2,9), (7,0)]
liste2 = [(2,6), (-3,-1), (4,0), (5,-1)]

for (i,v) in enumerate(liste2):
    print(min(liste1, key =
        lambda x:(x[0]-v[0])**2+(x[1]-v[1])**2))
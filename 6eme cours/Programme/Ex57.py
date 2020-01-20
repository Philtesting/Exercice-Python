def successeurs(l):
    sux = {}
    for (v1,v2) in l:
        if not v1 in sux:
            sux[v1] = set()
        if not v2 in sux:
            sux[v2] = set()
        sux[v1].add(v2)
        sux[v2].add(v1)
    return sux
g = [(1,3),(2,4),(2,3),(3,5),(4,5)]
print(successeurs(g))
        
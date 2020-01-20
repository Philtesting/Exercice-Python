def triangles(g1):
    return any([set(e3) == set(e1)^set(e2) for
        e1 in g1 for e2 in g1 for e3 in g1])
def triangles2(g2):
    return any([i1 in s2 and len(s1&s2) > 0 for
        (i1,s1) in g2.items() for s2 in g2.values()])

print(triangles([(1,2),(3,4),(4,5),(2,4),(4,1)]))
print(triangles2({1:{2,3},2:{1,4},3:{1,4},4:{2,3}}))
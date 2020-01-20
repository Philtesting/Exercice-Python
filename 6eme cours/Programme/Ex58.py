def fusion(d1,d2):
    d3 = d1.copy()
    d3.update(d2)
    return d3
print(fusion({1:2,3:4},{3:5,7:9}))

def f(l1):
    l2=[]
    l3=[]
    for i in range(len(l1)):
        l2.append([])
        l3.append([])
        for x in range(len(l1)):
           l2[i].append(l1[i-x])
        if l2[i] not in l3:
            l3[i] = l2[i]
    return l3
l=[1,2,3,5,7]
print(f(l))

            
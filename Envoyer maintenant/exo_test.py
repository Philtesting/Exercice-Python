l1 = [1, 4, 7, 0]
l2 = [2, 9, 1, 4]

l = [x for x in set(l1) & set(l2)]
print(l)
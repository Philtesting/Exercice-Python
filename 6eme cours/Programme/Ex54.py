s1 = {2, 3, 7}
s2 = {2, 3, 5, 7, 9}
s3 = {3, 8}

def sousensemble(x,y):
    return all(i in y for i in x)

print(sousensemble(s1,s2))
print(sousensemble(s3,s2))
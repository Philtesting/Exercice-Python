m1 = (2,3,6,5)
m2 = (1,1,2,4)

def multiply(x,y):
    return sum([x[i]*y[i] for i in range(len(x))])

print(multiply(m1,m2))
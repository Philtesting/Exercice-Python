x = [1, 2]
y = [1, 2]
def f():
    z = x[:]
    z[0] = 7
    y = [6, 6]
    print(z,y)
f()
print(x,y)
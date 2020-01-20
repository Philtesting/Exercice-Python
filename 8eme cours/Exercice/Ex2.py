def factorielle(n):
    f = 1
    for i in range(1,n+1):
        f *= i
    return f

x = int(input("donner moi un entier: "))
print("%s! = %s"%(x,factorielle(x)))


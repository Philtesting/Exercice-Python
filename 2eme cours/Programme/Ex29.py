a = int(input("Donner moi une grandes valeurs de n:"))
for n in range(a):
    s1 = sum([i for i in range(n+1)])
    s2 = sum([i**2 for i in range(n+1)])
    print(s1 == n*(n+1)//2)
    print(s2 == n*(n+1)*(2*n+1)//6)
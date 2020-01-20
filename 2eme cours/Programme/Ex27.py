from math import factorial
n = 9
nCp = []
for p in range(n+1):
        x = factorial(n)//(factorial(p)*factorial(n-p))
        if x % 2 == 0:
            nCp.append(x)
print(nCp)
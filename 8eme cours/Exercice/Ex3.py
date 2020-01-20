def conversion(f,n):
    c = 0
    for i in range(n+1):
        c = c + 5*(f-32)/9
        print("%.2f fahrenheit = %.2f celsius"%(f, c))
        f += 5

x = float(input("donner moi les fahrenheit: "))
y = int(input("combien de fois le voulez vous de 5 en 5: "))
conversion(x,y-1)
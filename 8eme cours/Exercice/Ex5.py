def fibonacci(n):
    n1 = 0
    n2 = 1
    count = 0
    print("Fibonacci pour",n,"therme: ")
    while count < n:
       print(n1,end=' , ')
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1

n = int(input("Vous voulez fibunacci jusqu'a quel therme (attention le therme doi être supérieur ou égal a 2)? "))
while n < 2:
    n = int(input("Vous voulez fibunacci jusqu'a quel therme (attention le therme doi être supérieur ou égal a 2)? "))
fibonacci(n)
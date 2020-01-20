from math import sqrt
def is_prime(q):
    if q%2 == 0:
        return q==2
    else:
        borne = int(sqrt(q))+1
        p = 3
        while p<=borne and q%p != 0:
            p = p + 2 + 2*(p%6 == 1)
        return p>borne
print(sum(2*x + 1 for x in range(1,5000)
              if is_prime(2*x + 1)))
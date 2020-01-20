def compteCar(a,b) :
    n = 0
    for x in a :
        if x == b :
            n += 1
    return n

print (compteCar("ananas au jus","a"))
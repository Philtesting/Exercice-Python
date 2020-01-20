def trouve(a,b) :

    for i in range(0,len(a)) :
        if a[i] == b :
            return i
    return -1

print (trouve("Juliette &  Roméo", "&"))

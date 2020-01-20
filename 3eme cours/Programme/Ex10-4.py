def trouve(a,b,c=0) :
    for i in range(c,len(a)) :
        if a[i] == b :
            return i
    return -1

print (trouve("César & Cléopâtre", "r", 5))
